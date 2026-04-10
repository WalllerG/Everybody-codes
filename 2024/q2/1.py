with open('input.txt')as f:
    words, sentence = f.read().split('\n\n')

words = words.split(':')[1].split(',')
sentence = sentence.split(' ')
ans = 0

for s in sentence:
    for w in words:
        if w in s:
            ans += 1
print(ans)