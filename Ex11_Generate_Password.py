import secrets

def gen_pass(num_word, wordlist="Ex11_diceware.txt"):
    with open(wordlist, 'r') as file:
        lines = file.readlines()
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_word)]
    return ' '.join(words)

print(gen_pass(5))