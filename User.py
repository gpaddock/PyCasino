# Tracks the human player

class User:

    def __init__(self, name, guppyBucks):
        self.n = name
        self.gB = guppyBucks
        self.initialAmount = guppyBucks
        self.totalWinnings = 0

    def bet(self, betAmount) -> int:
        if (input(f"Confirm bet of GB${betAmount}? (Y/N)") == "Y"):
            if (self.gB - betAmount >= 0):
                self.gB -= betAmount
                print(f"{self.name} bet GB${betAmount}.")
                return 1
            else:
                print("Bet invalid (Too large!).")
                return 0
        else:
            print("Bet unconfirmed.")
            return 0
        
    def payout(self, bet, winnings) -> int:
        print(f"{self.n} won GB${winnings} from a GB${bet} bet!")
        self.gB += winnings
        print(f"New balance of GB${self.gB}")
        self.totalWinnings += winnings
