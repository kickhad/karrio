from typing import List, Tuple
from purplship.core.utils.serializable import Serializable, Deserializable
from purplship.api.mapper import Mapper as BaseMapper
from purplship.core.models import (
    ShipmentCancelRequest,
    PickupUpdateRequest,
    ShipmentRequest,
    TrackingRequest,
    PickupRequest,
    RateRequest,
    ConfirmationDetails,
    TrackingDetails,
    ShipmentDetails,
    PickupDetails,
    RateDetails,
    Message,
)
from purplship.providers.ups_ground import (
    pickup_update_request,
    shipment_request,
    pickup_request,
    rate_request,
    tracking_request,
    parse_pickup_update_response,
    parse_pickup_cancel_response,
    parse_shipment_response,
    parse_pickup_response,
    parse_rate_response,
    parse_tracking_response,
)
from purplship.mappers.ups.settings import Settings


class Mapper(BaseMapper):
    settings: Settings

    def create_rate_request(self, payload: RateRequest) -> Serializable:
        return rate_request(payload, self.settings)

    def create_tracking_request(self, payload: TrackingRequest) -> Serializable:
        return tracking_request(payload, self.settings)

    def create_shipment_request(self, payload: ShipmentRequest) -> Serializable:
        return shipment_request(payload, self.settings)

    def create_pickup_request(self, payload: PickupRequest) -> Serializable:
        return pickup_request(payload, self.settings)

    def create_pickup_update_request(
        self, payload: PickupUpdateRequest
    ) -> Serializable:
        return pickup_update_request(payload, self.settings)

    def parse_cancel_pickup_response(
        self, response: Deserializable[str]
    ) -> Tuple[ConfirmationDetails, List[Message]]:
        return parse_pickup_cancel_response(response.deserialize(), self.settings)

    def parse_pickup_response(
        self, response: Deserializable[str]
    ) -> Tuple[PickupDetails, List[Message]]:
        return parse_pickup_response(response.deserialize(), self.settings)

    def parse_pickup_update_response(
        self, response: Deserializable[str]
    ) -> Tuple[PickupDetails, List[Message]]:
        return parse_pickup_update_response(response.deserialize(), self.settings)

    def parse_rate_response(
        self, response: Deserializable[str]
    ) -> Tuple[List[RateDetails], List[Message]]:
        return parse_rate_response(response.deserialize(), self.settings)

    def parse_shipment_response(
        self, response: Deserializable[str]
    ) -> Tuple[ShipmentDetails, List[Message]]:
        return parse_shipment_response(response.deserialize(), self.settings)

    def parse_tracking_response(
        self, response: Deserializable[str]
    ) -> Tuple[List[TrackingDetails], List[Message]]:
        return parse_tracking_response(response.deserialize(), self.settings)