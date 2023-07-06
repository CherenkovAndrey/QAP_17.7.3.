print("")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))

A = int(per_cent['ТКБ']*money/100)
B = int(per_cent['СКБ']*money/100)
C = int(per_cent['ВТБ']*money/100)
D = int(per_cent['СБЕР']*money/100)

print("")
deposit = [A, B, C, D]
print("Накопленные средства за год вклада в каждом из банков:", 'ТКБ:',A,'| СКБ:',B,'| ВТБ:',C,'| СБЕР:',D)

print("")
max_deposit = max(deposit)
bank_index = deposit.index(max_deposit)
max_bank = list(per_cent.keys())[bank_index]

print("Максимальная сумма, которую вы можете получить:", max_deposit, "в банке", max_bank)