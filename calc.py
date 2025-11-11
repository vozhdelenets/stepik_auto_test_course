while True:
    chislo1 = int(input("Введите первое число: "))
    chislo2 = int(input("Введите второе число: "))
    rez = input("Введите символ: ")
    if rez == "+":
        print("Результат операции = ", chislo1 + chislo2)
    if rez == "-":
        print("Результат операции = ", chislo1 - chislo2)
    if rez == "/":
        print("Результат операции = ", chislo1 / chislo2)
    if rez == "*":
        print("Результат операции = ", chislo1 * chislo2)

    if "y" == input("Завершить программу? (Y) "):
        break