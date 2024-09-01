from aiogram import Router

from src.bot.utils import filters

# MESSAGES
admin_msg = Router()
admin_msg.message.filter(filters.IsAdmin())
msg = Router()

# CALLBACKS
# admin_cb = Router()
# admin_cb.message.filter(filters.IsAdmin())
# cb = Router()

# INLINES
# inl = Router()

# ERRORS
# err = Router()
