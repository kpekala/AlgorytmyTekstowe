import trie
import time
from tree import Tree

def get_texts():
    t = ["bbbd1","aabbabd2","ababcd3","abcbccd4"]
    file = open("article.txt")
    t.append(file.read()+"@")
    return t


def test_tree():
    ts = get_texts()
    for t in ts[:4]:
        tree = Tree(t)
        tree.print_suffixes(tree.root, "")
        print("")

def test_trie():
    ts = get_texts()
    for t in ts[:4]:
        root = trie.build_suffix_trie(t)
        trie.print_suffixes(root, "")
        print("")



def speed_test(method, text):
    start_time = time.time()
    method(text)
    return time.time() - start_time


def time_test_tree():
    ts = get_texts()
    for t in ts:
        start_time = time.time()
        tree = Tree(t)
        print(time.time() - start_time)

def time_test_trie():
    ts = get_texts()
    for t in ts:
        start_time = time.time()
        root = trie.build_suffix_trie(t)
        print(time.time() - start_time)

if __name__ == '__main__':
    test_trie()
    time_test_trie()

