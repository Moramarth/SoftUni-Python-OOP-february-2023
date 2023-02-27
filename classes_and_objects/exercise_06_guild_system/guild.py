from classes_and_objects.exercise_06_guild_system.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = list()

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        for member in self.players:
            if member.name == player_name:
                member.guild = "Unaffiliated"
                self.players.remove(member)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = [f"Guild: {self.name}"]
        for member in self.players:
            result.append(member.player_info())

        return "\n".join(result)
