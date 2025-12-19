import random

text = "I love AI I love Python AI loves Python"
words = text.split()

markov_chain = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in markov_chain:
        markov_chain[current_word] = []

    markov_chain[current_word].append(next_word)

current_word = random.choice(words)
generated_text = current_word

for i in range(10):
    if current_word in markov_chain:
        next_word = random.choice(markov_chain[current_word])
        generated_text += " " + next_word
        current_word = next_word
    else:
        break

print("Generated Text:")
print(generated_text)
