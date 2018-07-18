import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I
import numpy as np


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # self.batchnorm = nn.BatchNorm2d(1)

        self.conv1 = nn.Conv2d(1, 32, 5)
        self.pool1= nn.MaxPool2d(2,2)

        self.conv2 = nn.Conv2d(32, 64, 3)
        self.pool2= nn.MaxPool2d(2,2)

        self.conv3 = nn.Conv2d(64, 128, 3)
        self.pool3 = nn.MaxPool2d(2,2)

        self.conv4 = nn.Conv2d(128, 256, 3)
        self.pool4 = nn.MaxPool2d(2,2)

        self.conv5 = nn.Conv2d(256, 512, 1)
        self.pool5 = nn.MaxPool2d(2,2)

        self.fc1= nn.Linear(6*6*512,2048)
        self.fc2= nn.Linear(2048, 136)
        
        self.dropout = nn.Dropout(p=0.5)

        I.xavier_normal_(self.conv1.weight)
        I.xavier_normal_(self.conv3.weight)
        I.xavier_normal_(self.fc1.weight)
        I.xavier_normal_(self.fc2.weight)

        
    def forward(self, x):
        ## Define the feedforward behavior of this model
        # x = self.batchnorm(x)
        x = self.pool1(F.selu(self.conv1(x)))
        x = self.pool2(F.selu(self.conv2(x)))
        x = self.pool3(F.selu(self.conv3(x)))
        x = self.pool4(F.selu(self.conv4(x)))
        x = self.pool5(F.selu(self.conv5(x)))
        
        x = x.view(x.size(0), -1)
        
        x = self.dropout(F.selu(self.fc1(x)))
        x = self.fc2(x)

        return x
    
# This network for some reason doesn't fit in the GPU, and takes FOREVER to train on a CPU!!!
# class Net(nn.Module):

#     def __init__(self):
#         # VGG-like architecture (mse=0.03@120epochs)
#         # K -> Number of filters
#         # F -> Spatial extend
#         # S -> Stride
#         # P -> Padding
#         super(Net, self).__init__()
        
#         # Methods to compute the dimensions
#         conv_dim = lambda W, H, D, K, F, S, P: ((W-F+2*P)//S+1, (H-F+2*P)//S+1, K)
#         pool_dim = lambda W, H, D, F, S: ((W-F)//S+1, (H-F)//S+1, D)
#         W, H, D = 224, 224, 1  # Inputs
#         Y = 136  # Outputs
        
#         ## LAYERS
#         self.batchnorm_1 = nn.BatchNorm2d(1)
        
#         # Group 1
#         K, F, S, P = 32, 3, 1, 0
#         self.conv1_1 = nn.Conv2d(D, K, F, S, P)
#         I.xavier_normal_(self.conv1_1.weight)
#         W, H, D = conv_dim(W, H, D, K, F, S, P)
#         self.activation_conv1_1 = nn.LeakyReLU()
        
#         self.conv1_2 = nn.Conv2d(D, K, F, S, P)
#         I.xavier_normal_(self.conv1_2.weight)
#         W, H, D = conv_dim(W, H, D, K, F, S, P)
#         self.activation_conv1_2 = nn.LeakyReLU()
        
#         self.conv1_3 = nn.Conv2d(D, K, F, S, P)
#         I.xavier_normal_(self.conv1_3.weight)
#         W, H, D = conv_dim(W, H, D, K, F, S, P)
#         self.activation_conv1_3 = nn.LeakyReLU()
                
#         F, S = 2, 2
#         self.pool1 = nn.MaxPool2d((F, F), (S, S))
#         W, H, D = pool_dim(W, H, D, F, S)
        
#         # Group 2
#         K, F, S, P = 96, 5, 1, 0
#         self.conv2_1 = nn.Conv2d(D, K, F, S, P)
#         I.xavier_normal_(self.conv2_1.weight)
#         W, H, D = conv_dim(W, H, D, K, F, S, P)
#         self.activation_conv2_1 = nn.LeakyReLU()
        
#         self.conv2_2 = nn.Conv2d(D, K, F, S, P)
#         I.xavier_normal_(self.conv2_2.weight)
#         W, H, D = conv_dim(W, H, D, K, F, S, P)
#         self.activation_conv2_2 = nn.LeakyReLU()
        
#         self.conv2_3 = nn.Conv2d(D, K, F, S, P)
#         I.xavier_normal_(self.conv2_3.weight)
#         W, H, D = conv_dim(W, H, D, K, F, S, P)
#         self.activation_conv2_3 = nn.LeakyReLU()
        
#         F, S = 2, 2
#         self.pool2 = nn.MaxPool2d((F, F), (S, S))
#         W, H, D = pool_dim(W, H, D, F, S)
        
#         # Dense Group
#         ins = W*H*D
#         outs = 512
#         self.fc1 = nn.Linear(ins, outs)
#         I.xavier_normal_(self.fc1.weight)
#         self.activation_fc1 = nn.LeakyReLU()
        
#         ins = outs
#         outs = 512
#         self.fc2 = nn.Linear(ins, outs)
#         I.xavier_normal_(self.fc2.weight)
#         self.activation_fc2 = nn.LeakyReLU()
#         self.dropout2 = nn.Dropout()
        
#         ins = outs
#         outs = Y
#         self.fc3 = nn.Linear(ins, outs)
#         I.xavier_normal_(self.fc3.weight)
        
#     def forward(self, x):
#         x = self.batchnorm_1(x)
        
#         x = self.conv1_1(x)
#         x = self.activation_conv1_1(x)
#         x = self.conv1_2(x)
#         x = self.activation_conv1_2(x)
#         x = self.conv1_3(x)
#         x = self.activation_conv1_3(x)
#         x = self.pool1(x)
        
#         x = self.conv2_1(x)
#         x = self.activation_conv2_1(x)
#         x = self.conv2_2(x)
#         x = self.activation_conv2_2(x)
#         x = self.conv2_3(x)
#         x = self.activation_conv2_3(x)
#         x = self.pool2(x)
        
#         x = x.view(x.size(0), -1)
        
#         x = self.fc1(x)
#         x = self.activation_fc1(x)
        
#         x = self.fc2(x)
#         x = self.activation_fc2(x)
#         x = self.dropout2(x)
        
#         x = self.fc3(x)

#         return x