class ICC:
    def __init__(self, events, teamboards, year):
        self.events = events
        self.teamboards = teamboards
        self.year = year
        self.winning_trophy = False

    def start(self):
        if not self.winning_trophy:
            self.winning_trophy = True
            return ("The team won the championship.", self.year, self.events, self.teamboards)
        else:
            return ("The team didn't won the championship.", self.year, self.events, self.teamboards)

    def stop(self):
        if self.winning_trophy:
            self.winning_trophy = False
            return ("The team is not playing.", self.year, self.events, self.teamboards)
        else:
            return ("The team is already playing.", self.year, self.events, self.teamboards)

class players(ICC):
    def __init__(self, events, teamboards, year, player_name):
        super().__init__(events, teamboards, year)
        self.player_name = player_name

new_player = players("T_20", "BCCI", 2007, "dohni")
print(new_player.start())
print(new_player.stop())
print("player is playing in the event.", new_player.player_name)

#Multiple Inheritance

class player_runs:
    def __init__(self, runs):
        self.runs = runs

    def charge(self):
        return ("dhoni scored a centuary in the event")

class details_player(players, player_runs):
    def __init__(self, events, teamboards, year, player_name, runs):
        players.__init__(self, events, teamboards, year, player_name)
        player_runs.__init__(self, runs)


details_player = details_player("T_20", "BCCI", 2007, "dohni",100)
print(details_player.start())
print(details_player.charge())


#Mutilevel Inheritance
class coplayers(players):
    def __init__(self,events, teamboards, year, player_name, co_players):
        super().__init__(events, teamboards, year, player_name)
        self.co_players = co_players

coplayers = coplayers("T_20", "BCCI", 2007, "dohni", ["Rohit sharma", "Virakt Kohli"])
print(coplayers.start())
print(f"the match has the following costarts: {', '.join(coplayers.co_players)}")