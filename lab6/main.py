from queue import Queue
from time import perf_counter

class Node:
    def __init__(self):
        self.state: int = 0
        self.fail = None
        self.transitions = {}

class StateMachine:
    def __init__(self, pattern) -> None:
        self.final_states= []
        self.final_states_automaton = {}
        self.root: Node = Node()
        self.itr_state: Node = self.root
        self.pattern = pattern

        self.root.state = 0
        counter = 0

        alphabet = set()

        for i in range(len(pattern[0])):
            temp = self.root
            for j in range(len(pattern)):
                if pattern[j][i] not in temp.transitions:
                    alphabet.add(pattern[j][i])
                    temp.transitions[pattern[j][i]] = Node()
                    temp.transitions[pattern[j][i]].state = counter
                    counter += 1
                temp = temp.transitions[pattern[j][i]]

        q = Queue()

        for letter in alphabet:
            if letter in self.root.transitions:
                self.root.transitions[letter].fail = self.root
                q.put(self.root.transitions[letter])
            else:
                self.root.transitions[letter] = self.root

        while not q.empty():
            current_node = q.get()
            for letter in alphabet:
                if letter in current_node.transitions:
                    next_node = current_node.transitions[letter]
                    q.put(next_node)
                    temp = current_node.fail
                    while letter not in temp.transitions:
                        temp = temp.fail
                    next_node.fail = temp.transitions[letter]

        self.compute_final_states(pattern)
        self.compute_final_states_automaton()

    def read_char(self, letter):
        while letter not in self.current_state.transitions.keys():
            self.current_state = self.current_state.fail
            if self.current_state is None:
                self.current_state = self.root
                return self.current_state.state
        self.itr_state = self.current_state.transitions[letter]
        return self.current_state.state

    def rollback(self):
        self.itr_state = self.root

    def compute_final_states(self, pattern):
        for i in range(len(pattern[0])):
            self.final_states.append(0)
            for j in range(len(pattern)):
                self.final_states[-1] = self.read_char(pattern[j][i])
            self.rollback()

    def compute_final_states_automaton(self):
        for state in self.final_states:
            if state not in self.final_states_automaton.keys():
                self.final_states_automaton[state] = [0] * (len(self.final_states) + 1)
        long_ps = 0
        self.final_states_automaton[self.final_states[0]][0] = 1
        for i in range(len(self.final_states_automaton)):
            for state in self.final_states_automaton.values():
                state[i] = state[long_ps]
            if i < len(self.final_states):
                self.final_states_automaton[self.final_states[i]][i] = i + 1
                long_ps = self.final_states_automaton[self.final_states[i]][long_ps]

    def parse_line(self, line):
        result = []
        state = 0
        for i in range(len(line)):
            if line[i] not in self.final_states_automaton:
                state = 0
                continue
            state = self.final_states_automaton[line[i]][state]
            if state == len(self.final_states):
                result.append(i)
        return result

    def find(self, text):
        result = []
        length = 0
        automaton_output= []
        for word in text:
            length = max(length, len(word))
            automaton_output.append([])

        for i in range(length):
            for j in range(len(text)):
                if i < len(text[j]):
                    automaton_output[j].append(self.read_char(text[j][i]))
            self.rollback()

        for i in range(len(automaton_output)):
            temp: List[int] = self.parse_line(automaton_output[i])
            if len(temp) != 0:
                result.append((i, temp))
        return [(z[0] - len(self.pattern) + 1, y - len(self.pattern[0]) + 1) for z in result for y in z[1]]