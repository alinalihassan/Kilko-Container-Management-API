from dataclasses import dataclass
from datetime import datetime
from typing import Any
from .util import from_datetime, from_str, from_none, from_int


# TODO: There's no weight or volume for waste in Ouder Amstel, needs more testing
@dataclass
class Event:
    time: datetime
    price: str
    weight: None
    container_container_number: str
    event_type: str
    address: str
    fraction: str
    fraction_id: int
    volume: None

    @staticmethod
    def from_dict(obj: Any) -> "Event":
        assert isinstance(obj, dict)
        time = from_datetime(obj.get("time"))
        price = from_str(obj.get("price"))
        weight = from_none(obj.get("weight"))
        container_container_number = from_str(obj.get("containerContainerNumber"))
        event_type = from_str(obj.get("eventType"))
        address = from_str(obj.get("address"))
        fraction = from_str(obj.get("fraction"))
        fraction_id = from_int(obj.get("fractionId"))
        volume = from_none(obj.get("volume"))
        return Event(
            time,
            price,
            weight,
            container_container_number,
            event_type,
            address,
            fraction,
            fraction_id,
            volume,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["time"] = self.time.isoformat()
        result["price"] = from_str(self.price)
        result["weight"] = from_none(self.weight)
        result["containerContainerNumber"] = from_str(self.container_container_number)
        result["eventType"] = from_str(self.event_type)
        result["address"] = from_str(self.address)
        result["fraction"] = from_str(self.fraction)
        result["fractionId"] = from_int(self.fraction_id)
        result["volume"] = from_none(self.volume)
        return result
