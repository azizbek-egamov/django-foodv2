import asyncio
import logging
import sys

from datetime import datetime
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from config import *
from buttons import *
from sqlite import *
from states import *
from language import Languages

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    pr = message.text.split()
    res = one_table_info("main_users", "user_id", message.from_user.id)
    l = one_table_info("main_lang", "uid", message.from_user.id)
    if l != False:
        lang_texts = Languages(message, l[2])
    else:
        AddLangInformation(message.from_user.id, "uz")
        lang_texts = Languages(message, "uz")

    if len(pr) > 1:
        if res != False:
            r = pr[1].split("--")
            if f"{r[0]}" == "payment":
                if f"{r[1]}" == f"{message.from_user.id}":
                    await message.answer(
                        text=lang_texts["payment_select"],
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text=lang_texts["olinganda"],
                                        callback_data="olinganda",
                                    ),
                                    InlineKeyboardButton(
                                        text=lang_texts["card"], callback_data="card"
                                    ),
                                ],
                                [
                                    InlineKeyboardButton(
                                        text=lang_texts["zakrit"], callback_data="home"
                                    )
                                ],
                            ]
                        ),
                    )
                else:
                    await message.answer(
                        text=lang_texts["start"],
                        reply_markup=home(
                            message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']
                        ),
                    )
            else:
                await message.answer(
                    text=lang_texts["start"],
                    reply_markup=home(
                        message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']
                    ),
                )
        else:
            await message.answer(
                text=lang_texts["phone"],
                reply_markup=phone(lang_texts["button_phone"]),
            )
            await state.set_state(InfoSave.contact)
    else:
        res = one_table_info("main_users", "user_id", message.from_user.id)
        if res != False:
            await message.answer(
                text=lang_texts["start"],
                reply_markup=home(message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']),
            )
        else:
            await message.answer(
                text=lang_texts["phone"],
                reply_markup=phone(lang_texts["button_phone"]),
            )
            await state.set_state(InfoSave.contact)


@dp.message(F.contact, InfoSave.contact)
async def ContactSave(message: Message, state: FSMContext):
    l = one_table_info("main_lang", "uid", message.from_user.id)
    lang_texts = Languages(message, l[2])

    if message.contact.user_id == message.from_user.id:
        AddUserInfo(
            message.from_user.id,
            message.from_user.username,
            message.contact.phone_number,
        )
        r = await message.answer(".", reply_markup=ReplyKeyboardRemove())
        await bot.delete_message(message.from_user.id, r.message_id)
        await message.answer(
            text=lang_texts["start"],
            reply_markup=home(message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']),
        )
        await state.clear()
    else:
        await message.answer(
            text=lang_texts["phone_only"],
            reply_markup=phone(lang_texts["button_phone"]),
        )


@dp.callback_query(F.data == "home")
async def command_start_handler(callback: CallbackQuery, state: FSMContext):

    l = one_table_info("main_lang", "uid", callback.message.chat.id)
    lang_texts = Languages(callback, l[2])

    await callback.message.delete()
    await callback.message.answer(
        text=lang_texts["start"],
        reply_markup=home(callback.message.chat.id, lang_texts["button_buyurtma"], lang_texts['change_til']),
    )
    await state.clear()


@dp.message(F.text == "🏘 Asosiy menyu")
async def HomeX(message: Message, state: FSMContext):
    l = one_table_info("main_lang", "uid", message.from_user.id)
    lang_texts = Languages(message, l[2])
    m = await message.answer('.', reply_markup=ReplyKeyboardRemove())
    await bot.delete_message(message.from_user.id, m.message_id)
    await message.answer(
        text=lang_texts["start"],
        reply_markup=home(message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']),
    )
    await state.clear()


@dp.message(F.text == "🏘 Главное меню")
async def HomeX(message: Message, state: FSMContext):
    l = one_table_info("main_lang", "uid", message.from_user.id)
    m = await message.answer('.', reply_markup=ReplyKeyboardRemove())
    await bot.delete_message(message.from_user.id, m.message_id)
    lang_texts = Languages(message, l[2])
    await message.answer(
        text=lang_texts["start"],
        reply_markup=home(message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']),
    )
    await state.clear()


@dp.callback_query(F.data == "olinganda")
async def AzakazBer(callback: CallbackQuery, state: FSMContext):
    r = table_info("main_userfoodlist", "user_id", callback.message.chat.id)
    l = one_table_info("main_lang", "uid", callback.message.chat.id)
    lang_texts = Languages(callback, l[2])
    if r != False:
        await callback.message.delete()
        await callback.message.answer(
            text=lang_texts["order_location_prompt"],
            reply_markup=location(lang_texts["button_loc"], lang_texts["button_home"]),
        )
        await state.set_state(OlPay.location)
    else:
        await callback.message.delete()
        await callback.message.answer(
            text=lang_texts["order_empty"],
            reply_markup=home(callback.message.chat.id, lang_texts["button_home"], lang_texts['change_til']),
        )
        await state.clear()


@dp.message(OlPay.location)
async def Locs(message: Message, state: FSMContext):
    l = one_table_info("main_lang", "uid", message.from_user.id)
    lang_texts = Languages(message, l[2])
    if message.location:
        id = message.from_user.id
        res = table_info("main_userfoodlist", "user_id", id)
        if res != False:
            s = 1
            m = ""
            p = 0
            for i in res:
                m += f"""{s}: Nomi: {i[2]}
Narxi: {i[3]} so'm
Soni: {i[5]} ta
Umumiy: {float(i[3]) * int(i[5])} so'm\n\n"""
                s += 1
                p += float(i[3]) * int(i[5])

            locationn = message.location
            await bot.send_location(
                chat_id=admin,
                latitude=locationn.latitude,
                longitude=locationn.longitude,
            )

            await bot.send_message(
                chat_id=admin,
                text=f"""<b>✔️ Yangi buyurtma:\n\n<i>{m}</i>Umumiy summa: {p} so'm

Foydalanuvchi ma'lumoti:
User: {"@" + f"{message.from_user.username}" if message.from_user.username != None else "Mavjud emas"}
Telefon: {one_table_info('main_users', 'user_id', message.from_user.id)[3]}
<i>To'lov buyurtma olinganda qilinadi</i></b>""",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="✅ Yetkazildi", callback_data=f"ok-{id}"
                            ),
                            InlineKeyboardButton(
                                text="❌ Yetkazilmadi",
                                callback_data=f"no-{id}",
                            ),
                        ]
                    ]
                ),
            )
            b = await message.answer(".", reply_markup=ReplyKeyboardRemove())
            await bot.delete_message(chat_id=id, message_id=b.message_id)
            delete_table("main_userfoodlist", "user_id", message.from_user.id)
            await message.answer(
                text=lang_texts["order_success"],
                reply_markup=home(message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']),
            )
            await state.clear()
        else:
            await message.answer(
                text=lang_texts["order_empty"],
                reply_markup=home(message.from_user.id, lang_texts["button_buyurtma"], lang_texts['change_til']),
            )
            await state.clear()
    else:
        await message.answer(
            text=lang_texts["order_location_prompt"],
            reply_markup=location(lang_texts["button_loc"], lang_texts["button_home"]),
        )


@dp.callback_query(F.data == "card")
async def AzakazBer(callback: CallbackQuery, state: FSMContext):
    res = select_info("main_cardinfo")
    l = one_table_info("main_lang", "uid", callback.message.chat.id)
    lang_texts = Languages(callback, l[2])
    if res != False:
        r = table_info("main_userfoodlist", "user_id", callback.message.chat.id)
        if r != False:
            await callback.message.delete()
            await callback.message.answer_photo(
                photo=FSInputFile(f"../media/{res[0][2]}"),
                caption=lang_texts["payment_card"],
                reply_markup=back(lang_texts["button_back"]),
            )
            await state.set_state(Pay.payment)
        else:
            await callback.message.delete()
            await callback.message.answer(
                text=lang_texts["order_empty"],
                reply_markup=home(callback.message.chat.id, lang_texts["button_home"], lang_texts['change_til']),
            )
            await state.clear()
    else:
        await callback.answer(
            text=lang_texts["payment_null"],
            show_alert=True,
        )


@dp.message(Pay.payment)
async def PayPage(message: Message, state: FSMContext):
    if message.photo:
        l = one_table_info("main_lang", "uid", message.from_user.id)
        lang_texts = Languages(message, l[2])
        await state.update_data({"file_id": message.photo[-1].file_id})
        await state.update_data({"type": "photo"})
        await message.answer(
            text=lang_texts["payment_file_prompt"],
            reply_markup=location(lang_texts["button_loc"], lang_texts["button_home"]),
        )
        await state.set_state(Pay.location)
    elif message.document:
        if message.document.mime_type == "application/pdf":
            await state.update_data({"file_id": message.document.file_id})
            await state.update_data({"type": "document"})
            await message.answer(
                text=lang_texts["payment_file_prompt"],
                reply_markup=location(
                    lang_texts["button_loc"], lang_texts["button_home"]
                ),
            )
            await state.set_state(Pay.location)
        else:
            await message.answer(
                text=lang_texts["payment_file_error"],
                reply_markup=back(lang_texts["button_back"]),
            )
    else:
        await message.answer(
            text=lang_texts["payment_file_error"],
            reply_markup=back(lang_texts["button_back"]),
        )


@dp.message(Pay.location)
async def Locs(message: Message, state: FSMContext):
    if message.location:
        l = one_table_info("main_lang", "uid", message.from_user.id)
        lang_texts = Languages(message, l[2])
        id = message.from_user.id
        data = await state.get_data()
        file_id = data.get("file_id")
        type = data.get("type")
        res = table_info("main_userfoodlist", "user_id", id)
        if res != False:
            s = 1
            m = ""
            p = 0
            for i in res:
                m += f"""{s}: Nomi: {i[2]}
Narxi: {i[3]} so'm
Soni: {i[5]} ta
Umumiy: {float(i[3]) * int(i[5])} so'm\n\n"""
                s += 1
                p += float(i[3]) * int(i[5])

            locationn = message.location
            await bot.send_location(
                chat_id=admin,
                latitude=locationn.latitude,
                longitude=locationn.longitude,
            )
            if type == "photo":
                await bot.send_photo(
                    chat_id=admin, photo=file_id, caption="<b>🔗 Chek ma'lumoti</b>"
                )
            else:
                await bot.send_document(
                    chat_id=admin, document=file_id, caption="<b>🔗 Chek ma'lumoti</b>"
                )

            await bot.send_message(
                chat_id=admin,
                text=f"""<b>✔️ Yangi buyurtma:\n\n<i>{m}</i>Umumiy summa: {p} so'm

Foydalanuvchi ma'lumoti:
User: {"@" + f"{message.from_user.username}" if message.from_user.username != None else "Mavjud emas"}
Telefon: {one_table_info('main_users', 'user_id', message.from_user.id)[3]}
<i>Karta orqali to'lov</i></b>""",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="✅ Yetkazildi", callback_data=f"ok-{id}"
                            ),
                            InlineKeyboardButton(
                                text="❌ Yetkazilmadi", callback_data=f"no-{id}"
                            ),
                        ]
                    ]
                ),
            )
            b = await message.answer(".", reply_markup=ReplyKeyboardRemove())
            await bot.delete_message(chat_id=id, message_id=b.message_id)
            delete_table("main_userfoodlist", "user_id", message.from_user.id)
            await message.answer(
                text=lang_texts["order_success"],
                reply_markup=home(message.from_user.id, lang_texts['button_buyurtma'], lang_texts['change_til']),
            )
            await state.clear()
        else:
            await message.answer(
                text=lang_texts["order_empty"],
                reply_markup=home(message.from_user.id, lang_texts['button_buyurtma'], lang_texts['change_til']),
            )
            await state.clear()
    else:
        await message.answer(
            text=lang_texts["order_location_prompt"],
            reply_markup=location(lang_texts['button_loc'], lang_texts['button_home']),
        )


