import os

from sports_data_io_sdk.baseclient import BaseClient, GET
from sports_data_io_sdk.clients import BASE_URL, VERSION, RESP_TYPE
from sports_data_io_sdk.clients.utils import ADD_AUTH


class SportsDataOddsClient(BaseClient):
    def __init__(self, sport,  version=VERSION, resp_type=RESP_TYPE, **kwargs):
        self._base_url = "{base_url}/{version}/{sport}/{resp_type}".format(
            base_url=kwargs.get("base_url", BASE_URL), version=version, sport=sport, resp_type=resp_type)
        self._api_key = kwargs.get("api_key", os.getenv("SPORTS_DATA_IO_API_KEY"))
        self._params = {"key": self._api_key}
        super().__init__()

    @GET
    @ADD_AUTH
    def live_odds_by_date(self, date):
        return "{base_url}/LiveGameOddsByDate/{date}".format(base_url=self._base_url, date=date)

    @GET
    @ADD_AUTH
    def ingame_odds_line_movement(self, game_id):
        return "{base_url}/InGameOddsLineMovement/{game_id}".format(base_url=self._base_url, game_id=game_id)
               

    @GET
    @ADD_AUTH
    def player_props_by_date(self, date):
        return "{base_url}/PlayerPropsByDate/{date}".format(base_url=self._base_url, date=date)

    @GET
    @ADD_AUTH
    def player_props_by_player(self, date, player_id):
        return "{base_url}/PlayerPropsByPlayer/{date}/{player_id}".format(base_url=self._base_url, date=date,
                                                                          player_id=player_id)

    @GET
    @ADD_AUTH
    def player_props_by_team(self, date, team_id):
        return "{base_url}/PlayerPropsByTeam/{date}/{team_id}".format(base_url=self._base_url, date=date,
                                                                      team_id=team_id)

    @GET
    @ADD_AUTH
    def pregame_odds_by_date(self, date):
        return "{base_url}/GameOddsByDate/{date}".format(base_url=self._base_url, date=date)

    @GET
    @ADD_AUTH
    def pregame_odds_by_line_movement(self, date, game_id):
        return "{base_url}/GameOddsLineMovement/{date}/{game_id}".format(base_url=self._base_url, date=date,
                                                                         game_id=game_id)

