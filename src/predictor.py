def predict_next(word):
    dummy_predictions = {
        "hello": "world",
        "how": "are",
        "i": "am",
    }
    return dummy_predictions.get(word.lower(), "<next word>")
