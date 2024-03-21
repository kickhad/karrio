import base64
import typing
import jstruct
import datetime
import karrio.lib as lib
import karrio.core as core


class Settings(core.Settings):
    """TGE connection settings."""

    username: str
    password: str
    api_key: str
    toll_username: str
    toll_password: str
    my_toll_token: str
    my_toll_identity: str
    account_code: str = None
    sscc_count: int = None
    shipment_count: int = None

    cache: lib.Cache = jstruct.JStruct[lib.Cache]

    @property
    def carrier_name(self):
        return "tge"

    @property
    def server_url(self):
        return self.connection_config.server_url.state or "https://tge.3plapi.com"

    @property
    def auth(self):
        pair = "%s:%s" % (self.toll_username, self.toll_password)
        return base64.b64encode(pair.encode("utf-8")).decode("ascii")

    @property
    def authorization(self):
        pair = "%s:%s" % (self.username, self.password)
        return base64.b64encode(pair.encode("utf-8")).decode("ascii")

    @property
    def connection_config(self) -> lib.units.Options:
        from karrio.providers.tge.units import ConnectionConfig

        return lib.to_connection_config(
            self.config or {},
            option_type=ConnectionConfig,
        )

    def next_shipment_identifiers(
        self, options: lib.units.Options, package_count: int
    ) -> typing.Tuple[str, list, int, int]:
        sscc_gs1 = lib.text(self.connection_config.SSCC_GS1.state) or ""
        ship_gs1 = lib.text(self.connection_config.SHIP_GS1.state) or ""
        sscc_count = (
            self.sscc_count
            if self.sscc_count is not None
            else lib.to_int(self.connection_config.SSCC_range_start.state) or 0
        )
        shipment_count = (
            self.shipment_count
            if self.shipment_count is not None
            else lib.to_int(self.connection_config.SHIP_range_start.state) or 0
        )

        if "tge_ssc_ids" in options:
            SSCCs = options.tge_ssc_ids.state
        else:
            SSCCs = [
                f"000{sscc_gs1}{str(sscc_count + (_ * 10)).zfill(6)}"
                for _, __ in enumerate(range(package_count), start=1)
            ]

        ShipmentID = (
            options.tge_shipment_id.state
            if "tge_shipment_id" in options
            else f"{ship_gs1}{str(shipment_count + 1).zfill(7)}"
        )

        # save in cache
        cache_key = f"{self.carrier_name}|{self.api_key}"
        state = self.cache.get(cache_key) or {}

        sscc_count = sscc_count + package_count
        shipment_count = shipment_count + 1

        self.cache.set(
            cache_key,
            {**state, "sscc_count": sscc_count, "shipment_count": shipment_count},
        )

        return (
            ShipmentID,
            SSCCs,
            shipment_count,
            sscc_count,
        )


def parse_response(response: str) -> dict:
    _response = lib.failsafe(lambda: lib.to_dict(response))

    if _response is None:
        _error = response[: response.find(": {")].strip()
        return dict(
            message=_error if any(_error) else response,
            is_error=True,
        )

    return _response


def next_pickup_date(
    date_str: typing.Union[datetime.datetime, str]
) -> datetime.datetime:
    date = lib.to_date(date_str)

    # return next business day
    if date.weekday() == 5:
        return date + datetime.timedelta(days=3)

    return date + datetime.timedelta(days=1)
