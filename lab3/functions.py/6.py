def reverse_sentence(input_string):
    words = input_string.split()

  
    reversed_words = words[::-1]


    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence


user_input = input("Enter a sentence: ")


reversed_sentence = reverse_sentence(user_input)


print("Reversed sentence:", reversed_sentence)
