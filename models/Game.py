from random import randrange
class Game:
    def __init__(self, name: str, file="palavras.txt", won=False, lost = False, words=[], public_word="", tries=7,chosen_word=""):
        self.name = name
        self.file = file
        self.won = won
        self.lost = lost
        self.words = words
        self.public_word = public_word
        self.tries = tries
        self.chosen_word = chosen_word
    def show_name(self):
        print(
            "\n\n*****************************************\n"
            "*                                       *\n"
            f"*       Bem vindo ao {self.name}      *\n"
            "*                                       *\n"
            "*****************************************\n"
        )
    def conf_temp_list(self):
        file = open(self.file, "r")
        for index, i in enumerate(file):
            self.words.append(i.strip())
        self.chosen_word = self.words[randrange(index)]
        for i in self.chosen_word:
            self.public_word += "*"
        print("PALAVRA SECRETA: ", self.public_word)
        temp_list = ["*" for i in self.chosen_word]
        return temp_list
    def play(self):
        self.show_name()
        temp_list = self.conf_temp_list()
        new_str = ''
        '''
        OBS - já que a string não pode mudar, tem que criar uma lista, editar
        e reconverter pra string
        '''
        # Game loop
        while (not self.lost and  not self.won):
            guess = input("Digite a letra que você quer chutar: ")
            guess = guess.strip()
            if self.tries == 0:
                self.lost = True
                print("Perdeu!")
            for index,i in enumerate(self.chosen_word):
                    if guess.upper() == i.upper() and self.tries >= 1:
                        temp_list[index] = i
                        new_str = ''.join(temp_list)
            if self.chosen_word.find(guess) >= 0 and self.tries >= 1:
                print(new_str, "TENTATIVAS: ", self.tries)
                if new_str.find("*") == -1 and self.tries >= 1:
                    self.won = True
                    print("Venceu!")
            elif self.chosen_word.find(guess) == -1 and self.tries >= 1:
                self.tries -= 1
                print("TENTATIVAS: ", self.tries)

        print("Fim do jogo")
