#由chatgpt輔助
import random

citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

# 計算兩個城市之間的距離
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

# 計算路徑的總長度
def pathLength(p, citys):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i+1)%plen]])
    return dist

# 生成相鄰解
def neighbor(p):
    new_p = list(p)
    index1 = random.randint(0, len(p) - 1)
    index2 = random.randint(0, len(p) - 1)
    new_p[index1], new_p[index2] = new_p[index2], new_p[index1]
    return new_p

# 爬山演算法
def hill_climbing(citys, iterations):
    l = len(citys)
    path = [(i+1)%l for i in range(l)]
    current_length = pathLength(path, citys)

    for _ in range(iterations):
        new_path = neighbor(path)
        new_length = pathLength(new_path, citys)
        if new_length < current_length:
            path = new_path
            current_length = new_length

    return path, current_length

# 主程序
def main():
    iterations = 1000
    solution, length = hill_climbing(citys, iterations)

    print("最優路徑:", solution)
    print("最短路徑的總長度:", length)

if __name__ == "__main__":
    main()
