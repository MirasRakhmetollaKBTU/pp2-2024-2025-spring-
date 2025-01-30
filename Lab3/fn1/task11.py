def is_palyndrom(sentence : str):
    r_sentence = sentence[::-1]
    if r_sentence == sentence:
        return f"'{sentence}' is polyndrom"
    else:
        return f"'{sentence}' is not polyndrom"

sent = input("Enter your sentence : ")
print(is_palyndrom(sent))
