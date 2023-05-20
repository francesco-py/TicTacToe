import random


class TicTacToe:
    def __init__(self):
        self.player_class = self.Player
        self.grid = self.Grid()
        players = self.define_players()
        self.player1 = players["player1"]
        self.player2 = players["player2"]




    def define_players(self):
        self.not_ok = True
        self.not_sign_ok = True
        while self.not_ok:
            type_of_game = input("Do You Want to play multiplayer or singleplayer? type 'm' or 's': ")
            if type_of_game == "s":
                self.not_ok = False
                while self.not_sign_ok:
                    sign = input("What kind of sign do you want to play with? type 'o' or 'x': ")
                    if sign not in self.grid.signs:
                        print("sign not valid")
                    else:
                        self.not_sign_ok = False
                        player1 = self.player_class("player",sign)
                        self.grid.signs.remove(sign)
                        player2 = self.player_class("ai", self.grid.signs[0])
                        self.grid.signs.remove(self.grid.signs[0])
                        return {"player1": player1, "player2": player2}
            elif type_of_game == "m":
                self.not_ok = False
                player1 = self.player_class("player", random.choice(self.grid.signs))
                self.grid.signs.remove(player1.sign)
                player2 = self.player_class("player", self.grid.signs[0])
                self.grid.signs.remove(self.grid.signs[0])
                return {"player1": player1, "player2": player2}




    def start_game(self):
        game_on = True
        while game_on:
            if self.player2.check_win(self.grid) == True:
                print("Player 2 won")
                game_on = False
            else:
                if self.player1.make_move(self.grid) == True:
                    game_on = False
            if self.player1.check_win(self.grid) == True:
                print("Player 1 won")
                game_on = False
            else:
                if self.player2.make_move(self.grid) == True:
                    game_on = False
        print("Game ended")
        another = input("Do you want to play another game? type 'y' or 'n': ")
        if another == "y":
            self.grid = self.Grid()
            players = self.define_players()
            self.player1 = players["player1"]
            self.player2 = players["player2"]
            return True
        else:
            print("Goodbye!")
            return False




    class Grid:
        def __init__(self):
            self.grid_signs = {
                1: "1",
                2: "2",
                3: "3",
                4: "4",
                5: "5",
                6: "6",
                7: "7",
                8: "8",
                9: "9",
            }
            self.possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.signs = ["o", "x"]




        def show_grid(self):
            grid = ["\n ", self.grid_signs[1], " | ", self.grid_signs[2], " | ", self.grid_signs[3], "\n ",
                         "- - - - - - -", "\n ", self.grid_signs[4], " | ", self.grid_signs[5], " | ",
                         self.grid_signs[6], "\n ", "- - - - - - -", "\n ", self.grid_signs[7], " | ",
                         self.grid_signs[8], " | ", self.grid_signs[9]]
            return grid




    class Player:
        def __init__(self, type, sign):
            self.type = type
            self.sign = sign




        def make_move(self, grid):
            ok = True
            while ok:
                if self.type == "player":
                    if len(grid.possible_moves) > 0:
                        print(*grid.show_grid())
                        move = input(f"Type the number of the square you want to place the {self.sign}: ")
                        try:
                            move = int(move)
                        except:
                            move = False
                        if move in grid.possible_moves and move != False:
                            grid.possible_moves.remove(move)
                            grid.grid_signs[move] = self.sign
                            ok = False
                        else:
                            print("invalid data")
                    else:
                        return True
                else:
                    if len(grid.possible_moves) > 0:
                        move = random.choice(grid.possible_moves)
                        grid.possible_moves.remove(move)
                        grid.grid_signs[move] = self.sign
                        ok = False
                    else:
                        return True




        def check_win(self, grid):
            combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
            for combination in combinations:
                if grid.grid_signs[combination[0]] == self.sign:
                    if grid.grid_signs[combination[1]] == self.sign:
                        if grid.grid_signs[combination[2]] == self.sign:
                            print(*grid.show_grid())
                            return True




tictactoe = TicTacToe()
on = True
while on:
    if tictactoe.start_game() == False:
        on = False
