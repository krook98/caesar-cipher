import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


print(art.logo)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    repeat = input("Would you like to restart the cipher program? Type 'Y' if yes or 'N' if no")
    if repeat in ["n", "N"]:
        should_end = True
        print("Goodbye")



