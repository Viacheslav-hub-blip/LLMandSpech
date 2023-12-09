import numpy as np
import pandas as pd

sentence = "Thomas Jefferson began building Monticello at the age of 26."
sentence.split()

token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))
print(', '.join(vocab))

num_tokens = len(token_sequence)
vocab_size = len(vocab)
onehot_vecrors = np.zeros((num_tokens, vocab_size), int)

print(onehot_vecrors)

for i, word in enumerate(token_sequence):
    onehot_vecrors[i, vocab.index(word)] = 1

print(' '.join(vocab))
print()

print(onehot_vecrors)


print(pd.DataFrame(onehot_vecrors, columns=vocab))