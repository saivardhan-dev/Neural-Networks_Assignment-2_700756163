number_of_words = 0
with open('input.txt', 'r') as file:
    content = file.read()
    print(content)

number_of_words = 0
word_count = {}

with open('input.txt', 'r') as file:
    content = file.read()
    words = content.split()

    for word in words:
        word = word.strip().lower()
        word_count[word] = word_count.get(word, 0) + 1
        number_of_words += 1

print(f"Total Number of Words: {number_of_words}")

for word, count in word_count.items():
    print(f'{word}: {count}')

with open('output.txt', 'w') as output_file:
    print(f"Total Number of Words: {number_of_words}", file=output_file)

    for word, count in word_count.items():
        print(f'{word}: {count}', file=output_file)