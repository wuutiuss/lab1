"""
Шифрование и расшифровка строк с использованием шифра Виженера в диапазоне ASCII (от 32 до 126).

Этот модуль предоставляет из себя две функции:
1)encrypt: выполняет символьное шифрование строки со сдвигом символов
2)decrypt: расшифровывает строку, зашифрованную с помощью "encrypt".
"""
from lab1.caesar import ALPHABET

ASCII_START: int = 32
ASCII_END: int = 126
ALPHABET_SIZE: int = ASCII_END - ASCII_START + 1


def encrypt(plaintext: str, keyword: str) -> str:
    """
      Шифрует все печатные символы ASCII с использованием ключа по принципу шифра Виженера

    Args:
        plaintext (str): Входная строка для шифрования.
        keyword (str): Ключевое слово, в котором учитываются только буквы

    Returns:
        str: Зашифрованная строка
    """
    new_keyword= ''
    for symbol in keyword: #В этом модуле мы проверяем является ли символ буквой и формируем ключ
        if symbol.isalpha():
            new_keyword = new_keyword+symbol

    keyword=new_keyword.upper() #Переводим буквы в верхний регистр чтобы стандартизировать все буквы ключа

    if len(keyword)==0:
        return plaintext

    result= ''
    k=0 #Создаем счетчик для цикличного использования буквы ключа

    for symbol in plaintext:
        code= ord(symbol)

        if ASCII_START <= code <= ASCII_END:
            shift = ord(keyword[k]) - ord('A')

            shifted_code = ASCII_START + (code - ASCII_START + shift) % ALPHABET_SIZE
            result += chr(shifted_code)

            k = (k + 1) % len(keyword)

        else:
            result += symbol
    return result



def decrypt(ciphertext, keyword):
    """
    Дешифрует все печатные символы ASCII с использованием ключа по принципу шифра Виженера

       Args:
           ciphertext (str): Входная строка для расшифровки.
           keyword (str): Ключевое слово, в котором учитываются только буквы.

       Returns:
           str: Расшифрованная строка.
       """
    new_keyword = ''
    for symbol in keyword:#В этом модуле мы проверяем является ли символ буквой и формируем ключ
        if symbol.isalpha():
            new_keyword += symbol
    keyword = new_keyword.upper()  # Переводим буквы в верхний регистр чтобы стандартизировать все буквы ключа

    if len(keyword)==0:
        return ciphertext

    result = ''
    k = 0 #Создаем счетчик для цикличного использования буквы ключа

    for symbol in ciphertext:
        code = ord(symbol)

        if ASCII_START <= code <= ASCII_END:

            shift = ord(keyword[k]) - ord('A')

            shifted_code = ASCII_START + (code - ASCII_START - shift) % ALPHABET_SIZE
            result += chr(shifted_code)

            k = (k + 1) % len(keyword)

        else:
            result += symbol

    return result


print(encrypt("atack at dawn", "LEMON"))
