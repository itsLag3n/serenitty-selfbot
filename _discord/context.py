from .channel import *
from .guild import *
from .message import *
from .author import *

class Context:
    def __init__(self, session, command: str, args: list =None, channel: Channel =None, guild: Guild =None, message: Message =None, author: Author =None):
        self.session = session
        self.command = command
        self.args = args
        self.channel = channel
        self.guild = guild
        self.message = message
        self.author = author
    
    async def send(self, content, tts=False):
        await self.channel.send(content, tts)