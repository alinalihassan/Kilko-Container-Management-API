from typing import List

import requests
from kilko_waste.definitions import (
    LoginRequest,
    LoginResponse,
    AuthenticatedRequest,
    BalanceResponse,
    ConfigResponse,
    Event,
)
from kilko_waste.consts import (
    BASE_URL,
    LOGIN_ENDPOINT,
    BALANCE_ENDPOINT,
    CONFIG_ENDPOINT,
    EVENTS_ENDPOINT,
)


def login_request(body: LoginRequest) -> LoginResponse:
    response = requests.post(f"{BASE_URL}/{LOGIN_ENDPOINT}", json=body.to_dict())
    return LoginResponse.from_dict(response.json())


def balance_request(body: AuthenticatedRequest) -> BalanceResponse:
    response = requests.post(f"{BASE_URL}/{BALANCE_ENDPOINT}", json=body.to_dict())
    return BalanceResponse.from_dict(response.json())


def config_request(body: AuthenticatedRequest) -> ConfigResponse:
    response = requests.post(f"{BASE_URL}/{CONFIG_ENDPOINT}", json=body.to_dict())
    return ConfigResponse.from_dict(response.json())


def events_request(body: AuthenticatedRequest) -> List[Event]:
    response = requests.post(f"{BASE_URL}/{EVENTS_ENDPOINT}", json=body.to_dict())
    return [Event.from_dict(event) for event in response.json()]
