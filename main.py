from hangman import Game;

if __name__ == '__main__':
    player = Game()
    flag="lose"
    visited={}
    player.convertToString()
    while player.isMoveRemaining():
        m=input("Guess the Character: ")
        while m in visited:
            print("Already choosen!! Try Again")
            m=input("Guess the Character: ")
        visited[m]=1
        if player.validateCharacter(m):
            player.markPosition(m)
            player.convertToString()
        else:
            player.decrementMmove()
            print(f"{player.getMove()} Chance remaining")
        if player.isWinner():
            print("\nYou won. Hurray")
            flag="won"
            break
    if flag!="won":
        print("You Lose!! Try Again")
        player.showAnswer()