from collections import Counter, defaultdict
with open('input.txt')as f:
    words, sentence = f.read().split('\n\n')

words = words.split(':')[1].split(',')
ans = 0

for sen in sentence.splitlines():
    sen = sen.split(' ')
    for i, s in enumerate(sen):
        counts = [[char, 0] for char in s]
        for w in words:
            if w in s:
                for j in range(len(s)-len(w)+1):
                    if s[j:j+len(w)] == w:
                        for k in range(j,j+len(w)):
                            counts[k][1] += 1
            if w in s[::-1]:
                for j in range(len(s)-len(w)+1):
                    if s[::-1][j:j+len(w)] == w:
                        for k in range(j,j+len(w)):
                            counts[::-1][k][1] += 1
        print(counts)
        ans += sum(1 for count in counts if count[1] > 0)

print(ans)