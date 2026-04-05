import re
with open("input.txt") as f:
    data = list(map(int, re.findall(r'-?\d+', f.read())))
A = data[0] + data[1] * 1j
print(A)
ans = 0
for i in range(101):
    for j in range(101):
        P = (A.real + i * 10) + (A.imag + j * 10) * 1j
        R = 0
        for _ in range(100):
            R *= R
            R = int(R.real / 100000) + int(R.imag / 100000) * 1j
            R += P
            if -1000000 <= R.real <= 1000000 and -1000000 <= R.imag <= 1000000:
                continue
            break
        else:
            ans += 1
print(ans)