import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Conv1d(1, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(128, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(64, 1, kernel_size=3, padding=1),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x)

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv1d(1, 64, kernel_size=3, padding=1),
            nn.ReLU(0.2, inplace=True),
            nn.Conv1d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(0.2, inplace=True),
            nn.Conv1d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(0.2, inplace=True),
        )
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(256 * 80, 1)  # mel 크기와 일치하게 설정

    def forward(self, x):
        x = self.conv(x)
        x = self.flatten(x)
        x = self.fc(x)
        return torch.sigmoid(x)
