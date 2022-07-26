from copyreg import constructor


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cipher_text = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position+shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    plain_text = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position-shift
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

def caesar(text, shift, direction):
    output_text = ""
    if direction == "decode" :
        shift *= -1
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            new_letter = alphabet[new_position]
            output_text += new_letter
        else:
            output_text += i

    print(f"The decoded text is {output_text}")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26




    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

# if direction=="encode" :
#     encrypt(text, shift)
# elif direction=="decode" :
#     decrypt(text, shift)