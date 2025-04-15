from src.autocorrect import correct_word
from src.predictor import predict_next

# Test autocorrect
print("Autocorrect test:")
print(f"Input: wrld → Correction: {correct_word('wrld')}")

# Test next word prediction
print("\nNext-word prediction test:")
print(f"Input: hello → Prediction: {predict_next('hello')}")
