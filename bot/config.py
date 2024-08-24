from sqlite import select_info
TOKEN = "7407610854:AAH3xPcbM7t-6dS9BH6NjNNiv-0L7S2_ERk"
r = select_info("main_adminid")
admin = r[0][1] if r != False else "5668945618"