import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль!"
    return x / y

def power(x, y):
    return math.pow(x, y)

def main():
    print("--- Python Калькулятор v1.0 ---")
    history = []

    while True:
        print("\n--- Меню ---")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Степень (^)")
        print("6. История")
        print("0. Выход")

        choice = input("Ввод: ")

        if choice == '0':
            break
        
        if choice == '6':
            print("\n--- История ---")
            for h in history:
                print(h)
            continue

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Число 1: "))
                num2 = float(input("Число 2: "))
            except ValueError:
                print("Ошибка: нужны числа.")
                continue

            res = 0
            op = ""

            if choice == '1':
                res = add(num1, num2)
                op = "+"
            elif choice == '2':
                res = subtract(num1, num2)
                op = "-"
            elif choice == '3':
                res = multiply(num1, num2)
                op = "*"
            elif choice == '4':
                res = divide(num1, num2)
                op = "/"
            elif choice == '5':
                res = power(num1, num2)
                op = "^"

            out = f"{num1} {op} {num2} = {res}"
            print(">>>", out)
            history.append(out)
        else:
            print("Нет такой команды.")

if __name__ == "__main__":
    main()