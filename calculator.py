import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: на ноль делить нельзя"
    return x / y

def power(x, y):
    return math.pow(x, y)

def main():
    print("--- Калькулятор v0.5 (Math Module) ---")
    
    while True:
        print("\n1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '0':
            break
            
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Число 1: "))
                num2 = float(input("Число 2: "))
            except ValueError:
                print("Ошибка: вводите только цифры!")
                continue
            
            if choice == '1':
                print("Результат:", add(num1, num2))
            elif choice == '2':
                print("Результат:", subtract(num1, num2))
            elif choice == '3':
                print("Результат:", multiply(num1, num2))
            elif choice == '4':
                print("Результат:", divide(num1, num2))
            elif choice == '5':
                print("Результат:", power(num1, num2))
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()