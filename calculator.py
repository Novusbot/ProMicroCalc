def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print("--- Калькулятор v0.2 ---")
    
    while True:
        print("\n1. Сложение")
        print("2. Вычитание")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '0':
            break
            
        if choice in ('1', '2'):
            num1 = float(input("Число 1: "))
            num2 = float(input("Число 2: "))
            
            if choice == '1':
                print("Результат:", add(num1, num2))
            elif choice == '2':
                print("Результат:", subtract(num1, num2))
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()