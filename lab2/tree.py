class Edge:
    def __init__(self, s_i: int, e_i: int, to):
        self.start_index = s_i
        self.end_index = e_i
        self.to = to
    def __len__(self):
        return (self.end_index+1) - self.start_index

class TreeNode:
    def __init__(self, parent):
        self.parent = parent
        self.edges = []


class Tree:
    def __init__(self, text):
        self.root = TreeNode(None)
        self.text = text
        self.n = len(self.text)
        self.build_suffix_tree()

    def build_suffix_tree(self):
        for s_i in range(self.n):
            self.add_suffix(s_i, self.root)

    def add_suffix(self, s_i, itr):
        if itr is None:
            return
        i = s_i
        for edge in itr.edges:
            if self.text[edge.start_index] == self.text[i]:
                edge_i = edge.start_index
                #case when edge equals part of new suffix:
                if self.n - i >= len(edge) and self.text[i:(i+len(edge))] == self.text[edge_i:(edge_i+len(edge))]:
                    i+= len(edge)
                    self.add_suffix(i,edge.to)
                    return
                # case when size of remaing suffix is less than size of existing edge
                while self.text[edge_i] == self.text[i]:
                    edge_i += 1
                    i += 1
                    if i >= self.n:
                        return
                tmp_to = edge.to
                new_node = TreeNode(itr)
                edge.to = new_node
                new_old_edge = Edge(edge_i,edge.end_index,tmp_to)
                edge.end_index = edge_i - 1
                new_edge = Edge(i,len(self.text)-1,None)
                new_node.edges.extend([new_edge, new_old_edge])
                return

        new_edge = Edge(i, len(self.text) - 1, None)
        itr.edges.append(new_edge)

    def print_suffixes(self, itr, txt_acc):
        for edge in itr.edges:
            edge_text = self.text[edge.start_index:(edge.start_index+len(edge))]
            if edge.to is None:
                print("suffix: ",txt_acc + edge_text)
            else:
                self.print_suffixes(edge.to,txt_acc + edge_text)







