import math
import sys

def add(x: float, y: float) -> float:
    """Сложение"""
    return x + y

def subtract(x: float, y: float) -> float:
    """Вычитание"""
    return x - y

def multiply(x: float, y: float) -> float:
    """Умножение"""
    return x * y

def divide(x: float, y: float) -> float:
    """Деление с проверкой на ноль"""
    if y == 0:
        raise ValueError("Деление на ноль невозможно!")
    return x / y

def power(x: float, y: float) -> float:
    """Возведение в степень"""
    return x ** y

def square_root(x: float) -> float:
    """Квадратный корень с проверкой на отрицательное число"""
    if x < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа!")
    return math.sqrt(x)

def modulo(x: float, y: float) -> float:
    """Остаток от деления"""
    if y == 0:
        raise ValueError("Остаток от деления на ноль невозможен!")
    return x % y


def show_menu() -> None:
    print("\n" + "="*30)
    print("   Калькулятор")
    print("="*30)
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (**)")
    print("6. Квадратный корень (√)")
    print("7. Остаток от деления (%)")
    print("0. Выход")
    print("="*30)

def get_number(prompt: str) -> float:
    """Безопасный ввод числа с обработкой ошибок"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Пожалуйста, введите число (можно с точкой, например 3.14).")

def main() -> None:
    """Главный цикл программы"""
    # Словарь для связи выбора пользователя и функции
    operations = {
        '1': (add, "Введите первое число: ", "Введите второе число: "),
        '2': (subtract, "Введите уменьшаемое: ", "Введите вычитаемое: "),
        '3': (multiply, "Введите первый множитель: ", "Введите второй множитель: "),
        '4': (divide, "Введите делимое: ", "Введите делитель: "),
        '5': (power, "Введите число: ", "Введите степень: "),
        '6': (square_root, "Введите число: ", None),
        '7': (modulo, "Введите делимое: ", "Введите делитель: ")
    }

    while True:
        show_menu()
        choice = input("Выберите операцию (0-7): ").strip()

        if choice == '0':
            print("\nСпасибо за использование калькулятора. До свидания!")
            sys.exit(0)
            
        if choice in operations:
            func, prompt1, prompt2 = operations[choice]
            
            try:
                num1 = get_number(prompt1)
                
                if prompt2:
                    num2 = get_number(prompt2)
                    result = func(num1, num2)
                else:
                    result = func(num1)
          
                if result.is_integer():
                    result = int(result)
                    
                print(f" Результат: {result}")
                
            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")
        else:
            print("Неверный выбор. Пожалуйста, выберите цифру от 0 до 7.")

if __name__ == "__main__":
    main()
