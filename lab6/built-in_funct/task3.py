word   = input("Enter issue: ")
r_word = "".join(reversed(word))
print("word is polyndrom" if word == r_word else "word is not polyndrom")
