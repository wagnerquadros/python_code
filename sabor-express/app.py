import os

restaurantes = [{'nome': 'Pollos Hermanos', 'categoria': 'Mexicano', 'ativo': False},
                {'nome': 'Pizza Planet', 'categoria': 'Pizzaria', 'ativo': True},
                {'nome': 'Big Carruna', 'categoria': 'Burger', 'ativo': False}]

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
    exibir_subtitulo('Finalizando app')

def votar_ao_menu():
    input('\nPrecione uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção Inválida')
    votar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante:')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    dados_do_retaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_retaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado')
    votar_ao_menu()

def listar_restaurantes():

    exibir_subtitulo('Listando Restaurantes:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' -> {nome_restaurante} | {categoria} | {ativo}')
    votar_ao_menu()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante para alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'Restaurante {nome_restaurante} ativado' if restaurante['ativo'] else f'Restaurante {nome_restaurante} desativado'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    votar_ao_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}!')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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