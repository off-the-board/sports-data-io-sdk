import json
import os

import nose
import nose.tools
import responses

from sports_data_io_sdk.clients.news import SportsDataNewsClient
from sports_data_io_sdk.tests.clients import FIXTURES_DIR
from sports_data_io_sdk.tests.fixtures import SPORT, TEST_API_KEY, TEST_RESP_TYPE, TEST_VERSION, TEST_DATE, \
    TEST_PLAYER_ID
from sports_data_io_sdk.tests.test_utils import get_free_port, load_json

NEWS_DIR = os.path.join(FIXTURES_DIR, "news/")


class TestSportsDataNewsClient(object):
    base_url = "http://localhost:{port}".format(port=get_free_port())
    mock_news_client = SportsDataNewsClient(base_url=base_url, version=TEST_VERSION, resp_type=TEST_RESP_TYPE,
                                            sport=SPORT, api_key=TEST_API_KEY)

    @responses.activate
    def test_news(self):
        uri_path = "{base_url}/News?key={api_key}".format(
            base_url=self.mock_news_client._base_url, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "news_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.news()
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_news_by_date(self):
        uri_path = "{base_url}/NewsByDate/{date}?key={api_key}".format(
            base_url=self.mock_news_client._base_url, date=TEST_DATE, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "news_by_date_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.news_by_date(TEST_DATE)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_news_by_player(self):
        uri_path = "{base_url}/NewsByPlayerID/{player_id}?key={api_key}".format(
            base_url=self.mock_news_client._base_url, player_id=TEST_PLAYER_ID, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "news_by_player_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.news_by_player(TEST_PLAYER_ID)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_premium_news(self):
        uri_path = "{base_url}/PremiumNews?key={api_key}".format(
            base_url=self.mock_news_client._premium_url, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "premium_news_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.premium_news()
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_premium_news_by_date(self):
        uri_path = "{base_url}/PremiumNewsByDate/{date}?key={api_key}".format(
            base_url=self.mock_news_client._premium_url, date=TEST_DATE, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "premium_news_by_date_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.premium_news_by_date(TEST_DATE)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_premium_news_by_player(self):
        uri_path = "{base_url}/PremiumNewsByPlayerID/{player_id}?key={api_key}".format(
            base_url=self.mock_news_client._premium_url, player_id=TEST_PLAYER_ID, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "premium_news_by_player_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.premium_news_by_player(TEST_PLAYER_ID)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_rotoballer_articles(self):
        uri_path = "{base_url}/RotoBallerArticles?key={api_key}".format(
            base_url=self.mock_news_client._rotoballer_url, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "rotoballer_articles_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.rotoballer_articles()
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_rotoballer_articles_by_date(self):
        uri_path = "{base_url}/RotoBallerArticlesByDate/{date}?key={api_key}".format(
            base_url=self.mock_news_client._rotoballer_url, date=TEST_DATE, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "rotoballer_articles_by_date_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.rotoballer_articles_by_date(TEST_DATE)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_rotoballer_articles_by_player(self):
        uri_path = "{base_url}/RotoBallerArticlesByPlayerID/{player_id}?key={api_key}".format(
            base_url=self.mock_news_client._rotoballer_url, player_id=TEST_PLAYER_ID, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(NEWS_DIR, "rotoballer_articles_by_player_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_news_client.rotoballer_artcles_by_player(TEST_PLAYER_ID)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)
