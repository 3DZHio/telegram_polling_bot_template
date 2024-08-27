from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from src.bot.handlers import get_routers
from src.config import settings
from src.bot.logs import setup_logger


async def on_startup(bot: Bot) -> None:
	await bot.delete_webhook(drop_pending_updates=True if settings.DROP == 1 else None)


def main() -> None:
	setup_logger(level=settings.LOG_LEVEL)
	bot = Bot(
		token=settings.BOT_TOKEN.get_secret_value(),
		default=DefaultBotProperties(parse_mode=ParseMode.HTML),
	)
	dp = Dispatcher(storage=RedisStorage(redis=Redis.from_url(url=settings.storage_dsn)))
	dp.include_routers(*get_routers())
	dp.startup.register(on_startup)
	
	run(dp.start_polling(bot))


if __name__ == "__main__":
	main()
