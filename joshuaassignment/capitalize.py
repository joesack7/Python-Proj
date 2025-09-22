def capitalize_words(sentence):
    word = sentence.split()
    result = []
    for actual_word in word:
        result.append(actual_word.capitalize())
    return " ".join(result)

answer:str = input("What sentence do you want to try this code on?")
print(capitalize_words(answer))

