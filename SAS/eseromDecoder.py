# definitely not just a morse decoder (?)

ESEROM_CODE_DICT = {'.-': 'A', '-...': 'B', 
                        '-.-.': 'C', '-..': 'D', 
                        '.': 'E', '..-.': 'F', 
                        '--.': 'G', '....': 'H', 
                        '..': 'I', '.---': 'J', 
                        '-.-': 'K', '.-..': 'L', 
                        '--': 'M', '-.': 'N', 
                        '---': 'O', '.--.': 'P',
                        '--.-': 'Q', '.-.': 'R', 
                        '...': 'S', '-': 'T', 
                        '..-': 'U', '...-': 'V', 
                        '.--': 'W', '-..-': 'X', 
                        '-.--': 'Y', '--..': 'Z',
                        '.----': '1', '..---': '2', 
                        '...--': '3', '....-': '4', 
                        '.....': '5', '-....': '6', 
                        '--...': '7', '---..': '8', 
                        '----.': '9', '-----': '0'}

def eserom(s):
    # get and format input string
    x = [elt.split(' ') for elt in s.split('  ')]
    res = ''

    # for every word
    for word in x:
        # for every letter in the word
        for id, letter in enumerate(word):
            # convert to morse
            letter = ''.join(['.' if elt == '1' else '-' for elt in letter])
            # add corresponding english letter to result
            res += ESEROM_CODE_DICT[letter]
        # add space between words
        res += ' '

    return res


print(eserom("1111 1 1011 1011 000  100 000 101 1011 011"))