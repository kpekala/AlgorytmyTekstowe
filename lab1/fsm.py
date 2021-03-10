import re, copy

alphabet = []

def update_alphabet(al):
    alphabet.clear()
    alphabet.extend(al)

def transition_table(pattern, alphabet):
    result = []
    for q in range(0, len(pattern) + 1):
        result.append({})
        for a in alphabet:
            k = min(len(pattern), q + 1)
            while True:
                if re.search(f"{pattern[:k]}$", pattern[:q] + a):
                    break
                k -= 1
            result[q][a] = k
    return result



def fsm(text, pattern):
    tr_table = transition_table(pattern, alphabet)
    q = 0
    for s in range(0, len(text)):
        q = tr_table[q][text[s]]
        if q == len(tr_table) - 1:
            pass
            #print(f"Przesunięcie {s + 1 - q} jest poprawne")