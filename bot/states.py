from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Pay(StatesGroup):
    payment = State()
    location = State()
    
class OlPay(StatesGroup):
    location = State()
    
class InfoSave(StatesGroup):
    contact = State()
    
class SendUsersMessage(StatesGroup):
    mess = State()