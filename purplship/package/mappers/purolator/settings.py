"""PurplShip UPS connection settings."""

import attr
from purplship.carriers.purolator.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """UPS connection settings."""

    user_token: str
    account_number: str
    language: str = 'en'
    id: str = None
    test: bool = False
    carrier_name: str = "Purolator"