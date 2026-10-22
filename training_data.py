import torch
from tokenizer import encode, decode

token_ids = torch.tensor(encode("hello world"), dtype=torch.long)
context_length = 4

x = token_ids[: context_length]
y = token_ids[1: context_length +1]

print("Input: ", x)
print("Target: ", y)
print("Input text: ", decode(x.tolist()))
print("Target text: ", decode(y.tolist()))
print("Shapes: ", x.shape, y.shape)