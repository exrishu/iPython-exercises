from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
from nltk.util import ngrams
import random,nltk,re

wt = WhitespaceTokenizer()

file_name = input()


def read_script(name):
    with open(f'{name}', "r", encoding="utf-8") as f:
        lines = f.read().split()
    return lines


def token_stats(file_name):
    tokens = read_script(file_name)
    all_tokens = len(tokens)
    unique_tokens = len(set(tokens))
    return (f'''Corpus statistics
All tokens: {all_tokens} 
Unique tokens: {unique_tokens}''')


# print(token_stats(file_name))


def index_search_tokens(file_name):
    tokens = read_script(file_name)
    choice = input()
    if choice == 'exit':
        quit()
    else:
        try:
            index = tokens[int(choice)]
            print(index)
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except ValueError:
            print('Type Error. Please input an integer.')
    index_search_tokens(file_name)


# index_search_tokens(file_name)
def number_of_bigram(file_name):
    tokens = read_script(file_name)
    bigram = ngrams(tokens, 2)
    count = len(list(bigram))
    return count


# print(number_of_bigram(file_name))


def index_search_bigram(file_name):
    tokens = read_script(file_name)
    bigram = ngrams(tokens, 2)
    bigram_list = list(bigram)
    choice = input()
    if choice == 'exit':
        quit()
    else:
        try:
            index = bigram_list[int(choice)]
            print(f"Head: {index[0]}     Tail: {index[1]}")
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except ValueError:
            print('Type Error. Please input an integer.')

    index_search_bigram(file_name)


# index_search_bigram(file_name)

def markov_model(filename):
    tokens = read_script(filename)
    bigram = ngrams(tokens, 2)
    head_tail = {}
    for head, tail in bigram:
        head_tail.setdefault(head, []).append(tail)
    head = input()
    if head == 'exit':
        quit()
    else:
        try:
            tails = Counter(head_tail[head])
            print(f'Head: {head}')
            for tail, count in tails.items():
                print(f"Tail: {tail}    Count: {count}")
        except KeyError:
            print('The requested word is not in the model. Please input another word.')

    markov_model(filename)


# markov_model(file_name)
def sentence_generator(filename):
    tokens = read_script(filename)
    bigram = ngrams(tokens, 2)
    head_tail = {}
    for head, tail in bigram:
        head_tail.setdefault(head, []).append(tail)
    for i in range(1, 11):
        sen = []
        count = 1
        random_head = random.choice(tokens)
        sen.append(random_head)
        while count < 10:
            tails = Counter(head_tail[random_head])
            tail_list = list(tails.keys())
            tail_weight = list(tails.values())
            word = random.choices(tail_list, tail_weight)
            sen.append(word[0])
            random_head = word[0]
            count = count + 1
        for words in sen:
            print(words, end=" ")
        print("\n".strip())

# sentence_generator(file_name)
def generate_sentence_new(filename):
    tokens = read_script(filename)
    bigram = ngrams(tokens, 2)
    head_tail = {}
    for head, tail in bigram:
        head_tail.setdefault(head, []).append(tail)
    sen_count =10
    punc =['.','?','!']
    word_min =5
    for _ in range(sen_count):
        sen=[]
        while True:
            random_head = random.choice(tokens)
            if random_head[0].isupper() and random_head[-1] not in punc:
                break
        sen.append(random_head)
        while True:
            tails = Counter(head_tail[random_head])
            tail_list = list(tails.keys())
            tail_weight = list(tails.values())
            word = random.choices(tail_list, tail_weight)
            sen = sen + word
            if word[0][-1] in punc and len(sen) >= word_min:
                break
            random_head = word[0]
        print(" ".join(sen))

# generate_sentence_new(file_name)

def trigram_sen_generator(filename):
    tokens = read_script(filename)
    trigrams = list(nltk.trigrams(tokens))
    tokens_dict = {}

    for fist, second, tail in trigrams:
        tokens_dict.setdefault(f"{fist} {second}", []).append(tail)

    for token in tokens_dict:
        tokens_dict[token] = Counter(tokens_dict[token])

    for _ in range(0,10):
        while True:
            head = random.choice(list(tokens_dict.keys()))
            first = head.split()[0]
            if first.istitle() and not re.match(r'.+[!?,.]$', first):
                break
        sentence = head.split()
        while True:
            next_word = random.choices(list(tokens_dict[head].keys()),
                                       weights=list(tokens_dict[head].values()))[0]
            sentence.append(next_word)
            head = ' '.join(sentence[-2:])
            if len(sentence) >= 5 and re.match(r'.+[!?.]$', head):
                break
        print(*sentence, sep=' ', end='\n')

trigram_sen_generator(file_name)

