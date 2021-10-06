def prim(n):
    '''
    prim verifica daca un numar n este prim
    :param n: int
    :return: true daca n e prim false in caz contrar
    '''
    i = 1
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def is_superprim(n):
    '''
    superprim verifica daca un nr n este superprim
    :param n: numarul verificat (int)
    :return: true daca n este superprim false in caz contrar
    '''

    t = 1
    while n > t:
        t = t * 10
    t = t // 10
    while t != 0:
        prefix = n // t
        if prim(prefix) == True:
            t = t // 10
        else:
            return False
    return True

def test_is_superprim(n):
    '''
    functie test
    '''
    t = 1
    while n > t:
        t = t * 10
    t = t // 10
    while t != 0:
        prefix = n // t
        if prim(prefix) == True:
            t = t // 10
        else:
            return False
    return True

assert test_is_superprim(233) == True
assert test_is_superprim(237) == False
assert test_is_superprim(23) == True
assert test_is_superprim(879) == False

def inversul(n):
    '''
    creeaza inversul unui nr (ex 123 devine 321)
    :param n: numarul pt care se calculeaza inversul (int)
    :return: inversul numarului n
    '''
    global invers
    invers = 0
    while n != 0:
        invers = invers * 10 + n % 10
        n = n // 10
    return invers


def is_palindrom(n):
    '''
    verifica daca un numar este palindrom
    :param n:numarul verificat (int) 
    :return: true daca n e palindrom false in caz contrar
    '''
    if inversul(n) == n:
        return True
    else:
        return False
def test_is_palindrom(n):
    '''
    fuctie test
    '''
    if inversul(n) == n:
        return True
    else:
        return False

assert test_is_palindrom(233) == False
assert test_is_palindrom(121) == True
assert test_is_palindrom(253) == False
assert test_is_palindrom(552) == False
assert test_is_palindrom(1881) == True
def get_goldbach(n):
    '''
    determina numere prime p1 si p2 astfel incat n=p1+p2.
    :param n: numarul pentru care dorim sa gasim p1 si p2
    :return:p1 si p2 numere prime astfel incat n=p1+p2
    '''
    if prim(n - 2) == True:
        return 2, n - 2
    i = 3
    for i in range(3, n // 2, 2):
        if prim(i) == True and prim(n - i) == True:
            return i, n - i
    return 0,0

def test_get_goldbach(n):
    '''
    functie test
    '''
    if prim(n - 2) == True:
        return 2, n - 2
    i = 3
    for i in range(3, n // 2, 2):
        if prim(i) == True and prim(n - i) == True:
            return i, n - i
    return 0,0

assert test_get_goldbach(7) == (2, 5)
assert test_get_goldbach(11) == (0,0)
assert test_get_goldbach(9) == (2, 7)
assert test_get_goldbach(4) == (2, 2)
assert test_get_goldbach(5) == (2, 3)
if __name__ == '__main__':
    isRuning = True
    while isRuning == True:
        print('Acest program este capabil de mai multe lucruri')
        print('1.Verificare daca un numar este superprim')
        print('2.Verificare daca un numar este palindorm')
        print('3.Verificare goldbach')
        print('x.Iesire')
        obtiune = input('Selectati optiunea')
        if obtiune == '1':
            n = int(input('Dati nr care doriti sa il verificati'))
            if is_superprim(n) == True:
                print('Numarul este superprim')
            else:
                print('Numarul nu e superprim')
            print('Doriti sa efectuati alte comenzi?')
            print('y.da')
            print('n.nu')
            y_or_n = input('Selectati obtiunea')
            if y_or_n == 'n':
                isRuning = False
        if obtiune == '2':
            n = int(input('Dati nr care doriti sa il verificati'))
            if is_palindrom(n) == True:
                print('Numarul este palindrom')
            else:
                print('Numarul nu este palindrom')
            print('Doriti sa efectuati alte comenzi?')
            print('y.da')
            print('n.nu')
            y_or_n = input()
            if y_or_n == 'n':
                isRuning = False
        if obtiune == '3':
            n = int(input('Dati nr care doriti sa il verificati'))
            if get_goldbach(n) !=(0,0):
                print(get_goldbach(n),' sunt numerele p1 si p2 astfel incat n=p1 + p2 ')
            else:
                print('Nu exista 2 numere p1 si p2 astfel incat n=p1+p2')
            print('Doriti sa efectuati alte comenzi?')
            print('y.da')
            print('n.nu')
            y_or_n = input()
            if y_or_n == 'n':
                isRuning = False
        if obtiune == 'x':
            isRuning = False
