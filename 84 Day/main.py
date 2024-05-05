#%%
FIELDS_FULL = r"""

     _    _ _    __ _      _     _                         __ _ _ _          _ _           ____          _             _     _   _             ____                      
    / \  | | |  / _(_) ___| | __| |___    __ _ _ __ ___   / _(_| | | ___  __| | |         |  _ \ ___ ___| |_ __ _ _ __| |_  | |_| |__   ___   / ___| __ _ _ __ ___   ___ 
   / _ \ | | | | |_| |/ _ | |/ _` / __|  / _` | '__/ _ \ | |_| | | |/ _ \/ _` | |  _____  | |_) / _ / __| __/ _` | '__| __| | __| '_ \ / _ \ | |  _ / _` | '_ ` _ \ / _ \
  / ___ \| | | |  _| |  __| | (_| \__ \ | (_| | | |  __/ |  _| | | |  __| (_| |_| |_____| |  _ |  __\__ | || (_| | |  | |_  | |_| | | |  __/ | |_| | (_| | | | | | |  __/
 /_/   \_|_|_| |_| |_|\___|_|\__,_|___/  \__,_|_|  \___| |_| |_|_|_|\___|\__,_(_)         |_| \_\___|___/\__\__,_|_|   \__|  \__|_| |_|\___|  \____|\__,_|_| |_| |_|\___|                                                                                                                                                                         

"""

WINNER_X = r"""

  _____ _           __        ___                         _      __  ___ 
 |_   _| |__   ___  \ \      / (_)_ __  _ __   ___ _ __  (_)___  \ \/ / |
   | | | '_ \ / _ \  \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | / __|  \  /| |
   | | | | | |  __/   \ V  V / | | | | | | | |  __/ |    | \__ \  /  \|_|
   |_| |_| |_|\___|    \_/\_/  |_|_| |_|_| |_|\___|_|    |_|___/ /_/\_(_)                                                                     

"""

WINNER_O = r"""

  _____ _           __        ___                         _        ___  _ 
 |_   _| |__   ___  \ \      / (_)_ __  _ __   ___ _ __  (_)___   / _ \| |
   | | | '_ \ / _ \  \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | / __| | | | | |
   | | | | | |  __/   \ V  V / | | | | | | | |  __/ |    | \__ \ | |_| |_|
   |_| |_| |_|\___|    \_/\_/  |_|_| |_|_| |_|\___|_|    |_|___/  \___/(_)
                                                                        
"""

from random import randint
import numpy as np

