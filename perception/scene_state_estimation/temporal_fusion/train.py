import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from model.py import LSTMSceneEstimator

# Generate synthetic data for demonstration
def generate_data(num_samples, seq_length, input_size):
    X = torch.randn(num_samples, seq_length, input_size)
    y = torch.randn(num_samples, 1)
    return TensorDataset(X, y)

def train_model():
    input_size = 10
    hidden_size = 50
    output_size = 1
    num_layers = 2
    num_epochs = 10
    batch_size = 16

    model = LSTMSceneEstimator(input_size, hidden_size, output_size, num_layers)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    dataset = generate_data(1000, 20, input_size)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    for epoch in range(num_epochs):
        for X_batch, y_batch in dataloader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.4f}")

if __name__ == "__main__":
    train_model()
