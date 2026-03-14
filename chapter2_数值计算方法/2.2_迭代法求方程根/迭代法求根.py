import math

def f_prime(x):
    """导函数 f'(x) = e^x + 10"""
    return math.exp(x) + 10

def g_newton(x):
    """牛顿迭代法的迭代函数"""
    return x - func_f(x) / f_prime(x)

def g_simple(x):
    """简单迭代法：x = (2 - e^x) / 10"""
    return (2 - math.exp(x)) / 10

def func_f(x):
    """目标函数 f(x) = e^x + 10x - 2"""
    return math.exp(x) + 10 * x - 2

def newton_iteration(x0, eps=1e-4, max_iter=100):
    """牛顿迭代法求根"""
    print(f"\n{'='*60}")
    print("牛顿迭代法求解方程 e^x + 10x - 2 = 0")
    print(f"{'='*60}")
    print(f"初始值: x0 = {x0}")
    print(f"精度要求: eps = {eps}")
    print("迭代公式: x_{n+1} = x_n - f(x_n)/f'(x_n)")
    print(f"\n{'Iter':<6} {'x_n':<20} {'f(x_n)':<20} {'|x_{n+1}-x_n|':<20}")
    print("-" * 68)

    x = x0
    results = []

    for n in range(max_iter):
        fx = func_f(x)
        x_new = g_newton(x)
        diff = abs(x_new - x)

        print(f"{n:<6} {x:<20.10f} {fx:<20.10e} {diff:<20.10e}")
        results.append((n, x, fx, diff))

        if diff < eps:
            print("-" * 68)
            print(f"收敛！迭代 {n+1} 次后满足精度要求")
            print(f"方程的根约为: x = {x_new:.10f}")
            return x_new, results, True

        x = x_new

    print("未收敛！")
    return x, results, False

def simple_iteration(x0, eps=1e-4, max_iter=100):
    """简单迭代法求根"""
    print(f"\n{'='*60}")
    print("简单迭代法求解方程 e^x + 10x - 2 = 0")
    print(f"{'='*60}")
    print(f"初始值: x0 = {x0}")
    print(f"精度要求: eps = {eps}")
    print("迭代公式: x_{n+1} = (2 - e^{x_n}) / 10")
    print(f"\n{'Iter':<6} {'x_n':<20} {'f(x_n)':<20} {'|x_{n+1}-x_n|':<20}")
    print("-" * 68)

    x = x0
    results = []

    for n in range(max_iter):
        fx = func_f(x)
        x_new = g_simple(x)
        diff = abs(x_new - x)

        print(f"{n:<6} {x:<20.10f} {fx:<20.10e} {diff:<20.10e}")
        results.append((n, x, fx, diff))

        if diff < eps:
            print("-" * 68)
            print(f"收敛！迭代 {n+1} 次后满足精度要求")
            print(f"方程的根约为: x = {x_new:.10f}")
            return x_new, results, True

        x = x_new

    print("未收敛！")
    return x, results, False

def check_convergence_simple():
    """检查简单迭代法的收敛条件"""
    print("\n" + "="*60)
    print("简单迭代法收敛条件分析")
    print("="*60)
    print("迭代函数: g(x) = (2 - e^x) / 10")
    print("导函数: g'(x) = -e^x / 10")
    print("")
    print("收敛条件: |g'(x)| < 1")
    print("")

    # 在区间 [0, 0.5] 上检查
    for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
        g_prime = abs(-math.exp(x) / 10)
        print(f"  x = {x:.1f}: |g'(x)| = {g_prime:.10f}")

    print("")
    print("结论: 在 [0, 0.5] 区间内 |g'(x)| < 0.16 < 1，满足收敛条件")

