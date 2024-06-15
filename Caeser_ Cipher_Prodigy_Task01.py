def caeser_cipher(text, shift, encrypt = True):
    newText = ''
    upalpha= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowalpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
    if not encrypt:
        shift *= -1
    else:
        for char in text:
            if not char.isalpha():
                newText += char
            elif char.isupper():
                val = upalpha.index(char)
                newVal = (val + shift) % 26
                newText += chr(newVal)
            elif char.lowalpha():
                val = lowalpha.index(char)
                newVal = (val + shift) % 26
                newText += chr(newVal)
    return newText

                





