# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата
# На входе:
# num = 255
# На выходе:
# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff
num = 0
hex_str = ""

# Проверка результата с помощью функции hex()
expected_hex = hex(num)[2:]

if num == 0:
    hex_str = ""
else:
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            hex_digit = str(remainder)
        else:
            hex_digit = chr(ord('A') + remainder - 10)
        hex_str = hex_digit + hex_str
        num = num // 16

    # Проверка результата

print(f"Шестнадцатеричное представление числа: {hex_str}")
print(f"Проверка результата: 0x{expected_hex}")
