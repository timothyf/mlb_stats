import pandas as pd

from mlb_data_lab.apis.data_fetcher import DataFetcher
from mlb_data_lab.apis.mlb_stats_client import MlbStatsClient
from mlb_data_lab.apis.pybaseball_client import PybaseballClient
from mlb_data_lab.apis.fangraphs_client import FangraphsClient


class UnifiedDataClient:

    def __init__(self):
        pass

    ################
    # Batting Stats
    ################
    def fetch_batting_splits_leaderboards(self, player_bbref: str, season: int) -> pd.DataFrame:
        return PybaseballClient.fetch_batting_splits_leaderboards(player_bbref, season)

    def fetch_fangraphs_batter_data(self, player_name: str, team_fangraphs_id: str, start_year: int, end_year: int):
        return PybaseballClient.fetch_fangraphs_batter_data(player_name, team_fangraphs_id, start_year, end_year)

    def fetch_statcast_batter_data(self, player_id: int, start_date: str, end_date: str):
        return PybaseballClient.fetch_statcast_batter_data(player_id, start_date, end_date)

    def fetch_team_batting_stats(self, team_abbrev: str, start_year: int, end_year: int):
        return PybaseballClient.fetch_team_batting_stats(team_abbrev, start_year, end_year)

    def save_statcast_batter_data(self, player_id: int, year: int, file_path: str = None):
        return PybaseballClient.save_statcast_batter_data(player_id, year, file_path)

    ################
    # Pitching Stats
    ################
    def fetch_fangraphs_pitcher_data(self, player_name: str, team_fangraphs_id: str, start_year: int, end_year: int):
        return PybaseballClient.fetch_fangraphs_pitcher_data(player_name, team_fangraphs_id, start_year, end_year)

    def fetch_pitching_splits_leaderboards(self, player_bbref: str, season: int) -> pd.DataFrame:
        return PybaseballClient.fetch_pitching_splits_leaderboards(player_bbref, season)

    def fetch_statcast_pitcher_data(self, pitcher_id: int, start_date: str, end_date: str):
        return PybaseballClient.fetch_statcast_pitcher_data(pitcher_id, start_date, end_date)

    def fetch_team_pitching_stats(self, team_abbrev: str, start_year: int, end_year: int):
        return PybaseballClient.fetch_team_pitching_stats(team_abbrev, start_year, end_year)

    def save_statcast_pitcher_data(self, player_id: int, year: int, file_path: str = None):
        return PybaseballClient.save_statcast_pitcher_data(player_id, year, file_path)

    #######################
    # Team and Player Info
    #######################

    def fetch_team_schedule_and_record(self, team_abbrev: str, season: int):
        return PybaseballClient.fetch_team_schedule_and_record(team_abbrev, season)

    def lookup_player(self, last_name: str, first_name: str, fuzzy: bool = False):
        return PybaseballClient.lookup_player(last_name, first_name, fuzzy)

    def lookup_player_by_id(self, player_id: int):
        return PybaseballClient.lookup_player_by_id(player_id)
    
    def playerid_reverse_lookup(player_id, key_type='mlbam'):
        return PybaseballClient.playerid_reverse_lookup([player_id], key_type='mlbam')

