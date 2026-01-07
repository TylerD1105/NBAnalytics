#define a function that will call nba-api with a parameter of Team-ID, and using Team-ID, grab the stats for the team, use TEAM_INFO_COMMON from API
from nba_api.stats.endpoints import TeamInfoCommon
def fetch_team_stats(team_id: str):
    '''
    Fetch team stats for NBA API for provided team_id.
    '''
    stats = TeamInfoCommon(league_id = "00",team_id=team_id)
    data = stats.get_data_frames()

    team_info = data[0]
    team_ranks = data[1]
    return {
        'wins': int(team_info['W'].iloc[0]),
        'losses': int(team_info['L'].iloc[0]),
        'conference_standing': int(team_info['CONF_RANK'].iloc[0]),
        'div_standing': int(team_info['DIV_RANK'].iloc[0]),
        'points_per_game': float(team_ranks['PTS_PG'].iloc[0]),
        'rebounds_per_game': float(team_ranks['REB_PG'].iloc[0]),
        'assists_per_game': float(team_ranks['AST_PG'].iloc[0])

    }