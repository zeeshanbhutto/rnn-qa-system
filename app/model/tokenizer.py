def tokenize(text: str):
    text = text.lower()
    text = text.replace("?", " ").replace("'", "")
    return text.split()

def text_to_indices(text, vocab):
    return [vocab.get(token, vocab["<UNK>"]) for token in tokenize(text)]
