import os

restaurantes = ['Pollos Hermanos', 'Pizza Planet']

def exibir_nome():
    print("""
        █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
        ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls') # Limpa o console
    print('Fnalizando o app\n')

def opcao_invalida():
    print('Opção Inválida')
    input('Precione uma tecla para voltar ao menu')
    main()


def cadastrar_novo_restaurante():
    os.system('cls')
    print('Casdastro de Restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado')
    input('Precione uma tecla para voltar ao menu')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}!')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar Restaurante')
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()