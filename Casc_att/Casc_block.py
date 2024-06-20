import torch
import torch.nn as nn
import math
import torch.nn.functional as F
from Attention.ca_attention import CoordAttention
from Attention.SCconv import SCONV


class CASC(nn.Module):
    def __init__(self, in_channel,out_channel):
        super(CASC, self).__init__()

        self.ch_cd = CoordAttention(in_channel,out_channel)
        self.sc = SCONV(in_channel)

    def forward(self, x):
        identity = x

        x1 = self.ch_cd(x)
        x = self.sc(x1)

        x += identity

        return x

if __name__ == '__main__':
    x = torch.randn(32, 64, 64, 64)
    model = CASC(32,32)
    print(model(x).shape)


