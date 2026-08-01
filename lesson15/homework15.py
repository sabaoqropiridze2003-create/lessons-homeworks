class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

# პირველი ამოცანა
    def add_player(self, name, position, number, age, nationality):

        for p in self.players:
            if p["number"] == number:
                print(f"number {number} is already taken!!")
                return

        player_dict = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }

        self.players.append(player_dict)
        print(f"{name} with number {number} was added sucsesfully")


# მეორე ამოცანა

    def remove_player(self, number):
        for p in self.players:
            if p["number"] == number:
                self.players.remove(p)
                print(f"player with number {number} was deleted sucsesfully")
                return
        print(f"player with number {number} was not found")

# მესამე ამოცანა
    def update_player_info(self, number, **kwargs):
        for p in self.players:
            if p["number"] == number:
                for key, value in kwargs.items():
                    p[key] = value
                print(
                    f"information of the player with number {number} was updated")
                return
        print(f"player with number {number} was not found")
# მეოთხე ამოცანა

    def team_info(self):
        print("---club information---")
        print(f"club name: {self.team_name}")
        print(f"club coach: {self.coach}")
        print("---list of players---")
        if not self.players:
            print("there is no players in this club")
        for p in self.players:
            print(f"number {p["number"]}: {p["name"]}")

# მეხუთე ამოცანა
    def player_info(self, number):
        for p in self.players:
            if p["number"] == number:
                print("---player information---")
                for key, value in p.items():
                    print(f"{key}: {value}")
                return
        print(f"player with number {number} does not exist")


my_team = FootballTeam("Real Madrid", "Carlo Ancelotti")


my_team = FootballTeam("FC Barceloana", "Hansi flick")

my_team.add_player("messi", "forward", 10, 39, "argentinian")
my_team.add_player("kvaratxkhelia", "forward", 7, 25, "georgian")
my_team.add_player("haaland", "forward", 9, 25, "norwegian")


my_team.remove_player(9)

my_team.update_player_info(10, goals=918, asists=410)
my_team.update_player_info(7, UCL=2)


my_team.team_info()

my_team.player_info(10)
