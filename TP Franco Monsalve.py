def validocodigo(x):
    if x.isnumeric():
        x = int(x)
        if 0 <= x <= 99:
            return 0
        else:
            return 1
    else:
        return 1

def validoprecio(x):
    if x.replace('.', '', 1).isdigit():  # Permite un punto decimal solo una vez
        x = float(x)
        if 10 <= x <= 999.99:
            return 0
        else:
            return 1
    else:
        return 1

cantcp = 0
CP = input("Ingrese un codigo de pieza (00-99), ingrese 0 para finalizar: ")

while CP != "0":
    ValidadoCP = validocodigo(CP)
    if ValidadoCP == 0:
        CP = int(CP)
        cantcc = 0
        PrT = 0
        cantcp += 1
        print(f"Su codigo de pieza es: {CP}")
        CC = input("Ingrese un codigo de componente de por lo menos 2 digitos, ingrese 0 para finalizar: ")

        while CC != "0":
            ValidadoCC = validocodigo(CC)
            if ValidadoCC == 0:
                CC = int(CC)
                CC = CC * 100 + CP
                print(f"Su codigo de componente es: {CC}")
                while True:
                    PrC = input("Ingrese el precio del componente: ")
                    if validoprecio(PrC) == 0:
                        PrC = float(PrC)
                        cantcc += 1
                        PrT += PrC
                        print(f"El precio del componente es: ${PrC}")
                        CC = input("Ingrese otro componente o ingrese 0 para finalizar: ")
                        break
                    else:
                        print("Precio de componente incorrecto, vuelva a ingresar un precio entre 10,00 y 999,99.")
            else:
                CC = input("Codigo de componente incorrecto, vuelva a ingresar un codigo entre 00 y 99: ")

        print(f"El precio total de {cantcc} componentes es: ${PrT}")
        CP = input("Vuelva a ingresar un código de pieza o ingrese 0 para finalizar: ")
    
    else:
        CP = input("Codigo de pieza incorrecto, vuelva a ingresar un codigo entre 00 y 99 o ingrese 0 para finalizar: ")

print("Cantidad de piezas procesadas:", cantcp)