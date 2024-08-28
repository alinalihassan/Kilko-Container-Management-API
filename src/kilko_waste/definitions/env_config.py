from dataclasses import dataclass
from .util import from_str, from_int, to_int
from typing import Any


@dataclass
class EnvConfig:
    user: int
    password: str

    @staticmethod
    def from_dict(obj: Any) -> "EnvConfig":
        assert isinstance(obj, dict)
        user = to_int(obj.get("KILKO_USER"))
        password = from_str(obj.get("KILKO_PASSWORD"))
        return EnvConfig(user, password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["KILKO_USER"] = from_int(self.user)
        result["KILKO_PASSWORD"] = from_str(self.password)
        return result
