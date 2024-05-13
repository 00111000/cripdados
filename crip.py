# import os
# import base64
# import random
# import string
# import hashlib
# from cryptography.fernet import Fernet

# def exibir_nome_do_programa():
#     print("""

# ░█████╗░██████╗░██╗██████╗░░░░██████╗░░█████╗░██████╗░░█████╗░░██████╗
# ██╔══██╗██╔══██╗██║██╔══██╗░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
# ██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░██║███████║██║░░██║██║░░██║╚█████╗░
# ██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░██║██╔══██║██║░░██║██║░░██║░╚═══██╗
# ╚█████╔╝██║░░██║██║██║░░░░░██╗██████╔╝██║░░██║██████╔╝╚█████╔╝██████╔╝
# ░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═════╝░
#     """)

# def gerar_senha():
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     senha = ''.join(random.choice(caracteres) for _ in range(20))  # Senha com 20 caracteres
#     print("Senha gerada:", senha)  # Adicionando print para debug
#     return senha

# def salvar_chave(chave):
#     with open("chave.txt", "wb") as f:
#         f.write(chave)

# def carregar_chave():
#     with open("chave.txt", "rb") as f:
#         chave = f.read()
#     return chave

# def calcular_hash(arquivo):
#     sha256 = hashlib.sha256()
#     with open(arquivo, 'rb') as f:
#         while True:
#             data = f.read(8192)  # Leitura em blocos de 8KB
#             if not data:
#                 break
#             sha256.update(data)
#     return sha256.digest()

# def criptografar_arquivo(arquivo):
#     if os.path.exists(arquivo):
#         chave = carregar_chave()
#         arquivo_hash = calcular_hash(arquivo)
#         fernet = Fernet(chave)
#         with open(arquivo, 'rb') as f:
#             conteudo = f.read()
#         conteudo_criptografado = fernet.encrypt(conteudo)
#         with open(arquivo, 'wb') as f:
#             f.write(conteudo_criptografado)
#         print("Arquivo criptografado com sucesso!")
#     else:
#         print("O arquivo especificado não existe!")

# def descriptografar_arquivo(arquivo):
#     if os.path.exists(arquivo):
#         chave = carregar_chave()
#         arquivo_hash = calcular_hash(arquivo)
#         fernet = Fernet(chave)
#         with open(arquivo, 'rb') as f:
#             conteudo_criptografado = f.read()
#         conteudo_descriptografado = fernet.decrypt(conteudo_criptografado)
#         with open(arquivo, 'wb') as f:
#             f.write(conteudo_descriptografado)
#         print("Arquivo descriptografado com sucesso!")
#     else:
#         print("O arquivo especificado não existe!")

# def main():
#     exibir_nome_do_programa()
#     arquivo = input("Digite o nome do arquivo que deseja criptografar/descriptografar: ")
#     opcao = input("Digite 'c' para criptografar ou 'd' para descriptografar: ")
#     if opcao.lower() == 'c':
#         chave = Fernet.generate_key()
#         salvar_chave(chave)
#         criptografar_arquivo(arquivo)
#     elif opcao.lower() == 'd':
#         descriptografar_arquivo(arquivo)
#     else:
#         print("Opção inválida!")

# if __name__ == "__main__":
#     main()

import os
import base64
import random
import string
import hashlib
from cryptography.fernet import Fernet

listadedados = []

def exibir_nome_do_programa():
    print("""

░█████╗░██████╗░██╗██████╗░░░░██████╗░░█████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██║██╔══██╗░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░██║███████║██║░░██║██║░░██║╚█████╗░
██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░██║██╔══██║██║░░██║██║░░██║░╚═══██╗
╚█████╔╝██║░░██║██║██║░░░░░██╗██████╔╝██║░░██║██████╔╝╚█████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═════╝░
    """)

def exibir_menu(): 
    print('----------------------------------------------')
    print('c = Criptografar arquivo (c)')
    print('d = Descriptografar arquivo. (d)')
    print('g = Gerar arquivo .txt')
    print('add = Adicionar informações')
    print('s = Sair.\n')
    print('script feito pelo 00fleck')
    print('----------------------------------------------')

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('Pressione a tecla "enter" para retornar ao menu principal.')
    main()    

def Finalizar_app ():
    exibir_subtitulo('App finalizado.')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(20))  # Senha com 20 caracteres
    print("Senha gerada:", senha)  # Adicionando print para debug
    return senha

def salvar_chave(chave):
    with open("chave.txt", "wb") as f:
        f.write(chave)

def carregar_chave():
    if os.path.exists("chave.txt"):
        with open("chave.txt", "rb") as f:
            chave = f.read()
        return chave
    else:
        print("O arquivo de chave 'chave.txt' não existe.")
        return None

def calcular_hash(arquivo):
    sha256 = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        while True:
            data = f.read(8192)  # Leitura em blocos de 8KB
            if not data:
                break
            sha256.update(data)
    return sha256.digest()

def criptografar_arquivo(arquivo):
    if os.path.exists(arquivo):
        chave = Fernet.generate_key()
        salvar_chave(chave)
        arquivo_hash = calcular_hash(arquivo)
        fernet = Fernet(chave)
        with open(arquivo, 'rb') as f:
            conteudo = f.read()
        conteudo_criptografado = fernet.encrypt(conteudo)
        with open(arquivo, 'wb') as f:
            f.write(conteudo_criptografado)
        print("Arquivo criptografado com sucesso!")
    else:
        print("O arquivo especificado não existe!")
    voltar_ao_menu_principal()

def descriptografar_arquivo(arquivo):
    if os.path.exists(arquivo):
        chave = carregar_chave()
        if chave:
            arquivo_hash = calcular_hash(arquivo)
            fernet = Fernet(chave)
            with open(arquivo, 'rb') as f:
                conteudo_criptografado = f.read()
            conteudo_descriptografado = fernet.decrypt(conteudo_criptografado)
            with open(arquivo, 'wb') as f:
                f.write(conteudo_descriptografado)
            print("Arquivo descriptografado com sucesso!")
        else:
            print("Não foi possível descriptografar o arquivo sem a chave.")
    else:
        print("O arquivo especificado não existe!")
    voltar_ao_menu_principal()

def adicionar_dados():
    exibir_subtitulo('Coloque as informações: ')
    dados = input()
    listadedados.append(dados)
    print(f'Os dados foi inseridos corretamente.\n')
    voltar_ao_menu_principal()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    opcao = input("Escolha a opção: ")
    if opcao.lower() == 'c':
        arquivo = input("Digite o nome do arquivo que deseja criptografar: ")
        criptografar_arquivo(arquivo)
    elif opcao.lower() == 'd':
        arquivo = input("Digite o nome do arquivo que deseja descriptografar: ")
        descriptografar_arquivo(arquivo)
    elif opcao.lower() == 's':
        Finalizar_app()
    elif opcao.lower() == 'add':
        adicionar_dados():
        
    else:
         opcao_invalida()

if __name__ == "__main__":
    main()
