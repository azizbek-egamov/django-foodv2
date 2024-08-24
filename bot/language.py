from aiogram.types import Update, Message, CallbackQuery
from sqlite import select_info


def Languages(event: Update, lang: str) -> dict:
    if isinstance(event, Message):
        user = event.from_user
    elif isinstance(event, CallbackQuery):
        user = event.from_user

    texts = {
        "uz": {
            "start": f"<b>👋 Salom {user.full_name}, siz bizning restoranimizdan ovqat buyurtma berishingiz mumkin</b>",
            "phone": "<b>📞 Botdan foydalanish uchun telefon raqamingizni yuboring</b>",
            "payment_select": "<b>✔️ To'lov turini tanlang.</b>",
            "order_empty": "<b>💁🏻‍♂️ Savatingiz bo'shab qolgan ko'rinadi</b>",
            "payment_null": "<b>💁🏻‍♂️ To'lov qilishingiz uchun karta ma'lumotlari topilmadi</b>",
            "order_success": "<b>✅ Buyurtma berish muvaffaqiyatli amalga oshirildi, tez orada manzilingizga buyurtma yetib keladi.</b>",
            "order_location_prompt": "<b>📍 Botga joylashuv ma'lumotingizni yuboring.</b>",
            "phone_only": "<b>⚠️ Faqat o'zingizni telefon raqamingzini yuboring</b>",
            "payment_card": f"<b>💳 Karta: <code>{select_info('main_cardinfo')[0][1] if select_info('main_cardinfo')[0][1] != False else "Yo'q"}</code>\nTepedagi karta raqamiga to'lov qiling va to'lovni tastiqlovchi chek yoki screenshotni yuboring.</b>",
            "payment_file_prompt": "<b>📍 Endi botga joylashuv ma'lumotingizni yuboring.</b>",
            "payment_file_error": "<b>⚠️ To'lovni tastiqlovchi chek yoki screenshotni yuboring.</b>",
            "order_thank_you": "<b>✅ Buyurtamngiz uchun rahmat, Sizni yana kutib qolamiz</b>",
            "order_cancelled": "<b>❌ Buyurtamngiz ba'zi sabablarga ko'ra bekor qilindi, iltimos qayta buyurtma bering.</b>",
            "send_user_message": "Foydalanuvchilarga yuboriladigan xabarni yuboring",
            "message_sent": "Xabar yuborish boshlandi",
            "message_sent_finish": "Xabar yuborish yakunlandi",
            "interface": "<b>Hozirda interfeys tili</b>",
            "button_buyurtma": "➕ Buyrtma berish",
            "button_back": "⬅️ Orqaga",
            "button_phone": "📞 Telefon raqamni ulashish",
            "button_loc": "📍 Joylashuvni ulashish",
            "button_home": "🏘 Asosiy menyu",
            "olinganda": "💰 Olinganda to'lanadi",
            "card": "💳 Karta orqali",
            "zakrit": "❌ Yopish",
            "yetkazildi": "✅ Yetkazildi",
            "yetkazilmadi": "❌ Yetkazilmadi",
            "change_til": "🌏 Tilni o'zgartirish",
            "change_button": "🇷🇺 Ruschaga o'zgartiring",
        },
        "ru": {
            "start": f"<b>👋 Привет {user.full_name}, вы можете заказать еду в нашем ресторане</b>",
            "phone": "<b>📞 Пожалуйста, отправьте свой номер телефона для использования бота</b>",
            "payment_select": "<b>✔️ Выберите способ оплаты</b>",
            "order_empty": "<b>💁🏻‍♂️ Ваш заказ выглядит пустым</b>",
            "payment_null": "<b>💁🏻‍♂️ Для осуществления платежа данные карты не найдены.</b>",
            "order_success": "<b>✅ Заказ успешно оформлен, вскоре он будет доставлен по вашему адресу.</b>",
            "order_location_prompt": "<b>📍 Пожалуйста, отправьте ваше местоположение.</b>",
            "phone_only": "<b>⚠️ Отправьте только свой номер телефона</b>",
            "payment_card": f"<b>💳 Карта: <code>{select_info('main_cardinfo')[0][1] if select_info('main_cardinfo')[0][1] != False else "Нет"}</code>\nОплатите по указанной карте и отправьте чек или скриншот подтверждения платежа.</b>",
            "payment_file_prompt": "<b>📍 Пожалуйста, отправьте ваше местоположение.</b>",
            "payment_file_error": "<b>⚠️ Отправьте чек или скриншот подтверждения платежа.</b>",
            "order_thank_you": "<b>✅ Спасибо за ваш заказ, мы ждем вас снова</b>",
            "order_cancelled": "<b>❌ Ваш заказ был отменен по некоторым причинам, пожалуйста, сделайте новый заказ.</b>",
            "send_user_message": "Отправьте сообщение пользователям",
            "message_sent": "Отправка сообщения началась",
            "message_sent_finish": "Отправка сообщения завершена",
            "interface": "<b>Текущий язык интерфейса</b>",
            "button_buyurtma": "➕ Сделать заказ",
            "button_back": "⬅️ Назад",
            "button_phone": "📞 Поделиться номером телефона",
            "button_loc": "📍 Поделиться местоположением",
            "button_home": "🏘 Главное меню",
            "olinganda": "💰 Оплата производится при получении",
            "card": "💳 Через карту",
            "zakrit": "❌ Закрыть",
            "yetkazildi": "✅ Доставлено",
            "yetkazilmadi": "❌ Не доставлено",
            "change_til": "🌏 Изменить язык",
            "change_button": "🇺🇿 Изменить на узбекский",
        },
    }
    return texts[lang]
