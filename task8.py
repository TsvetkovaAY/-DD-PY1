money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
i = 1
while money_capital >= spend:
    spend_new = (increase * i + 1) * spend
    money_capital = money_capital - spend_new + salary
    month += 1
    i += 1
print(month)
