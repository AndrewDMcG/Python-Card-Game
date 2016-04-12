players = [player1,player2,player3,player4]

for player in players:
    if player.VP >= 15: win(player)
    res_take()
    res_use()
    player.VP += scoring()date(self, *args, **kwargs):
        pass

class Player(object):
    def __init__(self,name):
        self.name = name
        self.VP = 0
        self.AP = 2

class Game(object):
    def __init__(self,players):
        self.players = players # a list of players
        self.running = False
    def win(self,player):
        print("{} wins!".format(player.name))
    def run(self):
        self.running = True
        while self.running:
            for player in self.players:
                player.VP += VP()
                if player.VP >= 15:
                    self.running = False
                    win(player)
