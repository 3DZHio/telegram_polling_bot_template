from aiogram import Router

from src.bot.handlers import messages, callbacks, inlines, errors


def get_routers() -> list[Router]:
    # MESSAGES
    msg = [
        messages.routers.admin_msg,
        messages.routers.msg,
    ]
    # CALLBACKS
    cb = [
        # callbacks.routers.admin_cb,
        # callbacks.routers.cb,
    ]
    # INLINES
    inl = [
        # inlines.routers.inl,
    ]
    # ERRORS
    err = [
        # errors.routers.err,
    ]
    return msg + cb + inl + err
