from aiogram.utils import executor

from utils.misc.on_shutdown import on_shutdown
from utils.misc.on_startup import on_startup


def main():
    import handlers
    import middlewares
    executor.start_polling(
        dispatcher=handlers.dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )


if __name__ == '__main__':
    main()
