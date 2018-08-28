import os
import sys

import matplotlib.pyplot as plt
import numpy as np

import torch
import torch.nn as nn
from torchvision import transforms

COCOPATH = '/home/zafar/Desktop/Data/COCO' if os.environ['USER'] == 'zafar' else '/opt/cocoapi'
sys.path.append(os.path.join(COCOPATH, 'PythonAPI'))

from pycocotools.coco import COCO
from data_loader import get_loader
from model import EncoderCNN, DecoderRNN
import math


MODEL_PATH = "./models"
BEST_EPOCH=45
BEST_LOSS=0.0636
PRETRAINED_MODEL_PATH = os.path.join(MODEL_PATH, "{}-{{}}-{}.pkl".format(BEST_EPOCH, BEST_LOSS))

batch_size = 1             # batch size
vocab_threshold = 5        # minimum word count threshold
vocab_from_file = True     # if True, load existing vocab file
embed_size = 256           # dimensionality of image and word embeddings
hidden_size = 512          # number of features in hidden state of the RNN decoder
max_len = 20

transform_test = transforms.Compose([ 
    transforms.Resize(256),                          # smaller edge of image resized to 256
    # transforms.RandomRotation(15.0),                 # Rotate the image randomly
    transforms.RandomCrop(224),                      # get 224x224 crop from random location
    # transforms.RandomHorizontalFlip(),               # horizontally flip image with probability=0.5
    # transforms.ColorJitter(0.1, 0.1, 0.1),           # Jitter the color a little
    transforms.ToTensor(),                           # convert the PIL Image to a tensor
    transforms.Normalize((0.485, 0.456, 0.406),      # normalize image for pre-trained model
                         (0.229, 0.224, 0.225))])

# Build data loader.
data_loader = get_loader(transform=transform_test,
                         mode='test_small',
                         batch_size=batch_size,
                         vocab_threshold=vocab_threshold,
                         vocab_from_file=vocab_from_file,
                         cocoapi_loc=COCOPATH)

vocab = data_loader.dataset.vocab
# The size of the vocabulary.
vocab_size = len(vocab)

# Initialize the encoder and decoder. 
encoder = EncoderCNN(embed_size)
decoder = DecoderRNN(embed_size, hidden_size, vocab_size)

device = torch.device("cpu")
# encoder.to(device)
# decoder.to(device)

# Load the pretrained model
encoder.load_state_dict(torch.load(PRETRAINED_MODEL_PATH.format('encoder')))
decoder.load_state_dict(torch.load(PRETRAINED_MODEL_PATH.format('decoder')))

encoder.eval()
decoder.eval()

images, conv_images = next(iter(data_loader))
features = encoder(conv_images).unsqueeze(1)
output = decoder.sample(features, max_len=max_len)

word_list = []
for word_idx in output:
    if word_idx == vocab.word2idx[vocab.start_word]:
        continue
    if word_idx == vocab.word2idx[vocab.end_word]:
        break
    word_list.append(vocab.idx2word[word_idx])

print(' '.join(word_list))
plt.imshow(np.squeeze(images))
# plt.title(' '.join(word_list))
# plt.axis([])
plt.show()
