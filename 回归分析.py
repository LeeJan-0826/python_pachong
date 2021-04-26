# 用来求线性回归方程
import numpy as np
import matplotlib.pyplot as plt
def function_huigui(dim):
    print("输入x坐标：")
    list_a = []
    list_b = []
    for i in range(dim):
        x = input()
        list_a.append(int(x))
    print("输入x坐标：")
    for i in range(dim):
        y = input()
        list_b.append(int(y))
    total_a = 0.0
    a_2 = 0.0
    for ele in range(0, len(list_a)):
        total_a = total_a + list_a[ele]
        a_2 = a_2 + list_a[ele] * list_a[ele]
    total_b = 0.0
    a_b = 0.0
    for ele in range(0, len(list_b)):
        total_b = total_b + list_b[ele]
        a_b = a_b + list_a[ele] * list_b[ele]
    lxx = a_2 - float(total_a * total_a / dim)
    lxy = a_b - total_a*total_b / dim
    beta_1 = lxy/lxx
    beta_0 = total_b/dim - beta_1*total_a/dim
    print(beta_0, beta_1)
    plt.scatter(list_a,list_b)
    plt.plot( (min(list_a),min(list_a)*beta_1+beta_0),(max(list_a),max(list_a)*beta_1+beta_0))
    plt.plot()
    plt.show()
if __name__=="__main__":
    function_huigui(10)
# 斜率有点大