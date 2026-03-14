"""
二分法求解方程 x^4 - 3x + 1 = 0 在区间 [0.3, 0.4] 内的根
要求误差不超过 10^(-2)
"""

def func(x):
    """目标函数 f(x) = x^4 - 3x + 1"""
    return x**4 - 3*x + 1

def bisection(a, b, tol):
    """
    二分法求根
    参数:
        a: 区间左端点
        b: 区间右端点
        tol: 误差要求
    返回:
        根的近似值
    """
    if func(a) * func(b) >= 0:
        print(f"错误: f({a}) * f({b}) >= 0, 二分法不适用")
        return None

    iteration = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iteration += 1
        print(f"迭代 {iteration}: a={a:.6f}, b={b:.6f}, c={c:.6f}, 误差={(b-a)/2:.6f}")

    result = (a + b) / 2
    return result

def main():
    a, b = 0.3, 0.4
    tol = 1e-2

    print("方程: x^4 - 3x + 1 = 0")
    print(f"区间: [{a}, {b}]")
    print(f"误差要求: {tol}")
    print(f"f(0.3) = {func(0.3):.6f}")
    print(f"f(0.4) = {func(0.4):.6f}")
    print("-" * 50)
    print("二分法求根过程:")
    print("-" * 50)

    result = bisection(a, b, tol)

    if result is not None:
        print("-" * 50)
        print(f"结果: 根 ≈ {result:.6f}")
        print(f"f({result:.6f}) = {func(result):.6f}")
        print(f"最终误差: {(b-a)/2:.6f}")

        # 保存结果到文件
        with open("2.1_result.txt", "w", encoding="utf-8") as outfile:
            outfile.write("方程: x^4 - 3x + 1 = 0\n")
            outfile.write(f"区间: [{a}, {b}]\n")
            outfile.write(f"误差要求: {tol}\n")
            outfile.write(f"根的近似值: {result:.6f}\n")
            outfile.write(f"f({result:.6f}) = {func(result):.6f}\n")
        print("\n结果已保存到 2.1_result.txt")

if __name__ == "__main__":
    main()
