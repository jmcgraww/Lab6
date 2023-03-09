# Made by John McGraw
def encode(password):
    encodedpassword = ''
    for element in password:
        element = int(element) + 3 % 10
        encodedpassword = encodedpassword + str(element)

    return encodedpassword

def decode(password):
    decodedpassword = ''
    for element in password:
        element = abs(int(element) - 3)
        decodedpassword = decodedpassword + str(element)
    return decodedpassword

def main():
    userOption = 0
    while not userOption == 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        userOption = int(input("Please enter an option: "))
        if userOption == 1:
            password = str(input("Please enter your password to encode: "))
            encodedpassword = encode(password)
            decodedpassword = decode(encodedpassword)
            print("Your password has been encoded and stored!\n")
        elif userOption == 2:
            if encodedpassword == '':
                print("No password stored.")
            else:
                print("The encoded password is " + encodedpassword + ", and the original password is " + decodedpassword + ".")
        elif userOption == 3:
            break


if __name__ == "__main__":
    main()
