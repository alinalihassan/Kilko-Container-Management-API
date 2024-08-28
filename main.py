from dotenv import dotenv_values
from kilko_waste import (
    login_request,
    balance_request,
    config_request,
    events_request,
    LoginRequest,
    AuthenticatedRequest,
    EnvConfig,
)

APP_URL = "mykliko.kcm.com"
CLIENT_NAME = "Ouder Amstel"


# Kilko is a waste management company that operates in the Netherlands
class KilkoClient:
    logged_in: bool
    token: str

    def __init__(self) -> None:
        self.logged_in = False

    def login(self, user: str, password: str):
        body = LoginRequest(user, password, APP_URL, CLIENT_NAME)
        response = login_request(body)
        self.logged_in = True
        self.token = response.token

        # DEBUG
        print(response.to_dict())

    def balance(self) -> int:
        if not self.logged_in:
            return "You must be logged in!"
        body = AuthenticatedRequest(APP_URL, self.token)
        response = balance_request(body)

        return response.balance

    # TODO
    def containers(self):
        raise NotImplementedError

    def configuration(self):
        if not self.logged_in:
            return "You must be logged in!"
        body = AuthenticatedRequest(APP_URL, self.token)
        return config_request(body)

    def events(self):
        if not self.logged_in:
            return "You must be logged in!"
        body = AuthenticatedRequest(APP_URL, self.token)
        return events_request(body)


if __name__ == "__main__":
    # Load .env user and password
    config: EnvConfig = EnvConfig.from_dict(dotenv_values())

    client = KilkoClient()
    client.login(config.user, config.password)
    print(f"Credits left: {client.balance()}")
