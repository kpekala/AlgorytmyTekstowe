from collections import defaultdict

from bitarray._bitarray import bitarray


class Node:
    def __init__(self, letter, parent=None, weight=0):
        self.letter = letter
        self.parent = parent
        self.weight = weight
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self, text):
        self.root = None
        self.nodes = {}
        self.huffman_coding(text)
        self.codes = {}
        self.create_codes()

    def huffman_coding(self, text):
        self.root = Node("#", weight=0)
        self.nodes = {"#": self.root}
        for letter in text:
            if letter in self.nodes:
                letter_node = self.nodes[letter]
                self.prepare(letter_node)
                self.increment(letter_node)
            else:
                updated_node = self.nodes["#"]
                updated_node.letter = None
                node = Node(letter, parent=updated_node)
                self.nodes[letter] = node
                self.nodes.pop("#")
                zero_node = Node("#", parent=updated_node, weight=0)
                updated_node.left = zero_node
                updated_node.right = node
                self.nodes["#"] = zero_node
                self.prepare(node)
                self.increment(node)

    def next(self, weight, old_node):
        itr = self.root
        queue = [itr.left, itr.right]

        while len(queue) > 0:
            node = queue.pop(0)
            if node.weight == weight and node.letter != "#" and node is not old_node and old_node.parent != node:
                return node
            if node.letter is None and node.weight > old_node.weight:
                queue.extend([node.left, node.right])
        return None

    def prepare(self, node):
        itr = node
        while itr is not self.root:
            swap_node = self.next(itr.weight, itr)
            while swap_node is None and itr is not self.root:
                itr = itr.parent
                swap_node = self.next(itr.weight, itr)
            if itr is self.root:
                return
            if swap_node is not None:
                self.swap(itr, swap_node)
            itr = itr.parent

    def print_tree(self):
        queue = [self.root]
        print("printing tree")
        i = 0
        while len(queue) > 0:
            node = queue.pop(0)
            print(i,node.letter)
            i+= 1
            if node.letter is None:
                queue.extend([node.left, node.right])

    @staticmethod
    def swap(node1, node2):
        node1.parent, node2.parent = node2.parent, node1.parent
        if node1.parent.left == node2:
            node1.parent.left = node1
        else:
            node1.parent.right = node1

        if node2.parent.left == node1:
            node2.parent.left = node2
        else:
            node2.parent.right = node2

    def increment(self, node):
        itr = node
        while itr is not None:
            itr.weight += 1
            itr = itr.parent

    def codes_recur(self, itr: Node, code):
        ##print(code, itr.letter)
        if itr.letter is not None:
            self.codes[itr.letter] = code
        else:
            self.codes_recur(itr.left, code + "0")
            self.codes_recur(itr.right, code + "1")

    def create_codes(self):
        itr = self.root
        self.codes_recur(itr.left, "0")
        self.codes_recur(itr.right, "1")


def compress(text):
    tree = HuffmanTree(text)
    b = bitarray()
    for letter in text:
        code = tree.codes[letter]
        b += bitarray(code)
    return b, tree


def decompress(cmpr_text: bitarray, tree: HuffmanTree):
    cmpr_text = cmpr_text.to01()
    root = tree.root
    itr: Node = root
    text = ""
    for bit in cmpr_text:
        itr = itr.left if bit == '0' else itr.right
        if itr.letter is not None:
            text += itr.letter
            itr = root
    return text

