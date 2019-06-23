import json
import os

import nose
import nose.tools
import responses

from sports_data_io_sdk.tests.test_utils import get_free_port, load_json
from sports_data_io_sdk.clients.odds import SportsDataOddsClient
from sports_data_io_sdk.tests.fixtures import SPORT, TEST_API_KEY, TEST_DATE, TEST_RESP_TYPE, TEST_VERSION, \
    TEST_GAME_ID, TEST_PLAYER_ID, TEST_TEAM_ID
from sports_data_io_sdk.tests.clients import FIXTURES_DIR

ODDS_DIR = os.path.join(FIXTURES_DIR, "odds/")


class TestSportsDataOddsClient(object):
    base_url = "http://localhost:{port}".format(port=get_free_port())
    mock_odds_client = SportsDataOddsClient(base_url=base_url, version=TEST_VERSION, resp_type=TEST_RESP_TYPE,
                                            sport=SPORT, api_key=TEST_API_KEY)

    @responses.activate
    def test_live_odds_by_date(self):
        uri_path = "{base_url}/LiveGameOddsByDate/{date}?key={api_key}".format(
            base_url=self.mock_odds_client._base_url, date=TEST_DATE, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(ODDS_DIR, "live_odds_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_odds_client.live_odds_by_date(TEST_DATE)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_ingame_odds_line_movement(self):
        uri_path = "{base_url}/InGameOddsLineMovement/{game_id}?key={api_key}".format(
            base_url=self.mock_odds_client._base_url, game_id=TEST_GAME_ID, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(ODDS_DIR, "ingame_odds_movement_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_odds_client.ingame_odds_line_movement(TEST_GAME_ID)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_player_props_by_date(self):
        uri_path = "{base_url}/PlayerPropsByDate/{date}?key={api_key}".format(
            base_url=self.mock_odds_client._base_url, date=TEST_DATE, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(ODDS_DIR, "player_props_by_date_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_odds_client.player_props_by_date(TEST_DATE)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_player_props_by_player(self):
        uri_path = "{base_url}/PlayerPropsByPlayerID/{date}/{player_id}?key={api_key}".format(
            base_url=self.mock_odds_client._base_url, date=TEST_DATE, player_id=TEST_PLAYER_ID, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(ODDS_DIR, "player_props_by_player_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_odds_client.player_props_by_player(TEST_DATE, TEST_PLAYER_ID)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_player_props_by_team(self):
        uri_path = "{base_url}/PlayerPropsByTeam/{date}/{team_id}?key={api_key}".format(
            base_url=self.mock_odds_client._base_url, date=TEST_DATE, team_id=TEST_TEAM_ID, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(ODDS_DIR, "player_props_by_team_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_odds_client.player_props_by_team(TEST_DATE, TEST_TEAM_ID)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_pregame_odds_by_date(self):
        uri_path = "{base_url}/GameOddsByDate/{date}?key={api_key}".format(
            base_url=self.mock_odds_client._base_url, date=TEST_DATE, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(ODDS_DIR, "pregame_odds_by_date_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_odds_client.pregame_odds_by_date(TEST_DATE)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)

    @responses.activate
    def test_pregame_odds_line_movement(self):
        uri_path = "{base_url}/GameOddsLineMovement/{game_id}?key={api_key}".format(
            base_url=self.mock_odds_client._base_url, game_id=TEST_GAME_ID, api_key=TEST_API_KEY)
        response_body = load_json(os.path.join(ODDS_DIR, "pregame_odds_line_movement_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_odds_client.pregame_odds_line_movement(TEST_GAME_ID)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_equals(res.json(), response_body)
