import struct
import time
from heapq import *
from bitarray import bitarray
import static
import os
import io

def file_text(file_path):
    return io.open(file_path,mode="r",encoding="utf-8").read()

def cmpr_ratio_test(file_path, method):
    print("testing cmpr ratio of",file_path)
    text = file_text(file_path)
    cmpr_text, tree = method(text)
    print("cmpr ratio: ", round((1 - ((len(cmpr_text)//8)/os.path.getsize(file_path))) * 100,2))

def cmpr_speed_test(file_path, method):
    text = file_text(file_path)
    start_time = time.time()
    method(text)
    print("testing compression speed of file",file_path)
    print("Seconds: ", round(time.time() - start_time,4))
    return round(time.time() - start_time, 4)

if __name__ == '__main__':
    cmpr_ratio_test("test",static.compress)
    cmpr_speed_test("test",static.compress)
    #files/chineesche_filosofie
    cmpr_ratio_test("files/chineesche_filosofie", static.compress)
    cmpr_speed_test("files/chineesche_filosofie", static.compress)



