def alphabet_position(letter):
    letter = letter.lower()
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    counter = 0
    for i in alphabet:
        if i != letter:
            counter = counter + 1
        else:
            return counter
			
def rotate_character(char, rot):
    cap = False
    bb = char.upper()
    if char == bb:
        cap = True
    else:
        cap = False

    position = int(alphabet_position(char))
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    encrypted = ''
    rotated_index = position + int(rot)
    if rotated_index < 26:
        encrypted = alphabet[rotated_index]
    else:
        encrypted = alphabet[rotated_index % 26]
		
    if cap is True:
        result = encrypted.upper()
    else:
        result = encrypted.lower()
    return result