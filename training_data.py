import torch
from tokenizer import encode, decode

token_ids = torch.tensor(encode("hello world"), dtype=torch.long)
context_length = 5
batch_size = 3
input_sequences = []
target_sequences = []

for start in range(batch_size):
    x = token_ids[start: start + context_length]
    y = token_ids[start + 1: start + context_length +1]
    
    input_sequences.append(x)
    target_sequences.append(y)

print("\nInput sequences:", input_sequences)
print("Target sequences:", target_sequences)
x_batch = torch.stack(input_sequences)
y_batch = torch.stack(target_sequences)

print("\nApply stack. Input shape ->", x_batch.shape)
print("Apply stack. Target shape ->", y_batch.shape)
print("\nInput:", x_batch)
print("Target:", y_batch)
