

class Author:
    def __init__(self, session, json):
        self.session = session
        self.json = json
        self.public_flags = json.get('public_flags')
        self.flags = json.get('flags')
        self.id = json.get('id')
        self.username = json.get('username')
        self.discriminator = json.get('discriminator')
        self.avatar = json.get('avatar')
        self.avatar_url = f"https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.webp" if self.avatar else None
        self.banner = json.get('banner')
        self.banner_url = f"https://cdn.discordapp.com/banners/{self.id}/{self.banner}.webp" if self.banner else None
        self.banner_color = json.get('banner_color')
        self.accent_color = json.get('accent_color')
        self.global_name = json.get('global_name')
        self.avatar_decoration_data = json.get('avatar_decoration_data')
        self.clan = json.get('clan')
        self.primary_guild = json.get('primary_guild')