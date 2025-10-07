"""
Шифрование и расшифровка строк с использованием символьного шифра в диапазоне ASCII (от 32 до 126).

Этот модуль предоставляет из себя  две функции:
1) encrypt: выполняет символьное шифрование строки со сдвигом символов.
2)decrypt: расшифровывает строку, зашифрованную с помощью "encrypt".
"""
ASCII_START: int =32
ASCII_END: int = 126
ALPHABET: int = ASCII_END - ASCII_START + 1

def encrypt(plaintext: str, shift: int) -> str:
    """
    Шифрует  все печатные символы ASCII (с кодами от 32 до 126 включительно).

    Каждый сдвиг делается на определенное количество позиций.
    Сдвиг производится в пределах диапазона ASCII_START-ASCII_END
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
        if ASCII_START <= code <= ASCII_END:
            num = code - ASCII_START
            index = (num + shift) % ALPHABET
            new_code = ASCII_START + index
            result += chr(new_code)
        else:
            result += symbol
    return result




def decrypt(ciphertext: str, shift: int) -> str:
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

        for symbol in ciphertext:
            code = ord(symbol)
            if ASCII_START <= code <= ASCII_END:
                num = code - ASCII_START
                index = (num - shift) % ALPHABET
                new_code = ASCII_START + index
                result += chr(new_code)
            else:
                result += symbol
        return result


print(encrypt("H
