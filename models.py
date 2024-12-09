import torch
import torch.nn as nn

class VADSR_CNN(nn.Module):
    def __init__(self, k):
        super(VADSR_CNN, self).__init__()
        self.conv1 = nn.Conv1d(1, 16, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv1d(16, 32, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.conv3 = nn.Conv1d(32, 64, kernel_size=3, stride=1, padding=1)
        self.relu3 = nn.ReLU() 
        self.conv4 = nn.Conv1d(64, 128, kernel_size=3, stride=1, padding=1)
        self.relu4 = nn.ReLU()
        self.conv5 = nn.Conv1d(128, 256, kernel_size=3, stride=1, padding=1)
        self.relu5 = nn.ReLU()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(256 * k, 512)
        self.relu6 = nn.ReLU()
        self.fc2 = nn.Linear(512, 1)

    def forward(self, x):
        x = x.unsqueeze(1)
        x = self.relu1(self.conv1(x))
        x = self.relu2(self.conv2(x))
        x = self.relu3(self.conv3(x))
        x = self.relu4(self.conv4(x))
        x = self.relu5(self.conv5(x))
        x = self.flatten(x)
        x = self.relu6(self.fc1(x))
        x = self.fc2(x)
        x = torch.sigmoid(x)
        return x.T

# TODO: Alternate MLP implementation
# class VADSR_MLP(nn.Module):
#     def __init__(self, k):
#         super(VADSR_MLP, self).__init__()
#         self.fc1 = nn.Linear(k, 256)
#         self.relu1 = nn.ReLU()
#         self.fc2 = nn.Linear(256, 512)
#         self.relu2 = nn.ReLU()
#         self.fc3 = nn.Linear(512, 1024)
#         self.relu3 = nn.ReLU()
#         self.fc4 = nn.Linear(1024, 512)
#         self.relu4 = nn.ReLU()
#         self.fc5 = nn.Linear(512, 1)
#         self.sigmoid = nn.Sigmoid()

#     def forward(self, x):
#         x = self.relu1(self.fc1(x))
#         x = self.relu2(self.fc2(x))
#         x = self.relu3(self.fc3(x))
#         x = self.relu4(self.fc4(x))
#         x = self.sigmoid(self.fc5(x))
#         return x.T

