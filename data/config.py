from typing import List
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")
ADMINS: List[str] = env.str("ADMINS").split(',')

USE_PG: bool = env.bool("USE_PG", False) # if you use postgres

PG_HOST: str = env.str("PG_HOST")
PG_PORT: int = env.int("PG_PORT")
PG_USER: str = env.str("PG_USER")
PG_PASSWORD: str = env.str("PG_PASSWORD")
PG_DATABASE: str = env.str("PG_DATABASE")

USE_WEBHOOK: bool = env.bool("USE_WEBHOOK", False) # if you use webhook else pooling

if USE_WEBHOOK:
    MAIN_WEBHOOK_ADDRESS: str = env.str("MAIN_WEBHOOK_ADDRESS")
    MAIN_WEBHOOK_SECRET_TOKEN: str = env.str("MAIN_WEBHOOK_SECRET_TOKEN")
