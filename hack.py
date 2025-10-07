
ASCII_START: int = ord('A')
ASCII_END: int = ord('Z')
ALPHABET_SIZE: int = ASCII_END - ASCII_START + 1
MIN_KEY: int = 1
MAX_KEY: int = 25

ALPHABET: dict[str, float] = {
    'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70,
    'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15,
    'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51,
    'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
    'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07
}

def hack(ciphertext: str) -> tuple[str, int]:
    """
        Взламывает шифр Цезаря, используя самый надежный способ оценки —
        сравнение частоты букв в расшифрованном тексте с эталонной частотой для английского языка
        Функция в цикле  расшифровывает сообщение каждым возможным ключом (от 1 до 25) и  после каждой
        расшифровки  программа  оуенивает, насколько полученный текст похож на осмысленный английский текст
        и возвращает наиболее вероятный исходный текст и ключ, который был для этого использован

        Args:
            ciphertext (str): Зашифрованное сообщение для взлома

        Returns:
            tuple: Кортеж содержащий наиболее вероятный расшифрованный
                   текст (str) и найденный ключ (int)
        """

    result: str = ''
    keyword: int=0
    score : int =0

    for key in range(MIN_KEY, MAX_KEY + 1):
        plaintext: str = ''

        for symbol in ciphertext:
            if symbol.isalpha():
                code: int = ord(symbol.upper())
                shifted_code: int = code - key
                if shifted_code < ASCII_START:
                    shifted_code += ALPHABET_SIZE
                new_symbol: str = chr(shifted_code)
                plaintext += new_symbol
            else:
                plaintext += symbol

        count = {}
        total_letters = 0

        for symbol in plaintext:
            if symbol.isalpha():
                symbol_upper= symbol.upper()
                total_letters += 1
                if symbol_upper in count:
                    count[symbol_upper] += 1
                else:
                    count[symbol_upper] = 1

        if total_letters == 0:
            continue

        for symbol in count:  # Преобразуем количество букв в проценты
            count[symbol] = (count[symbol]/total_letters)*100

        current_score=0
        for symbol in ALPHABET:
            current_score =current_score +plaintext.count(symbol)

        if current_score > score:
            score = current_score
            keyword=key
            result = plaintext


    return result, keyword



ciphertext = "bla bka laa"
result, keyword = hack(ciphertext)

print(ciphertext, result, keyword)
