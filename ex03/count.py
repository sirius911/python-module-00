def count_upper(string):
    total = 0
    for c in string:
        if c.isupper():
            total += 1
    return total

def count_lower(string):
    total = 0
    for c in string:
        if c.islower():
            total += 1
    return total

def count_space(string):
    total = 0
    for c in string:
        if c == ' ':
            total += 1
    return total

def count_punctuation(string):
    total = 0
    for c in string:
        if c in ".,?!;:()[]'\"-":
            total += 1
    return total

def text_analyzer(*argv):
    """
    This function analyzes a string passed as a parameter. 
    Usage: text_analyzer(string)

    Description:
        The text analyzer() function displays the total character count,
        the number of lowercase letters, uppercase letters, spaces,
        and punctuation characters.

        NB. If more than one argument is given to the function,
            the function prints 'Error'.
            If no argument is given to the function,
            a prompt allows you to enter the character string

    Return:
        Nothing
    """
    if len(argv) > 1:
        print("Error")
        return
    if len(argv) == 0:
        string = ""
    else:
        string = str(argv[0])
    while len(string) == 0:
        string = input("What is the text to analyse?\n>> ")
    size = len(string)
    print ("The text contains", size, "characters:")
    print ("-",count_upper(string), "upper letters")
    print ("-", count_lower(string), "lower letters")
    print ("-", count_punctuation(string), "punctuation marks")
    print ("-", count_space(string), "spaces")