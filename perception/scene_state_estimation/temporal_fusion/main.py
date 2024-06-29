import torch
from model import LSTMSceneEstimator

def main():
    input_size = 10
    hidden_size = 50
    output_size = 1
    num_layers = 2

    model = LSTMSceneEstimator(input_size, hidden_size, output_size, num_layers)
    model.load_state_dict(torch.load("model.pth"))

    # Generate a single sample for inference
    sample = torch.randn(1, 20, input_size)
    prediction = model(sample)
    print(f"Predicted scene state: {prediction.item():.4f}")

if __name__ == "__main__":
    main()
