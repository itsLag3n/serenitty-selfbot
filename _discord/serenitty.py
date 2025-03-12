from .guild import *
from .channel import *
import tls_client

class Serenitty:
    def __init__(self, session, ws=None):
        self.ws = ws
        self.session = session
    
    def check_token(self):
        try:
            r = self.session.get("https://discord.com/api/v9/users/@me")
            if r.status_code != 200:
                return { "valid": False, "message": "Token Invalid" }
            else:
                return { "valid": True }
        except tls_client.exceptions.TLSClientExeption:
            return { "valid": False, "message": "Cannot connect to discord, check your internet connection." }
    
    async def send_message(self, channel_id, content, tts=False):
        payload = {
            "content": content,
            "tts": tts
        }
        r = self.session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload)
    
    async def get_guild(self, guild_id):
        r = self.session.get(f"https://discord.com/api/v9/guilds/{guild_id}")
        guild = Guild(self.session, r.json())
        return guild
    
    async def get_channel(self, channel_id):
        r = self.session.get(f"https://discord.com/api/v9/channels/{channel_id}")
        channel = Channel(self.session, r.json())
        return channel