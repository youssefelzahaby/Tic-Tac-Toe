class Player :
   def __init__(self):
       self.name=""
       self.symbol=""

   #function to choose name

   def choose_name (self):
       while True :
           name = input(" enter name (letter ) ")
           if name.isalpha():
               self.name=name
               break
           else: #====> error resat
            print("invalid name please enter (letter only )")

   #function to choose symbol

   def symbol_choose (self):
       while True:
           symbol=input(f"{self.name} please choose ( X OR O )")
           if symbol.isalpha() and len(symbol)==1 :
            self.symbol=symbol.upper()
            break
           else:
               print("please choose one letter only ")
class Menu:
    def disblay_main_menu(self):
        print("welcome ya 7alwen  ")
        print("1-start game ")
        print("2-quit game ")
        choice= input("enter your choice (1 or 2 )")
        return choice
    def display_end_menu(self):
        menu_text=""" game end 
        1- Resat game 
        2- Quit game 
        enter your choice 
        """
        choice=input(menu_text)
        return choice
class Board:
    def __init__(self):
        # إنشاء لوحة الأرقام 1-9
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        # عرض اللوحة بشكل منظم
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))  # طباعة صفوف اللوحة
            if i < 6:
                print("-" * 5)  # طباعة الخط الفاصل بين الصفوف

    def update_board(self, choice, symbol):
        # تحديث اللوحة إذا كانت الحركة صحيحة
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol  # وضع الرمز في المكان المناسب
            return True
        else:
            return False

    def is_valid_move(self, choice):
        # التحقق من أن المكان المحدد متاح
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        # إعادة ضبط اللوحة إلى الوضع الأولي
        self.board = [str(i) for i in range(1, 10)]

class Game:
    def __init__(self):
        self.players=[Player(),Player ()]
        self.board=Board()
        self.menu=Menu()
        self.current_player_index=0

    def start_game (self):
        choice= self.menu.disblay_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    def setup_players(self):
        for  number , player in enumerate( self.players , start=1  ):
            print(f"player {number}, enter your details ")
            player.choose_name()
            player.symbol_choose()
            # clear_screen()
            print("-"*20)
    def play_game (self):
        while True:
            self.play_turn()
            if self.check_win () or self.check_draw():
                choice=self.menu.display_end_menu()
                if choice=="1":
                 self.resat_game()
            else:
                self.quit_game()


    def switch_player(self):
        self.current_player_index=1-self.current_player_index

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name} turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choose a cell (1-9)"))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break  # الخروج من الحلقة إذا كانت الحركة صالحة
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

        # التبديل بين اللاعبين بعد الخروج من الحلقة
        self.switch_player()

    def check_win(self):
        WIN_CONDITIONS = [
            [0, 1, 2],  # الصف الأول
            [3, 4, 5],  # الصف الثاني
            [6, 7, 8],  # الصف الثالث
            [0, 3, 6],  # العمود الأول
            [1, 4, 7],  # العمود الثاني
            [2, 5, 8],  # العمود الثالث
            [0, 4, 8],  # القطر الرئيسي
            [2, 4, 6]  # القطر العكسي
        ]
        for combo in WIN_CONDITIONS:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all (not cell.isdigit() for cell in self.board.board)
    def resat_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()

    def quit_game (self):
        print("think you for playing ")


game= Game()
game.start_game()
