import random
import sys


# setting range of lottery numbers to be drawn
white_ball = list(range(1, 99))



# player_num.split(',')
# player_list = [int(value.strip()) for value in player_num.split(',')]




def get_user_numbers():
    while True:
        player_num = input('Select numbers from 1 - 99 (comma-separated): ')

        if player_num.strip() == 'q':
            sys.exit()

        player_list = []
        try:
            for value in player_num.split(','):
                num = int(value.strip())
                if num == 0:
                    print('Zero is included in your number')
                    sys.exit()
                elif 1 <= num <= 99:
                    player_list.append(num)
                else:
                    print('Invalid number. Please select numbers from 1 to 99.')
                    continue

            if len(player_list) <= 5:
                return player_list
            else:
                print('Please select exactly 5 numbers.')
        except ValueError:
            print('Invalid Input')




class Compare_Balls:
    def __int__(self, my_own, comp_own) -> None:
        self.my_own = my_own
        self.comp_own = comp_own

    def draw_values(self, my_own, comp_own):
        self.checking_balls = len(my_own.intersection(comp_own))
        return f"Your numbers are: {my_own}, Drawn Numbers are: {comp_own}, Matching numbers: {self.checking_balls}"
    
    def ticket_status(self):
        self.amt= 0
        if self.checking_balls == 5:
            self.amt += 20_000_000
        elif self.checking_balls == 4:
            self.amt += 1_000_000
        elif self.checking_balls == 3:
            self.amt += 40,000
        elif self.checking_balls == 2:
            self.amt += 2_000
        elif self.checking_balls == 1:
            self.amt += 1000
        else:
            self.amt += 0
    

        return f"You have won N{self.amt}"


# computer draws
comp_balls = set(random.sample(white_ball, k=5))

# players number
my_balls = set(get_user_numbers())

if __name__ == '__main__':
    ticket_winnings=Compare_Balls()
    earning = ticket_winnings.draw_values(my_balls, comp_balls)
    tix = ticket_winnings.ticket_status()
    print(earning)
    print(tix)
   


    