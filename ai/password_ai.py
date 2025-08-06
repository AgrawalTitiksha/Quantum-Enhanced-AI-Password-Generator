import torch
import numpy as np

def generate_password(seed, length, charset):
    torch.manual_seed(seed)
    np.random.seed(seed)
    return ''.join(np.random.choice(charset, length))
