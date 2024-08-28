from dataclasses import dataclass
from typing import Any
from .util import from_float


@dataclass
class BalanceResponse:
    balance: float

    @staticmethod
    def from_dict(obj: Any) -> "BalanceResponse":
        assert isinstance(obj, dict)
        balance = float(obj.get("balance"))
        return BalanceResponse(balance)

    def to_dict(self) -> dict:
        result: dict = {}
        result["balance"] = from_float(self.balance)
        return result
