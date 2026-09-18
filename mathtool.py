"""Консольное приложение для решения уравнений A*x^2 + B*x + C = 0."""

import math
import sys


MAX_VALUE = 10_000

HELP_TEXT = """mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
  python mathtool.py                  вывод справки
  python mathtool.py --help           вывод справки
  python mathtool.py solve            ввод коэффициентов с клавиатуры
  python mathtool.py solve -a 1 -b -3 -c 2
                                       решение с заданными коэффициентами

Коэффициенты A, B, C должны быть целыми числами,
по модулю не превышающими 10000.
"""


# Разбор параметров командной строки.
arguments = sys.argv[1:]

if len(arguments) == 0 or arguments[0] == "--help":
    print(HELP_TEXT)
    sys.exit(0)

if arguments[0] != "solve":
    print(f"ОШИБКА: неизвестная команда '{arguments[0]}'", file=sys.stderr)
    sys.exit(1)

keyboard_input = False

if len(arguments) == 1:
    keyboard_input = True
elif len(arguments) == 7:
    if arguments[1] != "-a" or arguments[3] != "-b" or arguments[5] != "-c":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)

    raw_a = arguments[2]
    raw_b = arguments[4]
    raw_c = arguments[6]
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)


# Получение коэффициентов и преобразование их в целые числа.
try:
    if keyboard_input:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    else:
        a = int(raw_a)
        b = int(raw_b)
        c = int(raw_c)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)


# Проверка допустимого диапазона значений.
if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)


# Определение вида уравнения, решение и вывод результата.
if a == 0:
    if b == 0:
        print(
            "ОШИБКА: это не уравнение, неизвестное отсутствует",
            file=sys.stderr,
        )
        sys.exit(1)

    print("Уравнение линейное")
    x = -c / b
    print(f"x = {x:.3f}")
else:
    print("Уравнение квадратное")
    discriminant = b * b - 4 * a * c
    print(f"D = {discriminant}")

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")
