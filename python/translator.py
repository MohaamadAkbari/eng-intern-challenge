import sys

braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}  

braille_reverse_map = {} 
for k, v in braille_map.items():
    if v in braille_reverse_map.keys():
        braille_reverse_map[v].append(k)
    else:
        braille_reverse_map[v] = [k]

def is_braille(input_str):
    return all(c in 'O. ' for c in input_str)

def english_to_braille(input_str):
    result = []
    number_mode = False
    for char in input_str:
        if char.isdigit(): 
            if not number_mode:
                result.append(braille_map['num'])
                number_mode = True
            result.append(braille_map[char])
        if char.isalpha():
            if char.isupper():
                result.append(braille_map['cap'])
            result.append(braille_map[char.lower()])
            number_mode = False
        elif char == ' ':
            result.append(braille_map[' '])
            number_mode = False
    return ''.join(result)

def braille_to_english(input_str):
    result = []
    number_mode = False
    capitalize_next = False
    braille_chars = [input_str[i:i+6] for i in range(0, len(input_str), 6)]
    for braille_char in braille_chars:
        if braille_char == braille_map['cap']:
            capitalize_next = True
        elif braille_char == braille_map['num']:
            number_mode = True
        elif braille_char == braille_map[' ']:
            result.append(' ')
            number_mode = False
        else:
            if number_mode:
                result.append(braille_reverse_map[braille_char][1])
            else:
                char = braille_reverse_map[braille_char][0]
                if capitalize_next:
                    result.append(char.upper())
                    capitalize_next = False
                else:
                    result.append(char)
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Please provide input for translation.")
        return
    
    input_str = sys.argv[1]
    n = len(sys.argv)
    for i in range(2, n):
        input_str += ' ' + sys.argv[i]

    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == '__main__':
    main()