import struct
import time
from heapq import *
from bitarray import bitarray
import static
import adaptive
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

def dcmpr_speed_test(file_path, method1, method2):
    text = file_text(file_path)
    cmpr_text, tree = method1(text)
    start_time = time.time()
    method2(cmpr_text, tree)
    print("testing decompression speed of file",file_path)
    print("Seconds: ", round(time.time() - start_time,4))
    return round(time.time() - start_time, 4)

def static_test():
    print("static test:")
    #time test
    cmpr_ratio_test("files/1k.txt", static.compress)
    cmpr_ratio_test("files/10k.txt", static.compress)
    cmpr_ratio_test("files/100k.txt", static.compress)
    cmpr_ratio_test("files/1m.txt", static.compress)
    #cmpr_speed_test("test", static.compress)
    # files/chineesche_filosofie
    #cmpr_ratio_test("files/chineesche_filosofie", static.compress)
    #cmpr_speed_test("files/chineesche_filosofie", static.compress)

def adaptive_test():
    print("adaptive test:")
    cmpr_ratio_test("files/1k.txt", adaptive.compress)
    cmpr_ratio_test("files/10k.txt", adaptive.compress)
    cmpr_ratio_test("files/100k.txt", adaptive.compress)
    cmpr_ratio_test("files/1m.txt", adaptive.compress)

def adaptive_test_dcmpr():
    print("adaptive test:")
    dcmpr_speed_test("files/1k.txt", adaptive.compress, adaptive.decompress)
    dcmpr_speed_test("files/10k.txt", adaptive.compress, adaptive.decompress)
    dcmpr_speed_test("files/100k.txt", adaptive.compress, adaptive.decompress)
    dcmpr_speed_test("files/1m.txt", adaptive.compress, adaptive.decompress)

def static_test_dcmpr():
    print("adaptive test:")
    dcmpr_speed_test("files/1k.txt", static.compress, static.decompress)
    dcmpr_speed_test("files/10k.txt", static.compress, static.decompress)
    dcmpr_speed_test("files/100k.txt", static.compress, static.decompress)
    dcmpr_speed_test("files/1m.txt", static.compress, static.decompress)


if __name__ == '__main__':
    #static_test()
    #adaptive_test()
    static_test_dcmpr()



