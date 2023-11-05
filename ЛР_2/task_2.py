salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
koef_of_increase = 1
capital = 0
month = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(1, months + 1):
    month += 1
    if i > 1:
        koef_of_increase = (1 + increase) ** (i - 1)
    current_spend = spend * koef_of_increase
    capital += (current_spend - salary)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital, 2))
