#由chatgpt輔助
from pulp import LpMaximize, LpProblem, LpVariable, lpSum
import random

# 定義變量
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# 定義目標函數
objective = 3 * x + 2 * y

# 定義線性規劃問題
problem = LpProblem("Simple_LP_Problem", LpMaximize)
problem += (2 * x + y <= 20, "constraint_1")
problem += (-4 * x + 5 * y <= 10, "constraint_2")
problem += objective

# 使用 PuLP 解決線性規劃問題
problem.solve()

# 初始解
best_solution = (x.value(), y.value())
best_value = objective.value()

# 爬山演算法改進解
max_iterations = 1000
for _ in range(max_iterations):
    # 隨機生成鄰近解
    new_x = max(0, random.uniform(best_solution[0] - 1, best_solution[0] + 1))
    new_y = max(0, random.uniform(best_solution[1] - 1, best_solution[1] + 1))
    
    # 計算鄰近解的值
    new_value = 3 * new_x + 2 * new_y
    
    # 如果新解更好，更新最佳解
    if new_value > best_value and 2 * new_x + new_y <= 20 and -4 * new_x + 5 * new_y <= 10:
        best_solution = (new_x, new_y)
        best_value = new_value

print("最佳解:", best_solution)
print("最佳值:", best_value)
