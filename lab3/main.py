from heapq import *
from bitarray import bitarray

class Symbol:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq


class HuffmanTree:
    def __init__(self, text):
        self.root = self.huffman_coding(self.create_symbols(text))

    def huffman_coding(self, symbols):
        queue = []
        for symbol in symbols:
            heappush(queue, Node(symbol))

        while len(queue) >= 2:
            node1 = heappop(queue)
            node2 = heappop(queue)
            new_node = Node(Symbol(None, node1.symbol.freq + node2.symbol.freq))
            new_node.leftChild = node1
            new_node.rightChild = node2
            heappush(queue, new_node)
        return heappop(queue)

    def create_symbols(self, text):
        symbols_map = {}
        for t in text:
            if t not in symbols_map:
                symbols_map[t] = 0
            symbols_map[t] += 1
        symbols = [Symbol(a, weight) for a, weight in symbols_map.items()]
        return symbols

class Node:
    def __init__(self, symbol: Symbol):
        self.symbol = symbol
        self.leftChild = None
        self.rightChild = None

    def __lt__(self, other):
        return self.symbol.freq < other.symbol.freq

class Compressor:
    def __init__(self, text):
        self.tree = HuffmanTree(text)
    def compress(self):
        b = bitarray()


if __name__ == '__main__':
    tree = HuffmanTree("")



