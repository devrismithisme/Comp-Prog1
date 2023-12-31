morse_codedict = {
    "A" or "a" : "._",
    "B" or "b" : "_...",
    "C" or "c" : "_._.",
    "D" or "d" : "_..",
    "E" or "e" : ".",
    "F" or "f" : ".._.",
    "G" or "g" : "_ _.",
    "H" or "h" : "....",
    "I" or "i" : "..",
    "J" or "j" : "._ _ _",
    "K" or "k" : "_._",
    "L" or "l" : "._..",
    "M" or "m" : "_ _",
    "N" or "n" : "_.",
    "O" or "o" : "_ _ _",
    "P" or "p" : "._ _.",
    "Q" or "q" : "_ _._",
    "R" or "r" : "._.",
    "S" or "s" : "...",
    "T" or "t" : "_",
    "U" or "u" : ".._",
    "V" or "v" : "..._",
    "W" or "w" : "._ _",
    "X" or "x" : "_.._",
    "Y" or "y" : "_._ _",
    "Z" or "z" : "_ _..",

    "Á" or "á" : "._ _._",
    "Ä" or "ä" : "._._",
    "É" or "é" : ".._..",
    "Ñ" or "ñ" : "_ _._ _",
    "Ö" or "ö" : "_ _ _.",
    "ü" or "Ü" : ".._ _",

    "1" : "._ _ _ _",
    "2" : ".._ _ _",
    "3" : "..._ _",
    "4" : "...._",
    "5" : ".....",
    "6" : "_....",
    "7" : "_ _...",
    "8" : "_ _ _..",
    "9" : "_ _ _ _.",
    "0" : "_ _ _ _ _",

    "," : "_ _.._ _",
    "." : "._._._",
    "?" : ".._ _..",
    '"' : "._.._.",
    ":" : "_ _ _...",
    "'" : "._ _ _ _.",
    "-" : "_...._",
    "/" : "_.._.",
    "(" : "_._ _.",
    ")" : "_._ _._",
}


message_to_code = input("Please give me a statement to translate into morse code.  ")

def to_morse_code(message):
    morse_code = ""
    for char in message:
        if char == " ":
            morse_code += "//"
        else:
            morse_code += morse_codedict[char.upper()] + "/"
    print(morse_code)

to_morse_code(message_to_code)