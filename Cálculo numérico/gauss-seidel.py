def gauss_seidel_equations(equations, x0, precisao=1e-4, max_iter=1000):
    n = len(equations)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            left_side, right_side = equations[i](x_new)
            x_new[i] = right_side / left_side

        # Verifica se a convergência foi atingida
        if max(abs(x_new[i] - x[i]) for i in range(n)) < precisao:
            return x_new, _

        x = x_new

    raise ValueError(
        "O método não convergiu após o número máximo de iterações")

# Definindo as equações diretamente


def equation1(x): return 3, 7.85 + 0.1 * x[1] + 0.2 * x[2]
def equation2(x): return 7, -19.3 - 0.1 * x[0] + 0.3 * x[2]
def equation3(x): return 10, 71.4 - 0.3 * x[0] + 0.2 * x[1]


equations = [equation1, equation2, equation3]
x0 = [0, 0, 0]  # Aproximação inicial

sol, iters = gauss_seidel_equations(equations, x0)
print(f'Equações seidel: solução encontrada: {sol} em {iters} iterações')
# 3 iterações