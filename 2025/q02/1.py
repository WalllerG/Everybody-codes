with open("input.txt") as f:
    data = list(map(int, f.read().split('=')[1][1:-1].split(',')))
print(data)
R = [0,0]
for _ in range(3):
    x1, y1 = R[0], R[1]
    x2, y2 = R[0], R[1]
    new_x = (x1 * x2) - (y1 * y2)
    new_y = (x1 * y2) + (y1 * x2)
    R[0] = int(new_x / 10)
    R[1] = int(new_y / 10)
    R[0] += data[0]
    R[1] += data[1]
print(f"[{R[0]},{R[1]}]")