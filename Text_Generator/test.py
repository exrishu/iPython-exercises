import time
from itertools import chain
from nltk.tokenize import WhitespaceTokenizer

start_time = time.time()
with open('test.txt', "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"File Reading time{time.time() - start_time}")

temp_list = []

for line in lines:
    tokens = WhitespaceTokenizer().tokenize(line)
    print(tokens)
    test_list = list(chain(temp_list, tokens))
    temp_list = test_list

print(len(temp_list))

print(f"Adding list time{time.time() - start_time}")
