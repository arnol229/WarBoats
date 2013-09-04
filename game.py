from random import shuffle

class Game(object): # Create a game. save these objects to pull up a match history?

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.winner = self.battle(player1, player2)
    
    def battle(self, player1, player2): #the stage for fighting. scroll through firing, assessing dmg, using power
        player_list=[player1, player2]
        shuffle(player_list)
        print "Player {} Will fire first, Player {} will fire second.".format(player_list[0].id, player_list[1].id)
        while not self.winner:
            for player in player_list:
                player.refresh_ships() # put ships off cooldown in my_ships

            self.exchange(player_list)# player 1 firing at player 2
            player_list.reverse()
            self.exchange(player_list)# player 2 firing at player 1
            for player in player_list:
                self.winner = self.check_winner(player)
        print "We have a winner! Congrats Player: {}".format(self.winner)
        return self.winner

    def exchange(self, players): #how to design firing? ships have multiple cannons?
        pos = 0
        complete = False
        shuffle(players[0].my_ships)
        while complete is False:
            if type(players[0].my_ships[pos]) is not list:# makes sure to skip over cooldown list in my_ships
                firecount = players[0].my_ships[pos].cannons
                while firecount is not 0:
                    print "player{}:".format(players[0].id)
                    x,y = players[0].my_ships[pos].fire()
                    self.assess_shot(players[1], x,y)#pass the other players my_ships and x,y of fire()
                    firecount -= 1
                players[0].cooldown.append(players[0].my_ships.pop(pos))
                complete = True
            else:
                pos +=1
        print "Player{} board:".format(players[0].id)
        players[1].my_board.print_board()

    def check_winner(self, player):
        for boat in player.my_ships:
            if type(boat) is list:
                for cdboat in boat:
                    if cdboat.is_dead:
                        continue
                    else:
                        return None
            if type(boat) is object:
                if boat.is_dead():
                    continue
                else:
                    return None
        #return player.id

    def assess_shot(self,player,x,y):
        for boat in player.my_ships:# check both my_ships and cooldown for hits in boat.points
            if type(boat) is list: # if its cooldown list, check the boats in there
                for cdboat in boat:
                    if cdboat.check_point(x,y):
                        player.my_board.board[x][y] = "X"
                        cdboat.kill_point(x,y)
                    else:
                        continue
            elif type(boat) is object:# if its a boat, check it
                if boat.check_point(x,y):
                    player.my_board.board[x][y] = "X"
                    boat.kill_point(x,y)
                else:
                    continue
            #else:# if theres nothing to check, its a miss.
            #    player.my_board.board[x][y] = "~"


    #def check_boat(self, boat):#same as is_alive on the boat? dont think i need...

    # firing idea:
    # each player scroll through and fire with a type of ship (d, then c, then wb) wb have 2 cannons?