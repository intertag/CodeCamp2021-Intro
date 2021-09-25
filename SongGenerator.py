def print_spam_line():
    line = "spam spam spam spam"
    line_in_upper = make_uppercase(line)
    print(line_in_upper)


def print_spam_line_with_words(word_1, word_2):
    print(f"{word_1} SPAM, {word_2} SPAM")


def make_uppercase(some_string):
    string_in_upper = some_string.upper()
    return string_in_upper


print("Wir generieren einen Song!")

print_spam_line()
print_spam_line()
print_spam_line_with_words("marvelous", "great")
print_spam_line()
print_spam_line()
print_spam_line_with_words("glory", "holy")
