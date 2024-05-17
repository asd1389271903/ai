#由chatgpt輔助
import numpy as np
from engine import Value

def norm(gp):
    return np.linalg.norm([g for g in gp])

def gradientDescendent(f, p0, h=0.01, max_loops=100000, dump_period=1000):
    p = [Value(val) for val in p0]
    for i in range(max_loops):
        fp = f(p).data#計算函數值
        for val in p:#重製梯度
            val.grad = 0
        f(p).backward()# 計算梯度
        gp = [val.grad for val in p]
        glen = norm(gp)
        
        #if i % dump_period == 0:
            #print('{:05d}: f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(
                #i, fp, str([val.data for val in p]), str(gp), glen))
        
        if glen < 0.00001:  # 如果步伐已经很小了，就停止
            break
        
        #逆梯度方向的一小步
        for val, grad in zip(p, gp):
            val.data += -h * grad
    
    print('{:05d}: f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(
        i, fp, str([val.data for val in p]), str(gp), glen))
    return [val.data for val in p]  # 傳回最低點！

def f(values):
    x, y = values
    return x**2 + y**2

p0 = [1.0, 2.0]

print("最低點：", gradientDescendent(f, p0))
