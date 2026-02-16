# save_artifacts.py
import torch
import pickle
from app.main import model , vocab 
torch.save(model.state_dict(), "artifacts/model.pt")

with open("artifacts/vocab.pkl", "wb") as f:
    pickle.dump(vocab, f)
