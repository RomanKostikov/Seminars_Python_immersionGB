# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def calculate_profit(company_data):
    for company, data in company_data.items():
        income = sum(data[:3])
        expenses = sum(data[3:])
        profit = income - expenses
        print(f"{company}: {profit}")
    if all(sum(data[:3]) > sum(data[3:]) for data in company_data.values()):
        return True
    else:
        return False


company_data = {
    'Company A': [1000, -2000, -3000, 500, 600],
    'Company B': [5000, 4000, 3000, 2000, 1000],
    'Company C': [1000, 2000, 3000, 500, 600, 700, 800, 900, 1000]
}
result = calculate_profit(company_data)
print(result)
