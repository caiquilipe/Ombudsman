from constants import accept_key_menu
from exceptions import SystemDone


manifestations = []
try:
    while True:
        menu_key = 999999
        print('\n\nSelecione uma opção: \nListar todas manifestações: 1\nListar todas sugestões: 2\nListar todas reclamações: 3\nListar todos elogios: 4\nCriar uma manifestação: 5\nBuscar uma manifestação: 6\nSair do sistema: 7')
        while not menu_key in list(range(1, 8)):
            try:
                menu_key = int(input('\n\nEscolha uma opção: '))
            except:
                print('\nDigite um numero inteiro.')
        response = accept_key_menu[menu_key]
        response(manifestations)
except SystemDone:
    print('\n\nFinalizando sistema.')
