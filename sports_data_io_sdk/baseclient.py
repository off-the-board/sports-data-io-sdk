from abc import ABC
from functools import wraps

from requests import Session, Request
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def GET(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        return self._make_request(Request("GET", **func(self, *args, **kwargs)))
    return wrapper


def POST(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        return self._make_request(Request("POST", **func(self, *args, **kwargs)))
    return wrapper


def url_auth(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        return self._url_auth(func(self, *args, **kwargs))
    return wrapper


def parameterize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        url, kwargs = func(*args, **kwargs)
        return url + "&".join(["{kw}={val}".format(kw=kw, val=val) for kw, val in kwargs.items() if val])
    return wrapper


class BaseClient(ABC):
    def __init__(self, **kwargs):
        self._session = self._build_session()
        self._api_key = kwargs.get("api_key")

    @staticmethod
    def _build_session():
        """Constructs session to interface with REST API"""
        status_forcelist = frozenset([500, 502, 503, 504])
        session = Session()
        retries = Retry(
            total=5,
            backoff_factor=0.3,
            status_forcelist=status_forcelist
        )
        adapter = HTTPAdapter(max_retries=retries)
        session.mount("https://", adapter)
        return session

    def _url_auth(self, url):
        return "{url}&api_key={api_key}".format(
            url=url,
            api_key=self._api_key
        )

    def _make_request(self, req):
        prepped = self._session.prepare_request(req)
        return self._session.send(prepped)
