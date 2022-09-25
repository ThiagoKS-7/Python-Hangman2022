from models.Game import Game

def play_the_game():
    game = Game(name="Jogo da Forca")
    return game.play()



if(__name__ == "__main__"):
    play_the_game()
