import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '8544018631:AAGbZHmzrae6rmFpC4t1deZ50Ob3-kJ8s0s')
    API_ID = int(os.environ.get("API_ID", '38504611'))
    API_HASH = os.environ.get("API_HASH", '420384645adef5188488fba99dd61df6')
    AUTH_USER = os.environ.get('AUTH_USERS', '8272089956').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer

