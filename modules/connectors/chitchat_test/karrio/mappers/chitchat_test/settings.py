
"""Karrio Chitchat client settings."""

import attr
import karrio.providers.chitchat_test.utils as provider_utils


@attr.s(auto_attribs=True)
class Settings(provider_utils.Settings):
    """Chitchat connection settings."""
    
    # required carrier specific properties
    access_token: str = None
    client_id: str = None
    id: str = None

    # generic properties
    id: str = None
    test_mode: bool = False
    carrier_id: str = "chitchat_test"
    account_country_code: str = None
    metadata: dict = {}
    config: dict = {}
