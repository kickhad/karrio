
from karrio.core.metadata import Metadata

from karrio.mappers.chitchat_test.mapper import Mapper
from karrio.mappers.chitchat_test.proxy import Proxy
from karrio.mappers.chitchat_test.settings import Settings
import karrio.providers.chitchat_test.units as units


METADATA = Metadata(
    id="chitchat_test",
    label="Chitchat",
    # Integrations
    Mapper=Mapper,
    Proxy=Proxy,
    Settings=Settings,
    # Data Units
    is_hub=False
)
