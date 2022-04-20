from manifestation import Manifestation, ManifestationStatus
from exceptions import SystemDone


def find_all_manifestations(manifestations):
    print('\n\nListagem das manifestações: ')
    if not manifestations:
        print(manifestations)
    for manifestation in manifestations:
        print(manifestation)

def find_all_seggestions(manifestations):
    print('\n\nListagem das sugestões: ')
    count = 0
    for manifestation in manifestations:
        if manifestation.status == ManifestationStatus.SUGGESTION.value[1]:
            print(manifestation)
            count += 1
    if count == 0:
        print([])

def find_all_claims(manifestations):
    print('\n\nListagem das reclamações: ')
    count = 0
    for manifestation in manifestations:
        if manifestation.status == ManifestationStatus.COMPLAINT.value[1]:
            print(manifestation)
            count += 1
    if count == 0:
        print([])

def find_all_praise(manifestations):
    print('\n\nListagem das elogios: ')
    count = 0
    for manifestation in manifestations:
        if manifestation.status == ManifestationStatus.PRAISE.value[1]:
            print(manifestation)
            count += 1
    if count == 0:
        print([])

def create_manifestation(manifestations: list):
    id = len(manifestations)+1
    name = ''
    status = ''
    while len(name.split()) == 0:
        name = input('\nDigite o nome do requisitante: ')
    print('\n\nSelecione uma opção: \nReclamação: 1\nSugestão: 2\nElogio: 3\n\n')
    while not status in list(range(1,4)):
        try:
            status = int(input('Digite o tipo da manifestação: '))
        except:
            print('\nDigite um numero inteiro.')
    description = input('Digite a descrição: ')
    manifestation = Manifestation(id, description, status, name)
    manifestations.append(manifestation)

def find_one_manifestation(manifestations):
    while True:
        try:
            id = int(input('\n\nDigite o codigo do protocolo: '))
        except:
            print('\nDigite um numero inteiro.')
        break
    print('\nBuscando protocolo..')
    count = 0
    for manifestations in manifestations:
        if id == manifestations.id:
            print('Protocolo encontrado!\n')
            print(manifestations)
            count = 1
    if count == 0:
        print('\nProtocolo não encontrado.')

def exit_system(manifestations=None):
    raise SystemDone()