@dp.callback_query(F.data.startswith("ok-"))
async def EditType(callback: CallbackQuery):

    id = callback.data.split("-")[1]
    txt = callback.message.text
    l = one_table_info("main_lang", "uid", id)
    lang_texts = Languages(callback, l[2])
    await callback.message.edit_text(text=f"<b>{txt}\n\n✅✅✅✅✅✅</b>")
    await bot.send_message(chat_id=id, text=lang_texts["order_thank_you"])


@dp.callback_query(F.data.startswith("no-"))
async def EditType(callback: CallbackQuery):
    id = callback.data.split("-")[1]
    txt = callback.message.text
    l = one_table_info("main_lang", "uid", id)
    lang_texts = Languages(callback, l[2])
    await callback.message.edit_text(text=f"<b>{txt}\n\n❌❌❌❌❌❌</b>")
    await bot.send_message(
        chat_id=id,
        text=lang_texts["order_cancelled"],
    )


@dp.message(Command("post"))
async def SendUserMessage(message: Message, state: FSMContext):
    if str(message.from_user.id) == admin:
        await bot.send_message(
            chat_id=admin,
            text="Foydalanuvchilarga yuboriladigan xabarni yuboring",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="◀️ Orqaga", callback_data="home")]
                ]
            ),
        )
        await state.set_state(SendUsersMessage.mess)


