

def somar():
    a = float(input("digite o primeiro numero: "))
    b = float(input("digite o segundo numero: "))
    res = a + b
    print(res)


def sub():
    a = float(input("digite o primeiro numero: "))
    b = float(input("digite o segundo numero: "))
    res = a - b
    print(res)


def mult():
    a = float(input("digite o primeiro numero: "))
    b = float(input("digite o segundo numero: "))
    res = a * b
    print(res)


def div():
    a = float(input("digite o primeiro numero: "))
    b = float(input("digite o segundo numero: "))
    res = a / b
    print(res)


print("Digite 'q' para sair a qualquer momento")

while True:

    operador = input(
        "\nVocê deseja utilizar qual operador? (soma, sub, mult, div) ")
    if operador == "soma":
        try:
            somar()
        except ValueError:
            print("\nÉ impossivel fazer calculos com letras ou caracteres especiais. Favor tente novamente com numeros.")
    if operador == "sub":
        try:
            sub()
        except ValueError:
            print("\nÉ impossivel fazer calculos com letras ou caracteres especiais. Favor tente novamente com numeros.")
    if operador == "mult":
        try:
            mult()
        except ValueError:
            print("\nÉ impossivel fazer calculos com letras ou caracteres especiais. Favor tente novamente com numeros.")
    if operador == "div":
        try:
            div()
        except ValueError:
            print("\nÉ impossivel fazer calculos com letras ou caracteres especiais. Favor tente novamente com numeros.")
        except ZeroDivisionError:
            print("\nÉ impossivel dividir um numero por zero!")
    if operador == "q":
        print("Saindo...")
        break
