import sys

MORSE_CODE_DICT = { ' ':' / ', 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', }

def valid_arg(argv):
    for arg in argv:
        for letter in arg:
            if not letter.isalnum() and letter != ' ':
                print ("ERROR")
                sys.exit(2)

def main(argv):
    if len(argv) > 1:
        valid_arg(argv[1:])
        for arg in argv[1:]:
            for letter in arg:
                print(MORSE_CODE_DICT[letter.upper()], end=' ')
    print("")

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(1)