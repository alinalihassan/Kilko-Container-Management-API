from dataclasses import dataclass
from typing import Any
from .util import from_int, from_str


@dataclass
class LoginRequest:
    card_number: int
    password: str
    app: str
    client_name: str

    @staticmethod
    def from_dict(obj: Any) -> "LoginRequest":
        assert isinstance(obj, dict)
        card_number = from_int(obj.get("cardNumber"))
        password = from_str(obj.get("password"))
        app = from_str(obj.get("app"))
        client_name = from_str(obj.get("clientName"))
        return LoginRequest(card_number, password, app, client_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cardNumber"] = from_int(self.card_number)
        result["password"] = from_str(self.password)
        result["app"] = from_str(self.app)
        result["clientName"] = from_str(self.client_name)
        return result
