class TrieNode:
    def __init__(self, val, parent):
        self.children = []
        self.val = val
        self.parent = parent
        self.length = parent.length + 1 if parent is not None else 0

    def find_head(self, text):
        if len(text) == 0:
            return None
        for child in self.children:
            if child.val == text[0]:
                return child.find_head(text[1:])
        return self, text

    def add_path(self, text):
        if len(text) == 0:
            return
        new_node = TrieNode(text[0],self)
        self.children.append(new_node)
        new_node.add_path(text[1:])

def build_suffix_trie(text):
    root = TrieNode("root",None)
    for i in range(len(text)):
        suffix = text[i:]
        head, delta_text = root.find_head(suffix)
        head.add_path(delta_text)
    return root



def get_texts():
    t = ["bbbd1","aabbabd2","ababcd3","abcbccd4"]
    file = open("article.txt")
    t.append(file.read()+"5")
    return t


if __name__ == '__main__':
    texts = get_texts()
    root = build_suffix_trie(texts[0])
    test_node,_ = root.find_head("bbc")
    print(test_node.length)
    test_node, _ = root.find_head("bbbde")
    print(test_node.length)

