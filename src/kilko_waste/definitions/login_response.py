from dataclasses import dataclass
from typing import Any
from .config_response import ConfigResponse
from .util import (
    from_int,
    from_str,
    from_bool,
    to_class,
)

@dataclass
class LoginResponse:
    success: bool
    card_number: int
    token: str
    config: ConfigResponse
    has_fcm_token: bool

    @staticmethod
    def from_dict(obj: Any) -> "LoginResponse":
        assert isinstance(obj, dict)
        success = from_bool(obj.get("success"))
        card_number = from_int(obj.get("cardNumber"))
        token = from_str(obj.get("token"))
        config = ConfigResponse.from_dict(obj.get("config"))
        has_fcm_token = from_bool(obj.get("hasFCMToken"))
        return LoginResponse(success, card_number, token, config, has_fcm_token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["success"] = from_bool(self.success)
        result["cardNumber"] = from_int(self.card_number)
        result["token"] = from_str(self.token)
        result["config"] = to_class(ConfigResponse, self.config)
        result["hasFCMToken"] = from_bool(self.has_fcm_token)
        return result
