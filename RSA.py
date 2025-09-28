def is_prime(n):
    """
    Проверяет является ли число простым, используюя перебор делителей от 2 до корня из n

    Args:
        n(int): число котрое проверяем

    Returns:
        True если число является простым, False если нет

    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """
    Находит наибольший общий делитель двух чисел, используя алгоритм Евклида

    Args:
        a(int): первое целое число
        b(int): второе целое число

    Returns:
        int: НОД чисел a и b

    """
    while b:
        a,b = b,a%b
    return a


def  multiplicative_inverse(e, phi):
    """
    Находит обратный элемент для е по модулю phi. Ищет число d, такое что (e*d)% phi ==1

    Args:
        e(int): число, кторое взаимно простое с phi
        phi(int): значение функции Эйлера от n

    Returns:
        Закрытая экспонента d, являющаяся мультипликативно обратной к e

    """
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d


def generate_keypair(p,q): #Выбираем два случайных простых числа p и q
    """
    Генерирует пару ключей RSA (публичный и приватный) на основе двух простых чисел.
    Вычисляет n = p * q и функция Эйлера phi = (p-1)*(q-1)
    Выбирает число e, взаимно простое с phi
    Находит число d, обратное к e по модулю phi
    Возвращаются публичный и приватный ключи в виде кортежей

        Args:
            p (int): первое простое число
            q (int): второе простое число (p!=q)

        Returns:
            tuple: кортеж из двух элементов:
                public_key (tuple): кортеж (e, n) открытый ключ для шифрования
                private_key (tuple): кортеж (d, n) закрытый ключ для расшифровки

        """
    if (not is_prime(p)) or (not is_prime(q)):
        raise ValueError
    if p==q:
        raise ValueError

    n = p * q
    phi = (p - 1) * (q - 1) #Вычисляем функцию Эйлера

    #В этом блоке выбираем число e, которое меньше  phi и является взаимно простым с phi
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = multiplicative_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)
    return (public_key, private_key)


def encrypt(public_key, text):
    """
    Шифрует текст с использованием открытого ключа RSA по форммуле C=M**e mod n

    Args:
        public_key (tuple): Кортеж вида (e, n)
        text (str): Строка текста для шифрования

    Returns:
        cipher_list: Список зашифрованных чисел, соответствующих каждому символу текста

    """
    cipher_list = []
    e = public_key[0]
    n = public_key[1]

    #В этом блоке мы перебираем каждую букву из строки, превращаем ее в числовой код и считаем по формуле C=M**e mod n
    for symbol in text:
        code = ord(symbol)
        encrypted_num = (code ** e) % n
        cipher_list.append(encrypted_num)

    return cipher_list


def decrypt(private_key, cipher_list):
    """
    Расшифровывает список чисел, зашифрованных с помощью RSA( по формуле M=C**d mod n), обратно в текст

    Args:
        private_key (tuple): Кортеж вида (d, n)
        cipher_list (list): Список зашифрованных чисел

    Returns:
        str: Расшифрованный текст

    """
    d = private_key[0]
    n = private_key[1]
    text = ""

    #В этом блоке мы перебираем каждую зашифрованную букву из строки,
    # превращаем зашифрованную букву обратно и считаем по формуле M=C**d mod n
    for encrypted_num in cipher_list:
        decrypted_num = (encrypted_num ** d) % n
        decrypted_symbol = chr(decrypted_num)
        text += decrypted_symbol

    return text

print(is_prime(10))

print( gcd(20,25))  # 5


p = 17
q = 23
public_key, private_key = generate_keypair(p, q)
print( public_key, private_key)

text = "Hello World!"
cipher = encrypt(public_key, text)
print( cipher)

decrypted_text = decrypt(private_key, cipher)
print( decrypted_text)