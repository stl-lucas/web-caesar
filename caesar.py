from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    encrypted = ''
    for char in text:
        if char.lower() in alphabet:
            encrypted = encrypted + rotate_character(char, rot)
        else:
            encrypted = encrypted + char
    return encrypted

def main():
    print(rotate_string(input("Type a message: "), input("Rotate by: ")))

if __name__ == "__main__":
    main()
