import matplotlib.pyplot as plt
import pandas as pd
from mlb_summary_sheets.config import StatsConfig
from mlb_summary_sheets.apis.fangraphs_client import FangraphsClient
from mlb_summary_sheets.components.stats_table import StatsTable
from mlb_summary_sheets.player import Player
from mlb_summary_sheets.apis.pybaseball_client import PybaseballClient
from mlb_summary_sheets.apis.mlb_stats_client import MlbStatsClient


class StatsDisplay:
    def __init__(self, player: Player, season: int, stat_type: str):
        self.player = player
        self.season = season
        self.stat_type = stat_type
        self.standard_stats = StatsConfig().stat_lists[stat_type]['standard']
        self.advanced_stats = StatsConfig().stat_lists[stat_type]['advanced']
        self.splits_stats_list = StatsConfig().stat_lists[stat_type]['splits']
        if stat_type == 'batting':
            self.standard_stat_data = MlbStatsClient.fetch_player_stats(player.mlbam_id, season)
            self.advanced_stat_data = FangraphsClient.fetch_leaderboards(season=self.season, stat_type=self.stat_type)
            self.splits_stats = PybaseballClient.fetch_batting_splits_leaderboards(player_bbref=self.player.bbref_id, season=self.season)
        else:
            self.stats = FangraphsClient.fetch_leaderboards(season=self.season, stat_type=self.stat_type)
            self.splits_stats = PybaseballClient.fetch_pitching_splits_leaderboards(player_bbref=self.player.bbref_id, season=self.season)


    def display_standard_stats(self, ax: plt.Axes):

        if self.stat_type == 'batting':
            if self.standard_stat_data is None:
                return
            # Flatten the data
            flattened_data = []
            for entry in self.standard_stat_data:
                flattened_entry = entry['stat']  # Start with the stats
                flattened_entry['season'] = entry['season']
                #flattened_entry['team'] = entry['team']['name']
                flattened_entry['player'] = entry['player']['fullName']
                #flattened_entry['league'] = entry['league']['name']
                flattened_entry['gameType'] = entry['gameType']
                flattened_data.append(flattened_entry)

            # Convert to DataFrame
            df = pd.DataFrame(flattened_data)

            missing_columns = [col for col in self.standard_stats if col not in df.columns]
            if missing_columns:
                print(f"Warning: The following columns are missing from the DataFrame: {missing_columns}")
                # You can decide whether to raise an error, fill missing columns with default values, or skip processing
                # For example, you could skip missing columns:
                available_columns = [col for col in self.standard_stats if col in df.columns]
                if not available_columns:
                    print("No valid columns available for plotting.")
                    return

                # Only keep available columns
                df = df[available_columns].reset_index(drop=True)

            else:
                # If all columns are available, proceed as normal
                df = df[self.standard_stats].reset_index(drop=True)               

            df = df[self.standard_stats].reset_index(drop=True)
            df_player = df #self.stats[0]['stat'] #[self.standard_stats] # .reset_index(drop=True)
        else:
            if self.stats is None:
                return
            df_player = self.stats[self.stats['xMLBAMID'] == self.player.mlbam_id][self.standard_stats].reset_index(drop=True)
        
        stats_table = StatsTable(df_player, self.standard_stats, self.stat_type)
        stats_table.create_table(ax, "Standard {}".format(self.stat_type.capitalize()))

    def display_advanced_stats(self, ax: plt.Axes):
        if self.stat_type == 'batting':
            if self.advanced_stat_data is None:
                return
            stats = self.advanced_stat_data
        else:
            if self.stats is None:
                return
            stats = self.stats
        df_player = stats[stats['xMLBAMID'] == self.player.mlbam_id][self.advanced_stats].reset_index(drop=True)
        stats_table = StatsTable(df_player, self.advanced_stats, self.stat_type)
        stats_table.create_table(ax, "Advanced {}".format(self.stat_type.capitalize()))

    def display_splits_stats(self, ax: plt.Axes):
        if self.splits_stats is None:
            return
        stats_table = StatsTable(self.splits_stats, self.splits_stats_list, self.stat_type)
        stats_table.create_table(ax, "Splits {}".format(self.stat_type.capitalize()), True)
