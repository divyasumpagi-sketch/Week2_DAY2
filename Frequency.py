# Count word frequency

text = input("Enter a sentence: ")

# Convert sentence into words
words = text.split()

# Create empty dictionary
word_count = {}

# Count frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display result
print("\nWord Frequency:")
for key, value in word_count.items():
    print(key, ":", value)
