import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types

from config_data.config import Config, load_config
from handlers.user_handlers import register_user_handlers
from handlers.other_handlers import register_other_handlers


# Инициализируем логгер
logger = logging.getLogger(__name__)


# Фнукция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_other_handlers(dp)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    # Настраиваем кнопку Menu
    async def set_main_menu(dp: Dispatcher):
        # Создаем список с командами для кнопки menu
        main_menu_commands = [
            types.BotCommand(command='/help', description='Справка по работе бота'),
            types.BotCommand(command='/support', description='Поддержка'),
            types.BotCommand(command='/contacts', description='Другие способы связи'),
            types.BotCommand(command='/payments', description='Платежи')
            ]
        await dp.bot.set_my_commands(main_menu_commands)

    # Регистрируем все хэндлеры
    register_all_handlers(dp)

    # Запускаем polling
    try:
        await dp.skip_updates() #в продакшене эту строку удалить она позволяет не принимать апдей когда бот был не запущен
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        # Запускаем функцию main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')