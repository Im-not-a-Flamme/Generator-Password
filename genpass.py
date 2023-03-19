import random ##Importa o módulo "random", que é usado para gerar números aleatórios.
import base64 ##Importa o módulo "base64", usado para criptografia.
import pyfiglet

banner = pyfiglet.figlet_format("GENP@S$", font="slant")
print(banner)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' ##Define a string "chars" como uma sequência de caracteres alfanuméricos.
chars_special = '!@#$%^&*()_+' ##Define a string "chars_special" como uma sequência de caracteres especiais.

def generate_simple_password(length): ##Define uma função chamada "generate_simple_password" que gera uma senha aleatória usando apenas caracteres alfanuméricos.
    password = ''.join(random.choice(chars) for _ in range(length)) 
    return password ##Retorna a senha gerada.

def generate_complex_password(length): ##Define uma função chamada "generate_complex_password" que gera uma senha aleatória usando caracteres alfanuméricos e especiais.
    password = ''.join(random.choice(chars + chars_special) for _ in range(length)) 
    return password 

def generate_encoded_password(length):
    password = ''.join(random.choice(chars + chars_special) for _ in range(length))
    password = base64.b64encode(password.encode('utf-8'))
    return password

while True: 
    typeP = input("Type for Password: S = (Simple) / C = (Complex) / E = (Encoded) / or Q(quit) ").lower() ##Solicita ao usuário que digite um tipo de senha ("S" para simples, "C" para complexa ou "Q" para sair) e armazena a entrada em "typeP", convertendo-a para minúsculas.
    
    if typeP == "s" or typeP == "simple": ##Se o usuário digitar "S" (para senha simples)    
        length = int(input("\nLength Password: ")) ##Solicita ao usuário que digite o comprimento da senha e armazena o valor em "length".
        password = generate_simple_password(length) ##Chama a função "generate_simple_password" para gerar uma senha aleatória com o comprimento "length" e armazena o valor em "password".
        print('Password:', password) 

    elif typeP == "c" or typeP == "complex": ##Se o usuário digitar "C" (para senha complexa)
        length = int(input("\nLength Password: ")) 
        password = generate_complex_password(length)
        print('Password:', password) 
    
    elif typeP == "quit" or typeP == 'q': ##Se o usuário digitar "Q" (para sair)
        print("Quitting Password Generator...") 
        break
    
    elif typeP == "e" or typeP == "encoded":  ##Se o usuário digitar "E" (para senha criptografada em base64)
        length = int(input("\nLength Password: ")) 
        password = generate_encoded_password(length)
        print("=Encoded Base64=")
        print('Password:', password)
    
    else: ##Se o usuário digitar uma entrada inválida:
        print("Invalid Input. Please Try Again.")
