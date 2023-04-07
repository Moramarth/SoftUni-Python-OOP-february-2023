class Controller:
    def __init__(self):
        self.players = list()
        self.supplies = list()

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    def add_player(self, *players):
        added_player_names = list()
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_player_names.append(player.name)

        return f"Successfully added: {', '.join(added_player_names)}"

    def add_supply(self, *supplies):
        self.supplies.extend(list(supplies))

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.attribute_collection_search(player_name, "name", self.players)
        if not player:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food":
            if not any(food.__class__.__name__ == "Food" for food in self.supplies):
                raise Exception("There are no food supplies left!")

        elif sustenance_type == "Drink":
            if not any(drink.__class__.__name__ == "Drink" for drink in self.supplies):
                raise Exception("There are no drink supplies left!")
        else:
            return

        supply_to_use = None

        for i in range(len(self.supplies) - 1, -1, -1):
            if sustenance_type == self.supplies[i].__class__.__name__:
                supply_to_use = self.supplies.pop(i)
                break

        if player.stamina + supply_to_use.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply_to_use.energy

        return f"{player_name} sustained successfully with {supply_to_use.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = self.attribute_collection_search(first_player_name, "name", self.players)
        player_two = self.attribute_collection_search(second_player_name, "name", self.players)
        duel_cannot_start = []
        if player_one.stamina == 0:
            duel_cannot_start.append(f"Player {first_player_name} does not have enough stamina.")

        if player_two.stamina == 0:
            duel_cannot_start.append(f"Player {second_player_name} does not have enough stamina.")

        if duel_cannot_start:
            return "\n".join(duel_cannot_start)

        if player_one.stamina < player_two.stamina:
            player_two.stamina -= player_one.stamina / 2
            if player_one.stamina - player_two.stamina / 2 <= 0:
                player_one.stamina = 0
                return f"Winner: {player_two.name}"
            player_one.stamina -= player_two.stamina / 2
        else:
            player_one.stamina -= player_two.stamina / 2
            if player_two.stamina - player_one.stamina / 2 <= 0:
                player_two.stamina = 0
                return f"Winner: {player_one.name}"
            player_two.stamina -= player_one.stamina / 2

        if player_one.stamina > player_two.stamina:
            return f"Winner: {player_one.name}"

        return f"Winner: {player_two.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        output = list()
        output.extend([str(player) for player in self.players])
        output.extend([supply.details() for supply in self.supplies])
        return "\n".join(output)
