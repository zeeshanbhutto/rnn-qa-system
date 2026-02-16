import torch
from app.model.rnn_model import SimpleRNN

class QAPredictor:
    def __init__(self, model_path):
        checkpoint = torch.load(
            model_path,
            map_location="cpu",
            weights_only=False
        )

        self.vocab = checkpoint["vocab"]
        self.inv_vocab = {v: k for k, v in self.vocab.items()}

        self.model = SimpleRNN(
            vocab_size=len(self.vocab),
            embedding_dim=checkpoint["embedding_dim"],
            hidden_dim=checkpoint["hidden_dim"],
            output_dim=checkpoint["output_dim"]
        )

        self.model.load_state_dict(checkpoint["model_state"])
        self.model.eval()

    def predict(self, question):
        tokens = question.lower().split()
        indices = [self.vocab.get(t, 0) for t in tokens]

        x = torch.tensor(indices).unsqueeze(0)

        with torch.no_grad():
            output = self.model(x)
            idx = torch.argmax(output, dim=1).item()

        return self.inv_vocab.get(idx, "I don't know")
