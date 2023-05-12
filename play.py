
import torch


x = torch.rand(4, 64, 256,2)
x2=x[:,:,:,0]
x3=x[:,:,:,1]
x4=torch.stack([x2,x3],dim=3)
x5=x4