class TicTacToe():
    def __init__(self) -> None:
        """
        Initiate TicTacToe Fields
        - 6 Fields
        - Start X or O is random
        """
        self.start = randint(0,1)
        if self.start == 0: print("X is starting\n")
        else: print("O is starting\n")

        self.create_array = None

    def initiate_fields(self):
        """
        Get the middle of the array, then print around the fields.
        - Length has to be odd
        """
        # self.create_array = np.array([str(val) for val in range(0,9)]).reshape(3,3).astype(object)
        self.create_array = np.array([" " for val in range(0,9)]).reshape(3,3).astype(object)


        self.x_index = int(len(self.create_array) / 2)
        self.y_index = self.x_index

        # print(f"Field in the middle: {self.x_index, self.y_index}")

            
    def create_fields(self):
        """
        - Create grid around the center
        """
        for row_index in range(self.create_array.shape[0]):
            for col_index in range(self.create_array.shape[1]):
                if row_index == self.x_index and col_index == self.y_index:
                    self.logic_insert_around_middle(x_index=self.x_index, y_index=self.y_index)


        self.print_fields()

    def logic_insert_around_middle(self, x_index, y_index):
        """
        Insert left side for all elements before and after.
        
        col_index stays the same.
        """
        copy_array = np.copy(self.create_array)

        for index_of_row_elements in range(self.create_array.shape[0]):
            copied_value = copy_array[index_of_row_elements, y_index]
            self.create_array[index_of_row_elements, y_index] = " │ " + copied_value + " │ "

    def print_fields(self):
        print_arr = np.copy(self.create_array)

        for row in range(print_arr.shape[0]):
            current_row = ""
            # Special case for middle (upper)
            if row == self.x_index:
                print("━━━"*print_arr.shape[1])

            # Print logic 
            for col in range(print_arr.shape[1]):
                current_row += print_arr[row,col]
            print(current_row)

            # Special case for middle (lower)
            if row == self.x_index:
                print("━━━"*print_arr.shape[1])
 


    def print_current_turn(self):

        if self.start == 0:
            # X start
            print(f"\nIt's X turn.\n Which field you want to pick? (row, col) / {self.create_array.shape}\n")
        elif self.start == 1:
            print(f"\nIt's O turn.\n Which field you want to pick? (row, col) / {self.create_array.shape}\n")
                
    def start_tictactoe(self):
        self.print_current_turn()
        
        print("--- Exit with q\n"),

        quit = False
        while quit == False:
            try:
                self.row_pick = input("\nRow: ")
                if self.row_pick == "q": quit = True; print("\nEnd game."); break

                self.col_pick = input("Col: ")
                if self.col_pick == "q": quit = True; print("\nEnd game."); break
                    
                self.row_pick = int(self.row_pick)-1
                self.col_pick = int(self.col_pick)-1

                if self.row_pick < 0 or self.col_pick < 0:
                    print("Please pick a row/col which is > 0")
                    raise Exception

                # Check if field is already filled or field exists
                try: 
                    picked_field = self.create_array[self.row_pick, self.col_pick]
                    picked_field = (self.row_pick, self.col_pick)
                except Exception as e:
                    print("Field does not exists!")
                
                try: 
                    picked_field = self.create_array[self.row_pick, self.col_pick]
                    if "O" in picked_field or "X" in picked_field:
                        raise Exception
                    else:
                        print(f"Field with row {self.row_pick} and col {self.col_pick} will be filled. \n")
                        self.fill_field(x_pick=self.row_pick, y_pick=self.col_pick)

                except Exception as e:
                    print("Field is already filled!")
            except Exception as e:
                print(e)

    
    def check_winner(self,x_pick, y_pick, current_player):
        """
        Check the current picked field if there are any fields which are three
        in a row.
        - current_player is 0, then X (Check for triple X)
        - current_player is 1, then 0 (Check for triple O)

        Check if there is an other filled field around the picked/current one

        Returns True if winner is found.
        """
        # all possible fields around
        fields_around = [   (x_pick-1,y_pick-1),  (x_pick-1,y_pick), (x_pick-1, y_pick+1),
                            (x_pick, y_pick-1),                      (x_pick, y_pick+1),
                            (x_pick+1, y_pick-1), (x_pick+1, y_pick),(x_pick+1, y_pick+1)]

        if current_player == 0:
            for field in fields_around:
                try:
                    # Find X around
                    x_coord = field[0]
                    y_coord = field[1]
                    if "X" in self.create_array[x_coord, y_coord] and x_coord >= 0 and y_coord >= 0:
                        # If x founded, check further fields
                        # Difference to nearest field is always 1
                        difference_to_go = x_coord - x_pick, y_coord - y_pick

                        third_X = x_coord + difference_to_go[0], y_coord + difference_to_go[1]

                        if "X" in self.create_array[x_pick,y_pick] and "X" in self.create_array[x_coord, y_coord] and "X" in self.create_array[third_X[0], third_X[1]]:
                            print(WINNER_X)
                            return True
                except:
                    # print("No fields found with X around!")
                    pass

        elif current_player == 1:
            for field in fields_around:
                try:
                    # Find X around
                    x_coord = field[0]
                    y_coord = field[1]
                    if "O" in self.create_array[x_coord, y_coord] and x_coord >= 0 and y_coord >= 0:
                        # If x founded, check further fields
                        # Difference to nearest field is always 1
                        difference_to_go = x_coord - x_pick, y_coord - y_pick

                        third_O = x_coord + difference_to_go[0], y_coord + difference_to_go[1]

                        if "O" in self.create_array[x_pick,y_pick] and "O" in self.create_array[x_coord, y_coord] and "O" in self.create_array[third_O[0], third_O[1]]:
                            print(WINNER_O)
                            return True
                except:
                    # print("No fields found with X around!")
                    pass



        return False
    
    def check_all_fields_filled(self):
        """
        Returns True if all fields filled. Game restarts.
        """
        count_X = lambda x: sum(1 for row in x for entry in row if "X" in entry)
        count_O = lambda x: sum(1 for row in x for entry in row if "O" in entry)

        # print("X counts:", count_X(self.create_array))
        # print("O counts:", count_O(self.create_array))

        x_counts_sum = count_X(self.create_array)
        o_counts_sum = count_O(self.create_array)
        # print(x_counts_sum, o_counts_sum)

        if x_counts_sum + o_counts_sum >= 9:
            print("\n"+FIELDS_FULL+"\n")
            return True
        else:
            return False

    def fill_field(self, x_pick, y_pick):
        """
        After field is correctly picked, fill the field.
        """

        count_spaces = lambda x: sum(1 for char in x if char == " ")
        current_player = self.start

        if self.start == 0:
            if count_spaces(self.create_array[x_pick, y_pick]) > 1:
                self.create_array[x_pick, y_pick] =  " │ " + "X" + " │ "

            else:
                self.create_array[x_pick, y_pick] = self.create_array[x_pick, y_pick].replace(" ","X")
            self.start = 1

        elif self.start == 1:
            if count_spaces(self.create_array[x_pick, y_pick]) > 1:
                self.create_array[x_pick, y_pick] =  " │ " + "O" + " │ "


            else:
                self.create_array[x_pick, y_pick] = self.create_array[x_pick, y_pick].replace(" ","O")
            self.start = 0

        if self.check_winner(x_pick, y_pick, current_player=current_player) == True:
            self.initiate_fields()
            self.create_fields()
            self.print_current_turn()
        elif self.check_all_fields_filled() == True:
            self.initiate_fields()
            self.create_fields()
            self.print_current_turn()
        else:
            self.print_current_turn()
            self.print_fields()




                    











if __name__ == "__main__" :
    game = TicTacToe()
    game.initiate_fields()
    game.create_fields()
    game.start_tictactoe()



# %%
