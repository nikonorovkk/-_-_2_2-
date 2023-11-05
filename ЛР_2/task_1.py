money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

koef_of_increase = 1
number_of_month = 0
current_spend = spend

while money_capital > (current_spend - salary):
    number_of_month += 1
    if number_of_month > 1:
        koef_of_increase = (1 + increase) ** (number_of_month - 1)
    current_spend = spend * koef_of_increase
    money_capital -= (current_spend - salary)

print("Количество месяцев, которое можно протянуть без долгов:", number_of_month)
