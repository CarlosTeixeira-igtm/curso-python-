from random import randint  

print("###------------ Vamos jogar? ------------###")
min = 0
max = 100
random = randint(min,max)
chute = 0
chances = 10
                
while chute != random:
    chute = input(f'Chute um numero entre {min} a {max}: ')
    if chute.isnumeric():
            chute = int(chute)
            chances = chances - 1
            if chute == random:
                print('\o/ \o/ \o/ \o/ \o/')
                print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
                print('\o/ \o/ \o/ \o/ \o/')
                print('\o/ \o/ \o/ \o/ \o/')
                break
            else:
                print('')
                if chute > random:
                       print('Você errou!!! Dica é um número menor!')
                else:
                       print('Você errou!!! é um número maior!')
                print('Você ainda possui {} chances.'.format(chances))
                print('')
            if chances == 0:
                    print('')
                    print('Suas chances acabaram! Você perdeu!')
                    print('')
                    break
print("###------------ GAME OVER? ------------###")

            
        