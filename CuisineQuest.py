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
import re

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s, level = logging.INFO')

TOKEN = '7113953543:AAGsP6zbVPR1kM8AwbU0Jjy7_jt0W5Jlh-A'

updater = Updater(token = TOKEN, use_context = True)

dp = updater.dispatcher

hawkers = pd.read_csv('/Users/DELL1/Downloads/Telegram Desktop/Orbital 12 Jun CSV File.csv')

START, FEATURE, CUISINE, DIETARY, LOCATION, RATING = range(6)


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Hello! Welcome to CuisineQuest bot. Type /features to see available instructions")
    return START

def feature_command(update: Update, context: CallbackContext) -> int:
    features_text = (
       "/Location - Choose a location of your liking and discover the best restaurants\n"
       "/dietary_preference - Filter restaurants based on dietary preference\n"
       "/Cuisine - Filter restaurants based on cuisine!\n"
       "/Ratings - Rate a restaurant!"
    )
    update.message.reply_text(features_text)
    return FEATURE

def dietary_preference(update: Update, context: CallbackContext) -> int:
    button1 = KeyboardButton('Vegan')
    button2 = KeyboardButton('Halal')
    button3 = KeyboardButton('Vegetarian')
    
    
    keyboard = ReplyKeyboardMarkup([[button1], [button2], [button3]], resize_keyboard=True, one_time_keyboard=True)
    
    update.message.reply_text('Please specify if you have any dietary preferences', reply_markup=keyboard)      
    return DIETARY  

def handle_dietary_preference(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    valid_dietary_preferences = ['Vegan', 'Halal', 'Vegetarian']
    if text in valid_dietary_preferences:
        updated = np.array(hawkers.loc[hawkers["Dietary Preferences"] == text])
        if updated.size == 0:
            update.message.reply_text(f'No {text} eateries')
        else:
            rows = random.randint(0, updated.shape[0] - 1)
            update.message.reply_text("Your eatery is: " + updated[rows, 3] + ", ratings: " + updated[rows, 13])
    else:
        update.message.reply_text('Invalid option! Please use the /dietary_preference command to choose again.')
    return ConversationHandler.END    
    

def cuisine(update: Update, context: CallbackContext) -> int:
    button1 = KeyboardButton('Asian')
    button2 = KeyboardButton('Western')
    button3 = KeyboardButton('Halal')
    button4 = KeyboardButton('Indian')
    button5 = KeyboardButton('Chinese')
    button6 = KeyboardButton('Korean')
    button7 = KeyboardButton('Japanese')
    button8 = KeyboardButton('Others (Click for surprise!)')
    
    keyboard = ReplyKeyboardMarkup([[button1], [button2], [button3], [button4], [button5], [button6], [button7], [button8]], resize_keyboard=True, one_time_keyboard=True)
    
    update.message.reply_text('Choose a cuisine to enjoy!', reply_markup=keyboard)
    return CUISINE

def handle_cuisine(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    valid_cuisines = ['Asian', 'Western', 'Halal', 'Indian', 'Chinese', 'Korean', 'Japanese', 'Others']
    if text in valid_cuisines:
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == text])
        if updated.size == 0:
            update.message.reply_text(f'No eateries found with {text} cuisine')
        else:
            rows = random.randint(0, updated.shape[0] - 1)
            update.message.reply_text("Your eatery is: " + updated[rows, 3] + ", ratings: " + updated[rows, 13])
    else:
        update.message.reply_text('Invalid option! Please use the /cuisine command to choose again.')    
    return ConversationHandler.END    




