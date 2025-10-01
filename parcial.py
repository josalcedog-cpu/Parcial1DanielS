#Autor: José Daniel Salcedo Gutiérrez

#=======================================================================================
#Primer punto:
#Cree un algoritmo que lea 5 números enteros uno por uno e identifique cuáles son positivos y pares. Al final, debe mostrar la suma total de esos números

def primero():
    numero = []
    sum = 0
    for i in range(5): 
        num = int(input("Escriba un numero:\t"))
        even = num/2
        numero.append(num)
        if num > 0 and even.is_integer(): 
            sum += num
            print(f"Su numero {num} es par positivo.")
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
    age = int(input("\nDigite su edad para clasificarlo:\t"))

    if age < 13: 
        print("Niño")
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
   
    letra = input("\nEscriba una palabra sin espacios:\t")
    if " " in letra: 
        print (f"Su texto tiene espacios, tiene {letra.count(" ")} espacios")
    else: 
        print(f"La vocal 'a' aparece {letra.count('a')} veces.")
        print(f"La vocal 'a' aparece {letra.count('a')} veces.")
        print(f"La vocal 'e' aparece {letra.count('e')} veces.")
        print(f"La vocal 'i' aparece {letra.count('i')} veces.")
        print(f"La vocal 'o' aparece {letra.count('o')} veces.")
        print(f"La vocal 'u' aparece {letra.count('u')} veces.")


        print(f"La vocal 'A' aparece {letra.count('A')} veces.")
        print(f"La vocal 'E' aparece {letra.count('E')} veces.")
        print(f"La vocal 'I' aparece {letra.count('I')} veces.")
        print(f"La vocal 'O' aparece {letra.count('O')} veces.")
        print(f"La vocal 'U' aparece {letra.count('U')} veces.")
        

            

def main():
    primero()
    segundo()
    tercero()

if __name__ == "__main__":
    main()
        
            
        