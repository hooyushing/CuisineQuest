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

hawkers = pd.read_csv('/Users/DELL1/Downloads/updated-2.csv')


def start(update, context):
    update.message.reply_text("Hello! Welcome to CuisineQuest bot. Type /features to see available instructions")

def feature_command(update, context):
    features_text = (
       "/Location - Choose a location of your liking and discover the best restaurants\n"
       "/Dietary preference - Filter restaurants based on dietary preference\n"
       "/Cuisine - Filter restaurants based on cuisine!\n"
       "/Review - Review your favourite restaurants!"
    )
    update.message.reply_text(features_text)
    

def cuisine(update, context):
    button1 = KeyboardButton('Asian')
    button2 = KeyboardButton('Western')
    button3 = KeyboardButton('Halal')
    button4 = KeyboardButton('Indian')
    button5 = KeyboardButton('Chinese')
    button6 = KeyboardButton('Korean')
    button7 = KeyboardButton('Japanese')
    button8 = KeyboardButton('Others (Click for surprise)')
    
    keyboard = ReplyKeyboardMarkup([[button1], [button2], [button3], [button4], [button5], [button6], [button7], [button8]], resize_keyboard=True, one_time_keyboard=True)
    
    update.message.reply_text('Choose a direction to find restaurants:', reply_markup=keyboard)

def handle_message(update, context):
    text = update.message.text
    if text == 'Asian':
        update.message.reply_text('Searching of Asian restaurants')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Asian"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    elif text == 'Halal':
        update.message.reply_text('Searching for Halal restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Halal"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    elif text == 'Western':
        update.message.reply_text('Searching for Western restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Western"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    elif text == 'Japanese':
        update.message.reply_text('Searching for Japanese restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Japanese"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    elif text == 'Korean':
        update.message.reply_text('Searching for Korean restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Korean"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    elif text == 'Chinese':
        update.message.reply_text('Searching for Chinese restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Chinese"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    elif text == 'Indian':
        update.message.reply_text('Searching for Indian restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Indian"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    elif text == 'Others':
        update.message.reply_text('Surprise!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Others"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your food place is: " + updated[rows, 2] + " (" + updated['address'] + ")")
    else:
        update.message.reply_text('Invalid option! Please use the /location command to choose again.')
        
    





dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("features", feature_command))
dp.add_handler(CommandHandler("Cuisine", cuisine))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()





