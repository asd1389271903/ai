#由chatgpt輔助
import random

# 背包問題實例
class KnapsackProblem:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity

# 計算解的總價值
def total_value(solution, problem):
    total = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total += problem.values[i]
    return total

# 計算解的總重量
def total_weight(solution, problem):
    total = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total += problem.weights[i]
    return total

# 生成相鄰解
def neighbor(solution):
    index = random.randint(0, len(solution) - 1)
    new_solution = list(solution)
    new_solution[index] = 1 - new_solution[index]  # 將 0 變為 1 或將 1 變為 0
    return new_solution

# 爬山演算法
def hill_climbing(problem, iterations):
    current_solution = [random.choice([0, 1]) for _ in range(len(problem.weights))]
    current_value = total_value(current_solution, problem)
    current_weight = total_weight(current_solution, problem)

    for _ in range(iterations):
        new_solution = neighbor(current_solution)
        new_weight = total_weight(new_solution, problem)
        if new_weight <= problem.capacity:  # 檢查新解的總重量是否超過背包容量
            new_value = total_value(new_solution, problem)
            if new_value > current_value:
                current_solution = new_solution
                current_value = new_value
                current_weight = new_weight
        elif current_weight > problem.capacity:  # 如果總重量已經超過了背包容量，則將已選中的物品移除背包
            index = random.choice([i for i, x in enumerate(current_solution) if x == 1])
            current_solution[index] = 0
            current_weight = total_weight(current_solution, problem)
            current_value = total_value(current_solution, problem)  # 更新總價值

    return current_solution, current_value

# 主程序
def main():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    problem = KnapsackProblem(weights, values, capacity)

    iterations = 1000
    solution, value = hill_climbing(problem, iterations)

    print("最優解:", solution)
    print("最優解的總價值:", value)

if __name__ == "__main__":
    main()
