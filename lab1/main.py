from fsm import fsm, update_alphabet
from kmp import kmp
import time
import io


def naive(text, pattern):
    for s in range(0, len(text) - len(pattern) + 1):
        if pattern == text[s:(s + len(pattern))]:
            pass
            #print(f"Przesunięcie {s} jest poprawne")


def speed_test(method, text, pattern):
    start_time = time.time()
    method(text, pattern)
    return round(time.time() - start_time, 5)

def avg_speed_test(method, text, pattern, n=1):
    time_sum = sum([speed_test(method,text,pattern) for _ in range(n)])
    return round(time_sum / n,8)


def run_full_test(text, pattern):
    methods = [naive, fsm, kmp]
    for method in methods:
        avg_time = avg_speed_test(method,text,pattern)
        print('{name} algorithm takes {avg_time} seconds to run'.format(name = method.__name__, avg_time = avg_time))

def read_alphabet(text):
    result = []
    for c in text:
        if c not in result:
            result.append(c)
    return result


def file_text(text_name):
    return io.open(text_name, mode="r", encoding="utf-8").read()

def run_article_test():
    text = file_text("ustawa.txt")
    alphabet = read_alphabet(text)
    update_alphabet(alphabet)
    run_full_test(text, "art")



if __name__ == '__main__':
    #run_full_test("abcbacbacbabcbacbbabcbbabcbcb","bcb")
    #run_full_test(file_text("ustawa.txt"), "art")
    run_article_test()
