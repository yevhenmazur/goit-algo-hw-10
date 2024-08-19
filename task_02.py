import matplotlib.pyplot as plt
import numpy as np
import scipy as spi
import random
import sympy as sp


def draw_graphic(f, a, b):
    # Створення діапазону значень для x
    x = np.linspace(a - 0.5, b + 0.5 , 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = np.exp(x**2) * np.sin(x**2) від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def resolve_with_quad(f, a, b):
    result, error = spi.integrate.quad(f, a, b)
    return result

def simpson_integral(f, a, b, num_points=1000):
    x = np.linspace(a, b, num_points)
    y = f(x)
    integral = spi.integrate.simpson(y, x=x)
    return integral

def symbolic_integral(f, a, b):
    x = sp.Symbol('x')
    expr = sp.exp(x**2) * sp.sin(x**2)
    # expr = f(x)
    integral = sp.integrate(expr, (x, a, b))
    return integral.evalf()

def is_inside(f, x, y):
    '''Перевіряє, чи знаходиться точка (x, y) під графіком f(x).'''
    return f(x) >= y

def find_maximum(f, a, b):
    '''Функція для знаходження максимуму'''
    # Оптимізуємо мінус функцію f(x) для знаходження максимуму
    result = spi.optimize.minimize_scalar(lambda x: -f(x), bounds=(a, b), method='bounded')
    
    max_x = result.x
    max_f = f(max_x)
    
    return max_f

def monte_carlo_simulation(f, a, b, num_experiments):
    '''Виконує серію експериментів методом Монте-Карло.'''
    average_area = 0
    y_max = find_maximum(f, a, b)

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(a, b), random.uniform(0, y_max)) for _ in range(15000)]
        # Відбір точок, що знаходяться під графіком функції
        inside_points = [point for point in points if is_inside(f, point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * ((b - a) * y_max)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area


# Визначення функції та межі інтегрування

def f(x):
    return np.exp(x**2) * np.sin(x**2)

### Розкоментуйте блок нижче, щоб перевірити що результати будуть подібними на функціях
### з інтегралом без комплексної складової
### -------
# def f(x):
#     return np.sin(x)

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість експериментів
num_experiments = 10

# Виконання симуляції
average_area = monte_carlo_simulation(f, a, b, num_experiments)
quad_area = resolve_with_quad(f, a, b)
simps_area = simpson_integral(f, a, b)
symb_resolv = symbolic_integral(f, a, b)

print(f"Інтеграл за допомогою quad: {quad_area}")
print(f"Інтеграл за методом Сімпсона: {simps_area}")
# print(f"Інтеграл, розрахований символьним методом: {symb_resolv}")
print(f"Середня площа фігури за {num_experiments} експериментів: {average_area}")

# draw_graphic(f, a, b) # Розкоментуйте щоб намалювати графік
