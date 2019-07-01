#!/usr/bin/python
import os

import sys

argument = sys.argv[1]  # digite -help para ver a ajuda

HOME = os.environ['HOME']

animals = ['beavis.zen', 'bong', 'bud-frogs', 'bunny',
           'cheese', 'cower', 'daemon', 'default', 'dragon', 'dragon-and-cow',
           'elephant', 'elephant-in-snake', 'ghostbusters', 'head-in',
           'hellokitty', 'kiss', 'kitty', 'koala', 'kosh', 'luke-koala',
           'meow', 'milk', 'moofasa', 'moose', 'mutilated', 'ren',
           'satanic', 'sheep', 'skeleton', 'small', 'sodomized', 'stegosaurus',
           'stimpy', 'supermilker', 'surgery', 'telebears', 'three-eyes',
           'turkey', 'turtle', 'tux', 'udder', 'vader', 'vader-koala', 'www']


def install_cowsay():
    """Instala o pacote."""
    os.system('sboinstall cowsay')


def customize(cow_animals_file, cow_frases_file):
    """Customiza o cowsay."""
    os.system('mkdir ~/.cow')
    cow_animals = open(cow_animals_file, "a+")
    cow_frases = open(cow_frases_file, "a+")
    for i in range(len(animals)):
        cow_animals.write(animals[i] + '\n')

    custom = raw_input(
        'voce deseja colocar frases personalizadas? (y/n)\n')

    if custom == 'y':
        cow_frases = open(cow_frases_file, "a+")
        while (custom == 'y'):
            frase = raw_input('digite a frase desejada:\n')
            cow_frases.write(frase)
            custom = raw_input('deseja colocar mais uma frase? (y/n)\n')
            if custom == 'y':
                cow_frases.write('\n')
            else:
                break
        fortune = False
    else:
        fortune = True

    bash = open(HOME + '/.bashrc', "a+")
    bash.write('\n')
    bash.write('cowdir="/home/guilherme/.cow"\n')
    bash.write('animal=`shuf -n 1 ${cowdir}/animals`\n')

    if fortune is True:
        bash.write('fortune | cowsay -f $animal\n')

    else:
        bash.write('frases=`shuf -n 1 ${cowdir}/frases`\n')
        bash.write('cowsay -f $animal $frases\n')


if argument == '-install':
    if HOME == '/root':
        install_cowsay()
    else:
        os.system('echo voce precisa estar logado como root')

elif argument == '-custom':
    if HOME == '/root':
        os.system('echo voce nao pode estar logado como root para fazer isto')

    else:
        cow_animals_file = HOME + '/.cow/animals'
        cow_frases_file = HOME + '/.cow/frases'
        customize(cow_animals_file=cow_animals_file,
                  cow_frases_file=cow_frases_file)

elif argument == '-addfrases':
    if HOME != '/root':
        frases = open(HOME + '/.cow/frases', "a+")
        insert_frase = 'y'
        while(insert_frase == 'y'):
            frase = raw_input('digite sua frase:\n')
            frases.write(frase)
            insert_frase = raw_input('deseja adicionar outra frase? (y/n)')
            if insert_frase == 'y':
                frases.write('\n')
            else:
                break
    else:
        print('saia do root para fazer isso')

else:
    print('-custom para adicionar ao bashrc e adicionar frases')
    print('-addfrases para adicionar frases')
    print('-install para instalar o cowsay')
