def play_the_game():
    print(
        "\n\n*****************************************\n"
        "*                                       *\n"
        "*       Bem vindo ao jogo da forca      *\n"
        "*                                       *\n"
        "*****************************************\n"
    )
    chosen_word = "banana"
    public_word = ""
    tries = 7
    for i in chosen_word:
        public_word += "*"
    lost_the_game = False
    won = False
    print("PALAVRA SECRETA: ", public_word)
    temp_list = list(public_word)
    new_str = ''
    '''
    OBS - já que a string não pode mudar, tem que criar uma lista, editar
    e reconverter pra string
    '''
    # Game loop
    while (not lost_the_game and  not won):
        guess = input("Digite a letra que você quer chutar: ")
        if tries == 1:
            lost_the_game = True
            print("Perdeu!")
        for index,i in enumerate(chosen_word):
                if guess == i and tries >= 1:
                    temp_list[index] = i
                    new_str = ''.join(temp_list)
        if chosen_word.find(guess) >= 0 and tries >= 1:
            print(new_str, "TENTATIVAS: ", tries)
            if new_str.find("*") == -1 and tries >= 1:
                won = True
                print("Venceu!")
        elif chosen_word.find(guess) == -1 and tries >= 1:
            tries -= 1
            print("TENTATIVAS: ", tries)

    print("Fim do jogo")


if(__name__ == "__main__"):
    play_the_game()
