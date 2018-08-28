import torch
import torch.nn as nn
import torchvision.models as models

class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        for param in resnet.parameters():
            param.requires_grad_(False)
        
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)
        self.embed = nn.Linear(resnet.fc.in_features, embed_size)

    def forward(self, images):
        features = self.resnet(images)
        features = features.view(features.size(0), -1)
        features = self.embed(features)
        return features
    
class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=1):
        super(DecoderRNN, self).__init__()

        self.embed = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers)
        self.fc = nn.Linear(hidden_size, vocab_size)

        # h, c
        self.hidden = (torch.zeros(1, 1, hidden_size), torch.zeros(1, 1, hidden_size))

        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        self.num_layers = num_layers
    
    def forward(self, features, captions):
        caption_embed = self.embed(captions[:, :-1])
        embeddings = torch.cat((features.unsqueeze(1), caption_embed), 1)
        lstm_out, self.hidden = self.lstm(embeddings)
        output = self.fc(lstm_out)

        return output

    def sample(self, inputs, states=None, max_len=20):
        " accepts pre-processed image tensor (inputs) and returns predicted sentence (list of tensor ids of length max_len) "
        result = []
        for iteration in range(max_len):
            lstm_out, states = self.lstm(inputs, states)
            print(lstm_out.squeeze(1)[0].shape)
            output = self.fc(lstm_out.squeeze(1)).max(1)[1]
            result.append(output.item())
            inputs = self.embed(output).unsqueeze(1)
        return result