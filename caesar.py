"""
Шифрование и расшифровка строк с использованием символьного шифра в диапазоне ASCII (от 32 до 126).

Этот модуль предоставляет из себя  две функции:
1) encrypt: выполняет символьное шифрование строки со сдвигом символов.
2)decrypt: расшифровывает строку, зашифрованную с помощью "encrypt".
"""


def encrypt(plaintext, shift):
    """
    Шифрует  все печатные символы ASCII (с кодами от 32 до 126 включительно).

    Каждый сдвиг делается на определенное количество позиций.
    Если символ переходит границы допустимого диапазона( от 32 до 126 ), то сдвиг "заворачивается" в пределах указанного диапазона символов.
    Символы вне этого диапазона не изменяются
    Args:
        plaintext (str): Входная строка для шифрования
        shift (int): Величина сдвига символов.

    Returns:
        str: Зашифрованная строка.
    """
    result = ""

    for symbol in plaintext:
        code = ord(symbol)
        if 32 <= code<= 126:
            shifted_code = code + shift
            while shifted_code >126:
                shifted_code = shifted_code - 95 #Вычитаем 95(126-32+1 = 95) чтобы завернуть в начало
            while shifted_code < 32:
                shifted_code = shifted_code + 95 #Прибавляем 95 чтобы завернуть в конец
            result += chr(shifted_code)
        else:
            result += symbol
    return result




def decrypt(ciphertext, shift):
    """
    Расшифровывает все зашифрованные печатные символы ASCII (с кодами от 32 до 126 включительно).

    Каждый символ сдвигается в обратную сторону на указанное количество позиций.
    Если символ переходит границы допустимого диапазона( от 32 до 126 ), то сдвиг "заворачивается" в пределах указанного диапазона символов.
    Символы вне этого диапазона не изменяются

    Args:
        ciphertext (str): Зашифрованная строка.
        shift (int): Величина обратного сдвига для расшифровки.

    Returns:
        str: Расшифрованная строка.
    """
    result = ""

    for symbol in ciphertext:
        code = ord(symbol)

        if 32 <= code <= 126:
            shifted_code = code - shift
            while shifted_code < 32:
                shifted_code = shifted_code + 95  # Прибавляем 95 чтобы завернуть в конец
            while shifted_code >126:
                shifted_code = shifted_code - 95 #Вычитаем 95(126-32+1 = 95) чтобы завернуть в начало
            result += chr(shifted_code)
        else:
            result += symbol

    return result


text='priv'
shift= 45

a= encrypt(text,shift)
b= decrypt(a,shift)
print(a)
print(b)