from aiogram import Dispatcher, types


# Функция для настройки кнопки Menu бота
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/command_1', description='command_1 desription'),
        types.BotCommand(command='/command_2', description='command_2 desription'),
        types.BotCommand(command='/command_3', description='command_3 desription'),
        types.BotCommand(command='/command_4', description='command_4 desription')
    ]
    await dp.bot.set_my_commands(main_menu_commands)