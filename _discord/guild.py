

class Guild:
    def __init__(self, session, json):
        self.session = session
        self.json = json
        self.id = json.get('id')
        self.name = json.get('name')
        self.icon = json.get('icon')
        self.icon_url = f"https://cdn.discordapp.com/icons/{self.id}/{self.icon}.webp" if self.icon else None
        self.description = json.get('description')
        self.banner = json.get('banner')
        self.banner_url = f"https://cdn.discordapp.com/banners/{self.id}/{self.banner}.webp" if self.banner else None
        self.owner_id = json.get('owner_id')
        self.region = json.get('region')
        self.afk_channel_id = json.get('afk_channel_id')
        self.afk_timeout = json.get('afk_timeout')
        self.system_channel_id = json.get('system_channel_id')
        self.system_channel_flags = json.get('system_channel_flags')
        self.widget_enabled = json.get('widget_enabled')
        self.widget_channel_id = json.get('widget_channel_id')
        self.verification_level = json.get('verification_level')
        self.roles = json.get('roles')
        self.default_message_notifications = json.get('default_message_notifications')
        self.mfa_level = json.get('mfa_level')
        self.explicit_content_filter = json.get('explicit_content_filter')
        self.max_presences = json.get('max_presences')
        self.max_members = json.get('max_members')
        self.max_stage_video_channel_users = json.get('max_stage_video_channel_users')
        self.max_video_channel_users = json.get('max_video_channel_users')
        self.vanity_url_code = json.get('vanity_url_code')
        self.premium_tier = json.get('premium_tier')
        self.premium_subscription_count = json.get('premium_subscription_count')
        self.preferred_locale = json.get('preferred_locale')
        self.rules_channel_id = json.get('rules_channel_id')
        self.safety_alerts_channel_id = json.get('safety_alerts_channel_id')
        self.public_updates_channel_id = json.get('public_updates_channel_id')
        self.premium_progress_bar_enabled = json.get('premium_progress_bar_enabled')
        self.latest_onboarding_question_id = json.get('latest_onboarding_question_id')
        self.nsfw = json.get('nsfw')
        self.nsfw_level = json.get('nsfw_level')
        self.emojis = json.get('emojis')
        self.stickers = json.get('stickers')
        self.incidents_data = json.get('incidents_data')
        self.inventory_settings  = json.get('inventory_settings')
        self.embed_enabled  = json.get('embed_enabled')
        self.embed_channel_id  = json.get('embed_channel_id')
    
    async def get_channels(self):
        pass
    
    async def leave(self):
        pass
    
    async def delete(self):
        pass
    
    async def create_text_channel(self, name, topic=None, nsfw=False):
        pass