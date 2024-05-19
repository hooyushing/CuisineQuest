import requests
import time
import datetime
import logging
import telegram
from telegram.ext import *
from telegram import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import preprocessing
import random

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s, level = logging.INFO')

TOKEN = '7113953543:AAGsP6zbVPR1kM8AwbU0Jjy7_jt0W5Jlh-A'

updater = Updater(token = TOKEN, use_context = True)

dp = updater.dispatcher

hawkers = pd.read_csv('/Users/DELL1/Downloads/Telegram Desktop/Updated List Of Hawker Centers.csv')


def start(update, context):
    update.message.reply_text("Hello! Welcome to CuisineQuest bot. Type /features to see available instructions")

def feature_command(update, context):
    features_text = (
       "/Location - Choose a location of your liking and discover the best restaurants\n"
       "/Dietary preference - Filter restaurants based on dietary preference\n"
       "/Review - Review your favourite restaurants!"
    )
    update.message.reply_text(features_text)
    

def location(update, context):
    button1 = KeyboardButton('North')
    button2 = KeyboardButton('South')
    button3 = KeyboardButton('East')
    button4 = KeyboardButton('West')
    button5 = KeyboardButton('Central')
    keyboard = ReplyKeyboardMarkup([[button1], [button2], [button3], [button4], [button5]], resize_keyboard=True, one_time_keyboard=True)
    
    update.message.reply_text('Choose a direction to find restaurants:', reply_markup=keyboard)

def handle_message(update, context):
    text = update.message.text
    if text == 'North':
        update.message.reply_text('Searching for restaurants in the North!')
        updated = np.array(hawkers.loc[hawkers["Location"] == "North"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 0] + " (" + updated[rows, 2] + ")")
    elif text == 'South':
        update.message.reply_text('Searching for restaurants in the South!')
        updated = np.array(hawkers.loc[hawkers["Location"] == "South"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 0] + " (" + updated[rows, 2] + ")")
    elif text == "West":
        update.message.reply_text('Searching for restaurants in the West!')
        updated = np.array(hawkers.loc[hawkers["Location"] == "West"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 0] + " (" + updated[rows, 2] + ")")
    elif text == 'East':
        update.message.reply_text('Searching for restaurants in the East!')
        updated = np.array(hawkers.loc[hawkers["Location"] == "East"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        
        update.message.reply_text("Your food place is: " + updated[rows, 0] + " (" + updated[rows, 2] + ")")
    elif text == 'Central':
        update.message.reply_text('Searching for restaurants in the Central')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Central"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        
        update.message.reply_text("Your food place is: " + updated[rows, 0] + " (" + updated[rows, 2] + ")")
    else:
        update.message.reply_text('Invalid option! Please use the /location command to choose again.')
        
    





dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("features", feature_command))
dp.add_handler(CommandHandler("Location", location))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()





