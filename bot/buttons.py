from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from aiogram.types.web_app_info import WebAppInfo


def home(id, name1, name2):
    home = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{name1}",
                    web_app=WebAppInfo(url=f"https://food.pyco.uz/?user_id={id}"),
                ),
                InlineKeyboardButton(
                    text=name2, callback_data="change_lang"
                )
                # InlineKeyboardButton(text="🛒 Savat", callback_data="savat"),
            ]
        ]
    )
    return home


def back(name):
    back = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f"{name}", callback_data="home")]]
    )
    return back


def phone(name):
    phone = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=f"{name}", request_contact=True)]],
        resize_keyboard=True,
    )
    return phone


def location(name1, name2):
    location = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"{name1}", request_location=True),
                KeyboardButton(text=f"{name2}"),
            ]
        ],
        resize_keyboard=True,
    )
    return location
