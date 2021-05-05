from random import random
from spacy.language import Language
from spacy.tokenizer import Tokenizer
from spacy.vocab import Vocab


def remove_random_tokens(tokens):
    res = []
    for t in tokens:
        if random() >= 0.03:
            res.append(t)
    return res

def lcs(s1, s2, return_array = 0):
    m = len(s1)
    n = len(s2)
    d = [[0 for i in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                d[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1])

    return d if return_array else d[m][n]

def diff(a, b):
    d = lcs(a,b,1)
    lines = []
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 and j >= 0:
        if a[i] == b[j]:
            i -= 1
            j -= 1
        elif d[i][j - 1] >= d[i - 1][j]:
            lines.append("> [{}] {}".format(j,b[j]))
            j -= 1
        elif d[i][j - 1] < d[i - 1][j]:
            lines.append("< [{}] {}".format(i,a[i]))
            i -= 1
    while j >= 0:
        lines.append("> [{}] {}".format(j, b[j]))
        j -= 1
    while i >= 0:
        lines.append("< [{}] {}".format(i, a[i]))
        i -= 1
    for line in reversed(lines):
        print(line)
    return d



with open('romeo-i-julia-700.txt', "r", encoding="utf8") as file:
    vb = Language(Vocab()).vocab
    tokenizer = Tokenizer(vb)
    tokens = tokenizer(file.read())
    a = remove_random_tokens(tokens)
    b = remove_random_tokens(tokens)
    with open('a.txt', 'w') as new_file:
        for token in a:
            new_file.write(token.text_with_ws)
    with open('b.txt', 'w') as new_file:
        for token in b:
            new_file.write(token.text_with_ws)
    with open('a.txt', 'r') as file1, open('b.txt', 'r') as file2:
        a = file1.readlines()
        b = file2.readlines()
        diff(a, b)

