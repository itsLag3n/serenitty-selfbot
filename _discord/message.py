from .author import *

class Message:
    def __init__(self, session, json):
        self.session = session
        self.json = json
        self.id = json.get('id')
        self.type = json.get('type')
        self.content = json.get('content')
        self.mentions = json.get('mentions')
        self.mention_roles = json.get('mention_roles')
        self.attachments = json.get('attachments')
        self.embeds = json.get('embeds')
        self.timestamp = json.get('timestamp')
        self.edited_timestamp = json.get('edited_timestamp')
        self.flags = json.get('flags')
        self.components = json.get('components')
        self.channel_id = json.get('channel_id')
        # Later
        self.authorJSON = json.get('author')
        self.author = Author(session, self.authorJSON)
        self.pinned = json.get('pinned')
        self.mention_everyone = json.get('mention_everyone')
        self.tts = json.get('tts')