from aiogram.utils import executor
from loader import dp
# Don`t remove this above, otherwise handlers will not be imported
import handlers


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
