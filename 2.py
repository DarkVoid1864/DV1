salary, monthly_payment, debt = input('Напишите зарплату, месячный платёж кредита'
                                      'и размер страховки через пробел - ').split()
print(f'После всех оплат у пользователя осталось - {int(salary) - int(monthly_payment) - int(debt)}.')



