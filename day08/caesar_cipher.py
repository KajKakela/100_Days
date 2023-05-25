import string

alphabets = list(string.ascii_lowercase)
scandic = ["å","ä","ö"]
alphabets.extend(scandic)
alphabets += alphabets

def main():
    choice = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()

    while choice != "encode" or choice != "decode":
        if choice == "encode" or choice == "decode":
            encode_decode(choice)
        else:
            choice = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
            


def encode_decode(process):
    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    single_letter = [letter for letter in message]

    new_message_list = []

    
    for letter in single_letter:
        if letter in alphabets:
            x = alphabets.index(letter)

            if process == "encode":
                new_message_list.append(alphabets[x+shift_number])
            else:
                new_message_list.append(alphabets[x-shift_number])

        elif letter == " ":
            new_message_list.append(" ")
        
        else:
            continue
    
    
    new_message = "".join(new_message_list)
    print(f"Here's the encoded result: {new_message}")

    choice = input("\nType 'yes' if you want to go again, otherwise type 'no':\n")

    if choice == "yes":
        main()
    else:
        exit()


main()