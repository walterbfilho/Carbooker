import json
import os

import locadora
import usuario

def main():

    while True:
        print("\n============================")
        print("Bem vindo(a) ao CarBooker!! ")
        print("============================")
        print("1. Usuário")
        print("2. Locadora")
        print("3. Sair")
        print("============================")
        arquivo_json = "usuarios.json"
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            usuario.menu()
        elif opcao == "2":
            locadora.menu()
        else:
            break


if __name__ == "__main__":
    main()
