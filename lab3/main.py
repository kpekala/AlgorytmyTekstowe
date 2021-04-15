from heapq import *
from bitarray import bitarray

class Symbol:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq

class Node:
    def __init__(self, symbol: Symbol):
        self.symbol = symbol
        self.leftChild = None
        self.rightChild = None

    def __lt__(self, other):
        return self.symbol.freq < other.symbol.freq


class HuffmanTree:
    def __init__(self, text):
        self.root = self.huffman_coding(self.create_symbols(text))
        self.codes = {}
        self.create_codes()
        #testing below
        for key, value in self.codes.items():
            print(key,value)

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

    def codes_recur(self, itr: Node, code):
        value = itr.symbol.value
        if value is not None:
            self.codes[value] = code
        else:
            self.codes_recur(itr.leftChild, code + "0")
            self.codes_recur(itr.rightChild, code + "1")

    def create_codes(self):
        itr = self.root
        self.codes_recur(itr.leftChild, "0")
        self.codes_recur(itr.rightChild, "1")

    def get_code(self, symbol_value):
        return self.codes[symbol_value]



class Compressor:
    def __init__(self, text):
        self.tree = HuffmanTree(text)
        self.text = text
    def compress(self,):
        b = bitarray()
        for letter in self.text:
            code = self.tree.codes[letter]
            b += bitarray(code)
        return b

if __name__ == '__main__':
    cmpr = Compressor("asbcabscbab")
    print(cmpr.compress())
    #0100010000011000
    #



