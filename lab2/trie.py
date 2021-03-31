class TrieNode:
    def __init__(self, letter, parent):
        self.children = []
        self.letter = letter
        self.parent = parent
        self.length = parent.length + 1 if parent is not None else 0

    def find_head(self, text):
        if len(text) == 0:
            return None
        for child in self.children:
            if child.letter == text[0]:
                return child.find_head(text[1:])
        return self, text

    def add_path(self, text):
        par_itr = self
        for i in range(len(text)):
            new_node = TrieNode(text[i], par_itr)
            par_itr.children.append(new_node)
            par_itr = new_node

def build_suffix_trie(text):
    root = TrieNode("",None)
    for i in range(len(text)):
        suffix = text[i:]
        head, delta_text = root.find_head(suffix)
        head.add_path(delta_text)
    return root


def print_suffixes(itr: TrieNode, txt_acc):
    if itr is None:
        return
    for child in itr.children:
        if len(child.children) == 0:
            print("sufix: ", txt_acc + itr.letter + child.letter)
        else:
            print_suffixes(child, txt_acc + itr.letter)