@dp.message(SendUsersMessage.mess)
async def SendUserMessage(message: Message, state: FSMContext):
    r = await message.answer("Xabar yuborish boshlandi")
    q = select_info("main_users")
    for i in q:
        if str(i[1]) != str(admin):
            await message.send_copy(chat_id=f"{i[1]}")

    await bot.delete_message(message.from_user.id, r.message_id)
    await message.answer("Xabar yuborish yakunlandi")
    await state.clear()

@dp.callback_query(F.data == "change_lang")
async def ChangeLanguage(callback: CallbackQuery):
    l = one_table_info("main_lang", "uid", callback.message.chat.id)
    lang_texts = Languages(callback, l[2])
    if f"{l[2]}" == "uz":
        flag = "🇺🇿"
        lang = "<b>O'zbek</b>"
    elif f"{l[2]}" == "ru":
        flag = "🇷🇺"
        lang = "<b>Русский</b>"
    await callback.message.delete()
    await callback.message.answer(
        text=f"{flag} {lang_texts['interface']}: {lang}",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=lang_texts['change_button'], callback_data=f"change")]
            ]
        )
    )
    
@dp.callback_query(F.data == "change")
async def ChangeLang(callback: CallbackQuery):
    l = one_table_info("main_lang", "uid", callback.message.chat.id)
    if f"{l[2]}" == "uz":
        UpdateLang(callback.message.chat.id, 'ru')
    elif f"{l[2]}" == "ru":
        UpdateLang(callback.message.chat.id, 'uz')
    l1 = one_table_info("main_lang", "uid", callback.message.chat.id)
    lang_texts = Languages(callback, l1[2])
    await callback.message.delete()
    await callback.message.answer(
        text=lang_texts['start'],
        reply_markup=home(callback.message.chat.id, lang_texts['button_buyurtma'], lang_texts['change_til'])
    )


async def send_message_to_admin():
    while True:
        now = datetime.now()
        if now.day == 20 and now.hour == 0 and now.minute == 0:
            message = await bot.send_message(chat_id=admin, text="<b>🕔 Bot o'chib qolishiga 2 kun qolganini ma'lum qilamiz, o'chib qolishini oldini olish uchun dasturchi bilan aloqaga chiqishingizni iltimos qilamiz.</b>")
            await bot.pin_chat_message(chat_id=admin, message_id=message.message_id)
            await asyncio.sleep(60)
        await asyncio.sleep(30)

@dp.startup()
async def on_startup():
    asyncio.create_task(send_message_to_admin())


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
