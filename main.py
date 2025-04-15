from src.autocorrect import correct_sentence
from src.predictor import predict_next
import nltk
nltk.download('punkt')


sentence = "helo how ar"


corrected = correct_sentence(sentence)
print(f"Autocorrected: {corrected}")

next_word = predict_next(corrected)
print(f"Predicted next word: {next_word}")