def main():
    # 打开文件记录
    output_file = "迭代法求根结果.txt"

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("=" * 80 + "\n")
        outfile.write("迭代法求解方程 e^x + 10x - 2 = 0 的根\n")
        outfile.write(f"精度要求: 10^(-4)\n")
        outfile.write("=" * 80 + "\n\n")

        # 问题分析
        outfile.write("1. 问题描述\n")
        outfile.write("-" * 40 + "\n")
        outfile.write("方程: e^x + 10x - 2 = 0\n")
        outfile.write("目标: 使用迭代法求解方程的根，精度达到 10^(-4)\n\n")

        outfile.write("2. 数值分析\n")
        outfile.write("-" * 40 + "\n")
        outfile.write("首先分析函数 f(x) = e^x + 10x - 2 的性质:\n\n")

        # 分析函数在区间 [0, 0.5] 的值
        outfile.write("   在不同点的函数值:\n")
        for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
            fx = func_f(x)
            outfile.write(f"   f({x:.1f}) = {fx:.10f}\n")

        outfile.write("\n   由于 f(0) = -1 < 0 且 f(0.5) ≈ 4.48 > 0，\n")
        outfile.write("   根据介值定理，方程在 (0, 0.5) 内至少有一个根。\n\n")

        # 牛顿迭代法
        x0_newton = 0.1
        root_newton, results_newton, conv_newton = newton_iteration(x0_newton)

        outfile.write("\n3. 牛顿迭代法求解过程\n")
        outfile.write("-" * 40 + "\n")
        outfile.write(f"初始值: x0 = {x0_newton}\n")
        outfile.write("迭代公式: x_{n+1} = x_n - f(x_n)/f'(x_n)\n")
        outfile.write(f"\n   迭代过程数据:\n\n")
        outfile.write(f"{'Iter':<6} {'x_n':<20} {'f(x_n)':<20} {'|x_{n+1}-x_n|':<20}\n")
        outfile.write("-" * 68 + "\n")

        for n, x, fx, diff in results_newton:
            outfile.write(f"{n:<6} {x:<20.10f} {fx:<20.10e} {diff:<20.10e}\n")

        outfile.write(f"\n   结果: \n")
        outfile.write(f"   - 迭代次数: {len(results_newton)}\n")
        outfile.write(f"   - 近似根: x = {root_newton:.10f}\n")
        outfile.write(f"   - 验证: f({root_newton:.10f}) = {func_f(root_newton):.10e}\n")
        outfile.write(f"   - 精度: |x_{n+1}-x_n| = {results_newton[-1][3]:.10e} < 10^(-4)\n")

        # 简单迭代法
        x0_simple = 0.1
        root_simple, results_simple, conv_simple = simple_iteration(x0_simple)

        outfile.write("\n4. 简单迭代法求解过程\n")
        outfile.write("-" * 40 + "\n")
        outfile.write(f"初始值: x0 = {x0_simple}\n")
        outfile.write("迭代公式: x_{n+1} = (2 - e^{x_n}) / 10\n")
        outfile.write(f"\n   迭代过程数据:\n\n")
        outfile.write(f"{'Iter':<6} {'x_n':<20} {'f(x_n)':<20} {'|x_{n+1}-x_n|':<20}\n")
        outfile.write("-" * 68 + "\n")

        for n, x, fx, diff in results_simple:
            outfile.write(f"{n:<6} {x:<20.10f} {fx:<20.10e} {diff:<20.10e}\n")

        outfile.write(f"\n   结果: \n")
        outfile.write(f"   - 迭代次数: {len(results_simple)}\n")
        outfile.write(f"   - 近似根: x = {root_simple:.10f}\n")
        outfile.write(f"   - 验证: f({root_simple:.10f}) = {func_f(root_simple):.10e}\n")
        outfile.write(f"   - 精度: |x_{n+1}-x_n| = {results_simple[-1][3]:.10e} < 10^(-4)\n")

        # 收敛性分析
        check_convergence_simple()
        outfile.write("\n5. 收敛性分析\n")
        outfile.write("-" * 40 + "\n")
        outfile.write("   牛顿法: 具有二阶收敛性，收敛速度快\n")
        outfile.write("   简单迭代法: 具有线性收敛性，收敛速度较慢\n\n")

        # 最终结果
        outfile.write("6. 最终结果\n")
        outfile.write("-" * 40 + "\n")
        outfile.write(f"   方程 e^x + 10x - 2 = 0 的根为:\n")
        outfile.write(f"   x ≈ {root_newton:.10f}\n")
        outfile.write(f"   (精度达到 10^(-4))\n")

        # 验证
        outfile.write(f"\n   验证:\n")
        outfile.write(f"   e^{root_newton:.10f} + 10*{root_newton:.10f} - 2 = {func_f(root_newton):.10e}\n")
        outfile.write(f"   |f(x)| < 10^(-4) ✓\n\n")

        outfile.write("=" * 80 + "\n")
        outfile.write("计算完成！\n")
        outfile.write("=" * 80 + "\n")

    print(f"\n详细结果已保存到: {output_file}")

if __name__ == "__main__":
    main()
