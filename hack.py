alphabet = ['E', 'T', 'A', 'O', 'I', 'N']

def hack(ciphertext):
    """
        Взламывает шифр Цезаря, используя самый надежный способ оценки —
        сравнение частоты букв в расшифрованном тексте с эталонной частотой для английского языка 'E', 'T', 'A', 'O', 'I', 'N'
        Функция в цикле  расшифровывает сообщение каждым возможным ключом (от 1 до 25) и  после каждой
        расшифровки  программа  оуенивает, насколько полученный текст похож на осмысленный английский текст
        и возвращает наиболее вероятный исходный текст и ключ, который был для этого использован

        Args:
            ciphertext (str): Зашифрованное сообщение для взлома

        Returns:
            tuple: Кортеж содержащий наиболее вероятный расшифрованный
                   текст (str) и найденный ключ (int)
        """
    result = ''
    keyword=0
    score = 0 #наибольшее количсетво букв из alphabet

    for key in range(1,26):  #В цикле расшифровываем сообщение каждым возможным ключом (от 1 до 25)
        plaintext = ''

        for symbol in ciphertext:
            if symbol.isalpha():
                code=ord(symbol.upper())
                shifted_code= code -key #CСдвигаем код символа обратно по алфаивту
                if shifted_code <ord('A'):
                    shifted_code = shifted_code+26 #Прибавляем 26 чтобы врнуться в диапазон (А - Z)(зацикливаем алфавит)
                new_symbol =chr(shifted_code)
                plaintext = plaintext+ new_symbol
            else:
                plaintext =plaintext + symbol

        current_score = 0
        for symbol in alphabet:
            current_score = current_score+ plaintext.count(symbol)

        if current_score > score:
            score = current_score
            result =plaintext
            keyword=key

    return(result,keyword)

ciphertext = "maama mia"
result, keyword = hack(ciphertext)

print(ciphertext, result, keyword)