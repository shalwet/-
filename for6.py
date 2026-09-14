sumKgCandy = float(input("Введите стоимость киллограма конфет:"))

for i in range(12, 21, 2):
    print(f"{i/10} кг конфет будет стоить {i/10 * sumKgCandy} рублей")