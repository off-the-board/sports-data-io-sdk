import os

from sports_data_io_sdk.baseclient import BaseClient, GET
from sports_data_io_sdk.clients import BASE_URL, VERSION, RESP_TYPE
from sports_data_io_sdk.clients.utils import ADD_AUTH


class SportsDataNewsClient(BaseClient):
    def __init__(self, sport,  version=VERSION, resp_type=RESP_TYPE, **kwargs):
        self._base_url = "{base_url}/{version}/{sport}/{resp_type}".format(
            base_url=kwargs.get("base_url", BASE_URL), version=version, sport=sport, resp_type=resp_type)
        self._premium_url = "{base_url}/{version}/{sport}/news-rotoballer/{resp_type}".format(
            base_url=kwargs.get("base_url", BASE_URL), version=version, sport=sport, resp_type=resp_type)
        self._rotoballer_url = "{base_url}/{version}/{sport}/articles-rotoballer/{resp_type}".format(
            base_url=kwargs.get("base_url", BASE_URL), version=version, sport=sport, resp_type=resp_type)
        self._api_key = kwargs.get("api_key", os.getenv("SPORTS_DATA_IO_API_KEY"))
        self._params = {"key": self._api_key}
        super().__init__()

    @GET
    @ADD_AUTH
    def news(self):
        return "{base_url}/News".format(base_url=self._base_url)

    @GET
    @ADD_AUTH
    def news_by_date(self, date):
        return "{base_url}/NewsByDate/{date}".format(base_url=self._base_url, date=date)
               

    @GET
    @ADD_AUTH
    def news_by_player(self, player_id):
        return "{base_url}/NewsByPlayerID/{player_id}".format(base_url=self._base_url, player_id=player_id)
               

    @GET
    @ADD_AUTH
    def premium_news(self):
        return "{base_url}/PremiumNews".format(base_url=self._premium_url)

    @GET
    @ADD_AUTH
    def premium_news_by_date(self, date):
        return "{base_url}/PremiumNewsByDate/{date}".format(base_url=self._premium_url, date=date)

    @GET
    @ADD_AUTH
    def premium_news_by_player(self, player_id):
        return "{base_url}/PremiumNewsByPlayerID/{player_id}".format(base_url=self._premium_url, player_id=player_id)
               

    @GET
    @ADD_AUTH
    def rotoballer_articles(self):
        return "{base_url}/RotoBallerArticles".format(base_url=self._rotoballer_url)

    @GET
    @ADD_AUTH
    def rotoballer_articles_by_date(self, date):
        return "{base_url}/RotoBallerArticlesByDate/{date}".format(base_url=self._rotoballer_url, date=date)

    @GET
    @ADD_AUTH
    def rotoballer_artcles_by_player(self, player_id):
        return "{base_url}/RotoBallerArticlesByPlayerID/{player_id}".format(base_url=self._rotoballer_url,
                                                                            player_id=player_id)