def find_eatery(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('These are the available MRT stations you can key in: Admiralty, Aljunied, Ang Mo Kio, Bartley, Bayfront, Bedok, Bishan, Boon Keng, Boon Lay, Bras Basah, Braddell, Buangkok, Bugis, Buona Vista, Changi Airport, Choa Chu Kang, Chinese Garden, Chinatown, City Hall, Clarke Quay, Clementi, Commonwealth, Dover, Dhoby Ghaut, Eunos, Esplanade, Expo, Farrer Park, HarbourFront, Havelock, Hougang, Joo Koon, Jurong East, Kallang, Kembangan, Keppel, Khatib, Kovan, Kranji, Lakeside, Lavender, Little India, Lorong Chuan, Marina Bay, Marina South, Marine Parade, Marine Terrace, Marsiling, Maxwell, Mountbatten, Novena, Orchard, Pasir Ris, Paya Lebar, Pioneer, Potong Pasir, Promenade, Punggol, Queenstown, Raffles Place, Redhill, Sembawang, Sengkang, Shenton Way, Siglap, Simei, Somerset, Stadium, Suntec City, Tampines, Tanah Merah, Tanjong Katong, Tanjong Pagar, Toa Payoh, Tiong Bahru, VivoCity, Woodlands, Yew Tee, Yishun')
    update.message.reply_text('Please enter your closest MRT Station name.')
    return LOCATION

def handle_location(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    valid_locations = [
        'Admiralty', 'Aljunied', 'Ang Mo Kio', 'Bartley', 'Bayfront', 'Bedok', 'Bishan', 'Boon Keng', 'Boon Lay',
        'Bras Basah', 'Braddell', 'Buangkok', 'Bugis', 'Buona Vista', 'Changi Airport', 'Choa Chu Kang',
        'Chinese Garden', 'Chinatown', 'City Hall', 'Clarke Quay', 'Clementi', 'Commonwealth', 'Dover',
        'Dhoby Ghaut', 'Eunos', 'Esplanade', 'Expo', 'Farrer Park', 'HarbourFront', 'Havelock', 'Hougang',
        'Joo Koon', 'Jurong East', 'Kallang', 'Kembangan', 'Keppel', 'Khatib', 'Kovan', 'Kranji', 'Lakeside',
        'Lavender', 'Little India', 'Lorong Chuan', 'Marina Bay', 'Marina South', 'Marine Parade', 'Marine Terrace',
        'Marsiling', 'Maxwell', 'Mountbatten', 'Novena', 'Orchard', 'Pasir Ris', 'Paya Lebar', 'Pioneer',
        'Potong Pasir', 'Promenade', 'Punggol', 'Queenstown', 'Raffles Place', 'Redhill', 'Sembawang', 'Sengkang',
        'Shenton Way', 'Siglap', 'Simei', 'Somerset', 'Stadium', 'Suntec City', 'Tampines', 'Tanah Merah',
        'Tanjong Katong', 'Tanjong Pagar', 'Toa Payoh', 'Tiong Bahru', 'VivoCity', 'Woodlands', 'Yew Tee', 'Yishun'
    ]
    if text in valid_locations:
        updated = np.array(hawkers.loc[hawkers["Location"] == text])
        if updated.size == 0:
            update.message.reply_text(f'No eateries found near {text}')
        else:
            rows = random.randint(0, updated.shape[0] - 1)
            update.message.reply_text("Your eatery is: " + updated[rows, 3] + ", ratings: " + updated[rows, 13])
    else:
        update.message.reply_text('Invalid location. Please enter a valid location.')
    return ConversationHandler.END    




def rate_restaurants(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Please enter the name of the restaurant you wish to rate.')
    return RATING

def handle_ratings(update: Update, context: CallbackContext) -> int:
    keywords = update.message.text
    pattern = re.compile(keywords, re.IGNORECASE)
    matching_restaurants = df[df['Restaurant Name'].apply(lambda x: bool(pattern.search(x)))]
    matching_names = matching_restaurants['Restaurant Name'].tolist()

    if matching_names:
        update.message.reply_text("Matching Restaurants:\n" + "\n".join(matching_names))
    else:
        update.message.reply_text("No matching restaurants found.")
    return ConversationHandler.END      



conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        START: [CommandHandler('features', feature_command)],
        FEATURE: [
            CommandHandler('cuisine', cuisine),
            CommandHandler('dietary_preference', dietary_preference),
            CommandHandler('location', find_eatery),
            CommandHandler('Review', rate_restaurants)
        ],
        CUISINE: [MessageHandler(Filters.text & ~Filters.command, handle_cuisine)],
        DIETARY: [MessageHandler(Filters.text & ~Filters.command, handle_dietary_preference)],
        LOCATION: [MessageHandler(Filters.text & ~Filters.command, handle_location)],
        RATING: [MessageHandler(Filters.text & ~Filters.command, handle_ratings)]
    },
    fallbacks=[CommandHandler('start', start)]
)

dp.add_handler(conv_handler)

updater.start_polling()
updater.idle()







