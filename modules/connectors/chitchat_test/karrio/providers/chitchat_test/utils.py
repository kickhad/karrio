
import karrio.core as core


class Settings(core.Settings):
    """Chitchat connection settings."""
    carrier_name: str = 'ChitChat'
    carrier_id: str = 'chitchats'
    username: str = ''
    client_id: str = 999999
    
    # username: str  # carrier specific api credential key

    @property
    def carrier_name(self):
        return "chitchat_test"

    @property
    def server_url(self):
        return (
            "https://staging.chitchat.com"
            if self.test_mode
            else "https://staging.chitchat.com"
        )
