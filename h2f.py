import time
with open("kattis-hash.txt") as f:
    content = f.readlines()

with open("RT.txt") as f:                # hash
    contento = f.readlines()

with open("pwdRT.txt") as f:             # password
    ordd = f.readlines()

ordd = [x.strip() for x in ordd]
contento = [x.strip() for x in contento]
content = [x.strip() for x in content]

for i in range(len(ordd)):
    if contento[i] in content:
        time.sleep(0)
        f = open("pph.txt", "a")
        f.write("print(\"" + contento[i] + ":" + ordd[i] + "\")" + "\n")
        f.close()
