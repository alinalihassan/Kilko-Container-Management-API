from dataclasses import dataclass
from typing import Any, List
from .util import (
    from_int,
    from_str,
    from_bool,
    from_none,
    from_list,
    from_float,
    to_class,
    to_float,
)


@dataclass
class AskEmailVerification:
    ask_now: bool
    current_email: None

    @staticmethod
    def from_dict(obj: Any) -> "AskEmailVerification":
        assert isinstance(obj, dict)
        ask_now = from_bool(obj.get("askNow"))
        current_email = from_none(obj.get("currentEmail"))
        return AskEmailVerification(ask_now, current_email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["askNow"] = from_bool(self.ask_now)
        result["currentEmail"] = from_none(self.current_email)
        return result


@dataclass
class Choices:
    price: List[str]
    balance: List[int]
    description: List[str]

    @staticmethod
    def from_dict(obj: Any) -> "Choices":
        assert isinstance(obj, dict)
        price = from_list(from_str, obj.get("price"))
        balance = from_list(lambda x: int(from_str(x)), obj.get("balance"))
        description = from_list(from_str, obj.get("description"))
        return Choices(price, balance, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["price"] = from_list(from_str, self.price)
        result["balance"] = from_list(
            lambda x: from_str((lambda x: str(x))(x)), self.balance
        )
        result["description"] = from_list(from_str, self.description)
        return result


@dataclass
class BalanceIncrease:
    method: str
    price_selection: str
    choices: Choices
    note_html: str

    @staticmethod
    def from_dict(obj: Any) -> "BalanceIncrease":
        assert isinstance(obj, dict)
        method = from_str(obj.get("method"))
        price_selection = from_str(obj.get("priceSelection"))
        choices = Choices.from_dict(obj.get("choices"))
        note_html = from_str(obj.get("noteHtml"))
        return BalanceIncrease(method, price_selection, choices, note_html)

    def to_dict(self) -> dict:
        result: dict = {}
        result["method"] = from_str(self.method)
        result["priceSelection"] = from_str(self.price_selection)
        result["choices"] = to_class(Choices, self.choices)
        result["noteHtml"] = from_str(self.note_html)
        return result


@dataclass
class BalanceNotation:
    nl_prefix: str
    en_prefix: str
    nl_postfix: str
    en_postfix: str

    @staticmethod
    def from_dict(obj: Any) -> "BalanceNotation":
        assert isinstance(obj, dict)
        nl_prefix = from_str(obj.get("NLPrefix"))
        en_prefix = from_str(obj.get("ENPrefix"))
        nl_postfix = from_str(obj.get("NLPostfix"))
        en_postfix = from_str(obj.get("ENPostfix"))
        return BalanceNotation(nl_prefix, en_prefix, nl_postfix, en_postfix)

    def to_dict(self) -> dict:
        result: dict = {}
        result["NLPrefix"] = from_str(self.nl_prefix)
        result["ENPrefix"] = from_str(self.en_prefix)
        result["NLPostfix"] = from_str(self.nl_postfix)
        result["ENPostfix"] = from_str(self.en_postfix)
        return result


@dataclass
class City:
    id: int
    country_code: str
    name: str
    latitude: None
    longitude: None

    @staticmethod
    def from_dict(obj: Any) -> "City":
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        country_code = from_str(obj.get("countryCode"))
        name = from_str(obj.get("name"))
        latitude = from_none(obj.get("latitude"))
        longitude = from_none(obj.get("longitude"))
        return City(id, country_code, name, latitude, longitude)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["countryCode"] = from_str(self.country_code)
        result["name"] = from_str(self.name)
        result["latitude"] = from_none(self.latitude)
        result["longitude"] = from_none(self.longitude)
        return result


@dataclass
class Address:
    id: int
    city_id: int
    street: str
    street_number: int
    zip_code: str
    address_type_id: None
    woz_number: None
    expiration_date: None
    remote_system_id: None
    remarks: None
    latitude: None
    longitude: None
    city: City

    @staticmethod
    def from_dict(obj: Any) -> "Address":
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        city_id = from_int(obj.get("cityId"))
        street = from_str(obj.get("street"))
        street_number = int(from_str(obj.get("streetNumber")))
        zip_code = from_str(obj.get("zipCode"))
        address_type_id = from_none(obj.get("addressTypeId"))
        woz_number = from_none(obj.get("wozNumber"))
        expiration_date = from_none(obj.get("expirationDate"))
        remote_system_id = from_none(obj.get("remoteSystemId"))
        remarks = from_none(obj.get("remarks"))
        latitude = from_none(obj.get("latitude"))
        longitude = from_none(obj.get("longitude"))
        city = City.from_dict(obj.get("city"))
        return Address(
            id,
            city_id,
            street,
            street_number,
            zip_code,
            address_type_id,
            woz_number,
            expiration_date,
            remote_system_id,
            remarks,
            latitude,
            longitude,
            city,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["cityId"] = from_int(self.city_id)
        result["street"] = from_str(self.street)
        result["streetNumber"] = from_str(str(self.street_number))
        result["zipCode"] = from_str(self.zip_code)
        result["addressTypeId"] = from_none(self.address_type_id)
        result["wozNumber"] = from_none(self.woz_number)
        result["expirationDate"] = from_none(self.expiration_date)
        result["remoteSystemId"] = from_none(self.remote_system_id)
        result["remarks"] = from_none(self.remarks)
        result["latitude"] = from_none(self.latitude)
        result["longitude"] = from_none(self.longitude)
        result["city"] = to_class(City, self.city)
        return result


@dataclass
class CardDetails:
    number: int
    address: Address

    @staticmethod
    def from_dict(obj: Any) -> "CardDetails":
        assert isinstance(obj, dict)
        number = from_int(obj.get("number"))
        address = Address.from_dict(obj.get("address"))
        return CardDetails(number, address)

    def to_dict(self) -> dict:
        result: dict = {}
        result["number"] = from_int(self.number)
        result["address"] = to_class(Address, self.address)
        return result


@dataclass
class MapDefault:
    latitude: float
    longitude: float
    zoom: int

    @staticmethod
    def from_dict(obj: Any) -> "MapDefault":
        assert isinstance(obj, dict)
        latitude = from_float(obj.get("latitude"))
        longitude = from_float(obj.get("longitude"))
        zoom = from_int(obj.get("zoom"))
        return MapDefault(latitude, longitude, zoom)

    def to_dict(self) -> dict:
        result: dict = {}
        result["latitude"] = to_float(self.latitude)
        result["longitude"] = to_float(self.longitude)
        result["zoom"] = from_int(self.zoom)
        return result


#TODO: Home page is null for Ouder Amstel, needs more testing
@dataclass
class ConfigResponse:
    client_id: int
    home_page: None
    card_details: CardDetails
    messages_enabled: bool
    map_with_fraction_icons: bool
    make_my_containers_collection_points: bool
    hide_container_search: bool
    enable_qr_codes: bool
    container_events_enabled: bool
    dump_enabled: bool
    wheelie_bins_enabled: bool
    waste_calendar_enabled: bool
    waste_calendar_notifications_enabled: bool
    remote_opening_enabled: bool
    bluetooth_opening_enabled: bool
    report_malfunction_enabled: bool
    paid: bool
    redirect_to_tab_if_no_containers_whitelisted: str
    ask_email_verification: AskEmailVerification
    allow_balance_increase: bool
    balance_notation: BalanceNotation
    balance_increase: BalanceIncrease
    map_default: MapDefault
    extra_pages: List[Any]
    extra_page_hash: str

    @staticmethod
    def from_dict(obj: Any) -> "ConfigResponse":
        assert isinstance(obj, dict)
        client_id = from_int(obj.get("clientId"))
        home_page = from_none(obj.get("homePage"))
        card_details = CardDetails.from_dict(obj.get("cardDetails"))
        messages_enabled = from_bool(obj.get("messagesEnabled"))
        map_with_fraction_icons = from_bool(obj.get("mapWithFractionIcons"))
        make_my_containers_collection_points = from_bool(
            obj.get("makeMyContainersCollectionPoints")
        )
        hide_container_search = from_bool(obj.get("hideContainerSearch"))
        enable_qr_codes = from_bool(obj.get("enableQRCodes"))
        container_events_enabled = from_bool(obj.get("containerEventsEnabled"))
        dump_enabled = from_bool(obj.get("dumpEnabled"))
        wheelie_bins_enabled = from_bool(obj.get("wheelieBinsEnabled"))
        waste_calendar_enabled = from_bool(obj.get("wasteCalendarEnabled"))
        waste_calendar_notifications_enabled = from_bool(
            obj.get("wasteCalendarNotificationsEnabled")
        )
        remote_opening_enabled = from_bool(obj.get("remoteOpeningEnabled"))
        bluetooth_opening_enabled = from_bool(obj.get("bluetoothOpeningEnabled"))
        report_malfunction_enabled = from_bool(obj.get("reportMalfunctionEnabled"))
        paid = from_bool(obj.get("paid"))
        redirect_to_tab_if_no_containers_whitelisted = from_str(
            obj.get("redirectToTabIfNoContainersWhitelisted")
        )
        ask_email_verification = AskEmailVerification.from_dict(
            obj.get("askEmailVerification")
        )
        allow_balance_increase = from_bool(obj.get("allowBalanceIncrease"))
        balance_notation = BalanceNotation.from_dict(obj.get("balanceNotation"))
        balance_increase = BalanceIncrease.from_dict(obj.get("balanceIncrease"))
        map_default = MapDefault.from_dict(obj.get("mapDefault"))
        extra_pages = from_list(lambda x: x, obj.get("extraPages"))
        extra_page_hash = from_str(obj.get("extraPageHash"))
        return ConfigResponse(
            client_id,
            home_page,
            card_details,
            messages_enabled,
            map_with_fraction_icons,
            make_my_containers_collection_points,
            hide_container_search,
            enable_qr_codes,
            container_events_enabled,
            dump_enabled,
            wheelie_bins_enabled,
            waste_calendar_enabled,
            waste_calendar_notifications_enabled,
            remote_opening_enabled,
            bluetooth_opening_enabled,
            report_malfunction_enabled,
            paid,
            redirect_to_tab_if_no_containers_whitelisted,
            ask_email_verification,
            allow_balance_increase,
            balance_notation,
            balance_increase,
            map_default,
            extra_pages,
            extra_page_hash,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["clientId"] = from_int(self.client_id)
        result["homePage"] = from_none(self.home_page)
        result["cardDetails"] = to_class(CardDetails, self.card_details)
        result["messagesEnabled"] = from_bool(self.messages_enabled)
        result["mapWithFractionIcons"] = from_bool(self.map_with_fraction_icons)
        result["makeMyContainersCollectionPoints"] = from_bool(
            self.make_my_containers_collection_points
        )
        result["hideContainerSearch"] = from_bool(self.hide_container_search)
        result["enableQRCodes"] = from_bool(self.enable_qr_codes)
        result["containerEventsEnabled"] = from_bool(self.container_events_enabled)
        result["dumpEnabled"] = from_bool(self.dump_enabled)
        result["wheelieBinsEnabled"] = from_bool(self.wheelie_bins_enabled)
        result["wasteCalendarEnabled"] = from_bool(self.waste_calendar_enabled)
        result["wasteCalendarNotificationsEnabled"] = from_bool(
            self.waste_calendar_notifications_enabled
        )
        result["remoteOpeningEnabled"] = from_bool(self.remote_opening_enabled)
        result["bluetoothOpeningEnabled"] = from_bool(self.bluetooth_opening_enabled)
        result["reportMalfunctionEnabled"] = from_bool(self.report_malfunction_enabled)
        result["paid"] = from_bool(self.paid)
        result["redirectToTabIfNoContainersWhitelisted"] = from_str(
            self.redirect_to_tab_if_no_containers_whitelisted
        )
        result["askEmailVerification"] = to_class(
            AskEmailVerification, self.ask_email_verification
        )
        result["allowBalanceIncrease"] = from_bool(self.allow_balance_increase)
        result["balanceNotation"] = to_class(BalanceNotation, self.balance_notation)
        result["balanceIncrease"] = to_class(BalanceIncrease, self.balance_increase)
        result["mapDefault"] = to_class(MapDefault, self.map_default)
        result["extraPages"] = from_list(lambda x: x, self.extra_pages)
        result["extraPageHash"] = from_str(self.extra_page_hash)
        return result
