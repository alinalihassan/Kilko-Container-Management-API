from dataclasses import dataclass
from typing import Any
from .util import from_str


@dataclass
class AuthenticatedRequest:
    app: str
    token: str

    @staticmethod
    def from_dict(obj: Any) -> "AuthenticatedRequest":
        assert isinstance(obj, dict)
        app = from_str(obj.get("app"))
        token = from_str(obj.get("token"))
        return AuthenticatedRequest(app, token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["app"] = from_str(self.app)
        result["token"] = from_str(self.token)
        return result
