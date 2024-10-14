from mlb_summary_sheets.team import Team
from mlb_summary_sheets.apis.mlb_stats_client import MlbStatsClient
import re

class Roster:
    def __init__(self):
        # Initialize self.players as an empty list
        self.players = []

    def add_players(self, players):
        """Add players to the self.players list"""
        if isinstance(players, list):
            self.players.extend(players)  # Add each player in the list to self.players
        else:
            raise ValueError("players should be a list")


    @staticmethod
    def get_active_roster(team_id: int = None, team_name: str = None, year: int = 2024):
        if team_id:
            roster = MlbStatsClient.fetch_active_roster(team_id=team_id, year=year)
        elif team_name:
            roster = MlbStatsClient.fetch_active_roster(team_name=team_name, year=year)

        print(f"Roster: {roster}")

        # Updated regular expression to handle middle initials, suffixes, and other name variations
       # player_names = re.findall(r'\d+\s+[A-Z0-9]+\s+([A-Za-z\w\s\-\.\']+(?:\s(Jr\.|Sr\.|II|III|IV|V)?)?)', roster)
       # player_names = re.findall(r'\s{2,}[A-Za-z\s\'\.\-]+(?:\s(Jr\.|Sr\.|II|III|IV|V)?)', roster)
       # player_names = re.findall(r'#?\s*[A-Z]+\s+([A-Za-z\'\.\-\s]+(?:\s(Jr\.|Sr\.|II|III|IV|V)?)?)', roster)
        player_names = re.findall(r'#?\s*[A-Z]+\s+([A-Za-zÁÉÍÓÚáéíóúñÑ\'\.\-\s]+(?:\s(Jr\.|Sr\.|II|III|IV|V)?)?)', roster)




        print(f"Player names: {player_names}")

        # Extract only the first element (full name) from each tuple and strip whitespace
        return [name[0].strip() for name in player_names]

# Compare this snippet from mlb_summary_sheets/team.py:
