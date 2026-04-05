with open('input.txt') as f:
    left,right = f.read().split(':')
left = int(left)
right = list(map(int, right.split(',')))
identifier = []
for num in right:
    for segment in identifier:
        if num < segment[1] and segment[0] is None:
            segment[0] = num
            break
        if num > segment[1] and segment[2] is None:
            segment[2] = num
            break
    else:
        identifier.append([None,num,None])
ans = "".join(str(segment[1]) for segment in identifier)
print(ans)