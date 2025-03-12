from .serenitty import *

class Channel:
    def __init__(self, session, json):
        self.session = session
        self.json = json
        self.id = json.get('id')
        self.type = json.get('type')
        self.last_message_id = json.get('last_message_id')
        self.flags = json.get('flags')
        self.guild_id = json.get('guild_id')
        self.name = json.get('name')
        self.parent_id = json.get('parent_id')
        self.rate_limit_per_user = json.get('rate_limit_per_user')
        self.topic = json.get('topic')
        self.position = json.get('position')
        self.permission_overwrites = json.get('permission_overwrites')
        self.nsfw = json.get('nsfw')
    
    async def send(self, content, tts=False):
        payload = {
            "content": content,
            "tts": tts
        }
        r = self.session.post(f"https://discord.com/api/v9/channels/{self.id}/messages", data=payload)
    
    async def delete(self):
        pass
    
    async def get_guild(self):
        return Serenitty(self.session).get_guild(self.guild_id)