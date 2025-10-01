#Autor: José Daniel Salcedo Gutiérrez

#=======================================================================================
#Primer punto:
#Cree un algoritmo que lea 5 números enteros uno por uno e identifique cuáles son positivos y pares. Al final, debe mostrar la suma total de esos números

def primero():
    numero = []
    sum = 0
    for i in range(5): 
        num = int(input("Escriba un numero par positivo:\t"))
        even = num/2
        numero.append(num)
        if num > 0 and even.is_integer(): 
            sum += num
            print(f"Los numero pares son estos {num} ")
    print(f"La suma de números pares es esta:\t{sum} ")
    print(f" La lista de numeros es esta:\t{numero}")


#=======================================================================================
#Segundo punto:
'''Diseñe un programa que lea la edad de una persona y muestre un mensaje según el siguiente criterio:
· Menor de 13 años → “Niño”

· Entre 13 y 17 años → “Adolescente”

· Entre 18 y 59 años → “Adulto”

· 60 años o más → “Adulto mayor”
'''
def segundo():
    age = int(input("digite su edad para clasificarlo:\t"))

    if age < 13: 
        print("niño")
    elif(age < 17 and age >= 13): 
        print("Adolescente.")
    elif(age < 59 and age >= 18): 
        print("Adulto")
    elif(age > 60): 
        print("Adulto mayor")

#=======================================================================================
#Tercer punto: 
# Solicite al usuario que escriba una palabra (sin espacios) y cuente cuántas vocales tiene. El programa debe ser sensible a mayúsculas y minúsculas (es decir, contar tanto a como A).
def tercero():
    letra = input("Escriba una palabra sin espacios:\t")
    if " " == letra: 
            print("Su texto contiene espacios.")
    else:
        for i in letra: 
            print(i)
            print(f"La vocal a esta {i.count("a")} veces.")
            print(f"La vocal e esta {i.count("e")} veces.")
            print(f"La vocal i esta {i.count("i")} veces.")
            print(f"La vocal o esta {i.count("o")} veces.")
            print(f"La vocal u esta {i.count("u")} veces.")
            print(f"La vocal A esta {i.count("A")} veces.")
            print(f"La vocal E esta {i.count("E")} veces.")
            print(f"La vocal I esta {i.count("I")} veces.")
            print(f"La vocal O esta {i.count("O")} veces.")
            print(f"La vocal U esta {i.count("U")} veces.")

def main():
    primero()
    segundo()
    tercero()

if __name__ == "__main__":
    main()
        
            
        