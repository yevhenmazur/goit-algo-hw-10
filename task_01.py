import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Quantity", pulp.LpMaximize)

# Визначення змінних
L = pulp.LpVariable('L', lowBound=0, cat='Integer')  # Кількість лимонаду
J = pulp.LpVariable('J', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Функція цілі (Максимізація кількості напоїв)
model += L + J

# Додавання обмежень
model += 2 * L + J <= 100
model += L <= 50
model += L <= 30
model += 2 * J <= 40

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонаду:", L.varValue)
print("Виробляти фруктового соку:", J.varValue)
