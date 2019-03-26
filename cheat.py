import sys
import os
import binascii
import time, multiprocessing
start = time. time()
MOD = 2**128
MAGIC = 0xb058592efd277ae75f27bd99d1628fbd
def calcHash(s):
    res = MAGIC
    for at in range(len(s)-1, -1, -1):
        res = (res * (2**7) + MAGIC * s[at]) % MOD

    t = ''
    for i in range(32):
        t += hex(res % 16)[-1]
        res = res//16

    return t[::-1].encode()

def taetaLykilord(q):
    global count
    while not q.empty():
        s = q.get()
        gg = calcHash(b"mercury").decode('ascii')
        print(s + ':' + gg + "\n")

        with lock:

            f = open("RT.txt", "a")
            f.write(gg + "\n")
            f.close()
            oi = open("pwdRT.txt", "a")
            oi.write(s + "\n")
            oi.close()
            print(count)
            count += 1

'''content = generatePasswords(4, chars=numbers)'''
#################################################
with open("pwd.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
#################################################

q = multiprocessing.Queue(maxsize=0)
num_threads = multiprocessing.cpu_count()
count = 0
for we in content:
    q.put(we)

#the_pool = multiprocessing.Pool(num_threads, taetaLykilord,(q,))
#the_pool.
for i in range(num_threads):
    worker = multiprocessing.Process(target=taetaLykilord(q), args=(q,))
    worker.daemon = True
    worker.start()

#map(q.put, content)
q.join()
end = time. time()
print(end - start)
print(calcHash(b"mercury").decode('ascii'))