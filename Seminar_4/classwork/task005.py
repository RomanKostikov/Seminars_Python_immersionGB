# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def calculate_prizes(names, bets, premia):
    prizes = {}
    for name, bet, prize in zip(names, bets, premia):
        prize_amount = bet * float(prize.strip('%')) / 100
        prizes[name] = prize_amount
    return prizes


names = ['Alice', 'Bob', 'Charlie']
bets = [10000, 20000, 30000]
premia = ['15.0%', '20.0%', '25.0%']
prizes = calculate_prizes(names, bets, premia)
print(prizes)
