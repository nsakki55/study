import torch.nn as nn
from sagan_self_attention import Self_Attention

class Generator(nn.Module):
    def __init__(self, z_dim=100, image_size=64):
        super(Generator, self).__init__()
        
        self.layer1 = nn.Sequential(
            nn.utils.spectral_norm(
                nn.ConvTranspose2d(z_dim, image_size*8, 
                                                   kernel_size=4, stride=1)),
            nn.BatchNorm2d(image_size*8),
            nn.ReLU(inplace=True))
        
        self.layer2 = nn.Sequential(
            nn.utils.spectral_norm(
                nn.ConvTranspose2d(image_size*8, image_size*4, 
                                                    kernel_size=4, stride=2, padding=1)),
            nn.BatchNorm2d(image_size*4),
            nn.ReLU(inplace=True))
        
        self.layer3 = nn.Sequential(
            nn.utils.spectral_norm(
                nn.ConvTranspose2d(image_size*4, image_size*2,
                                                      kernel_size=4, stride=2, padding=1)),
            nn.BatchNorm2d(image_size*2),
            nn.ReLU(inplace=True))

        # Self-Attentin層を追加
        self.self_attention1 = Self_Attention(in_dim=image_size*2)
        
        self.layer4 = nn.Sequential(
            nn.utils.spectral_norm(
                nn.ConvTranspose2d(image_size*2, image_size,
                                                      kernel_size=4, stride=2, padding=1)),
            nn.BatchNorm2d(image_size),
            nn.ReLU(inplace=True))
        
        # Self-Attentin層を追加
        self.self_attention2 = Self_Attention(in_dim=image_size)
        
        # 注意：白黒画像なので出力チャネルは1つだけ
        self.last = nn.Sequential(
            nn.ConvTranspose2d(image_size, 3, kernel_size=4, 
                                                  stride=2, padding=1),
            nn.Tanh())
        
    def forward(self, z):
        out = self.layer1(z)
        out = self.layer2(out)
        out = self.layer3(out)
        out, attention_map1 = self.self_attention1(out)
        out = self.layer4(out)
        out, attention_map2 = self.self_attention2(out)
        out = self.last(out)
        
        return out, attention_map1, attention_map2