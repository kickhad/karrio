
"""Karrio Chitchat client proxy."""

import karrio.lib as lib
import karrio.api.proxy as proxy
import karrio.mappers.chitchat_test.settings as provider_settings


class Proxy(proxy.Proxy):
    settings: provider_settings.Settings
    # def create_shipment(self, request: lib.Serializable) -> lib.Deserializable[str]:
    #     response = lib.request(
    #         url=f"{self.settings.server_url}/service",
    #         data=request.serialize(),
    #         trace=self.trace_as("json"),
    #         method="POST",
    #         headers={},
    #     )

    #     return lib.Deserializable(response, lib.to_dict)
    
    def get_all_shipments(self, request: lib.Serializable) -> lib.Deserializable[str]:
        response = lib.request(
            url=f"{self.settings.server_url}/api/v1/clients/{self.settings.client_id}/shipments",
            data=request.serialize(),
            trace=self.trace_as("json"),
            method="GET",
            headers={},
        )

        return lib.Deserializable(response, lib.to_dict)
    # def cancel_shipment(self, request: lib.Serializable) -> lib.Deserializable[str]:
    #     response = lib.request(
    #         url=f"{self.settings.server_url}/service",
    #         data=request.serialize(),
    #         trace=self.trace_as("json"),
    #         method="POST",
    #         headers={},
    #     )

    #     return lib.Deserializable(response, lib.to_dict)
    