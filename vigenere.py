"""
Шифрование и расшифровка строк с использованием шифра Виженера в диапазоне ASCII (от 32 до 126).

Этот модуль предоставляет из себя две функции:
1)encrypt: выполняет символьное шифрование строки со сдвигом символов
2)decrypt: расшифровывает строку, зашифрованную с помощью "encrypt".
"""



def encrypt(plaintext, keyword):
    """
    Шифрует  все печатные символы ASCII (с кодами от 32 до 126 включительно) с использованием ключа по принципу шифра Виженера.
    Ключевое слово (keyword) применяется циклически.
    Символы в ключевом слове нечувствительны к регистру ('A' и 'a' эквивалентны сдвигу на 0, 'B' и 'b' — на 1, и т.д.).

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

        if 32<=code<126:
            if k>=len(keyword): #Если мы дошли до конца ключа, то ключевое слово (keyword) применяем циклически
                k=0
            shift  =ord(keyword[k])-ord('A')#Вычитаем А чтобы получить сдвиг в диапазоне 0-25
            shifted_code= shift+code

            while shifted_code>126:
                shifted_code=shifted_code-95
            while shifted_code<32:
                shifted_code=shifted_code+95
            result = result + chr(shifted_code)
            k+=1

        else:
            result += symbol
    return result



def decrypt(ciphertext, keyword):
    """
       Дешифрует  все печатные символы ASCII (с кодами от 32 до 126 включительно) с использованием ключа по принципу шифра Виженера.
       Ключевое слово (keyword) применяется циклически.
       Символы в ключевом слове нечувствительны к регистру ('A' и 'a' эквивалентны сдвигу на 0, 'B' и 'b' — на 1, и т.д.).


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
    keyword = new_keyword

    keyword = new_keyword.upper()  # Переводим буквы в верхний регистр чтобы стандартизировать все буквы ключа

    if len(keyword)==0:
        return plaintext

    result = ''
    k = 0 #Создаем счетчик для цикличного использования буквы ключа

    for symbol in ciphertext:
        code = ord(symbol)

        if 32 <= code < 126:
            if k >= len(keyword): #Если мы дошли до конца ключа, то ключевое слово (keyword) применяем циклически
                k = 0
            shift =ord(keyword[k])-ord('A')#Вычитаем А чтобы получить сдвиг в диапазоне 0-25
            shifted_code= code - shift

            while shifted_code > 126:
                shifted_code = shifted_code - 95
            while shifted_code < 32:
                shifted_code = shifted_code + 95

            result = result + chr(shifted_code)
            k+=1

        else:
            result += symbol

    return result


a='itmo'
keyword='mom'
print(encrypt(a,keyword))
print(decrypt(encrypt(a,keyword),keyword))
