from nltk.tokenize import WhitespaceTokenizer

wt = WhitespaceTokenizer()


def read_script(name):
    with open(f'{name}.txt', "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines


def calculate_all_tokens(name):
    lines = read_script(name)
    count = 0
    for line in lines:
        tokens = wt.tokenize(line)
        cnt = len(tokens)
        count = cnt + count
    return count


def calculate_unique_token(name):
    lines = read_script(name)
    count = 0
    for line in lines:
        tokens = wt.tokenize(line)
        token_set = set(tokens)
        cnt = len(token_set)
        count = cnt + count
    return count
