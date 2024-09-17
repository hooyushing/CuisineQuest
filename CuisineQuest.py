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

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Bot token
TOKEN = '-'

# Initialize the updater and dispatcher
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

# Load the hawkers CSV file
hawkers = pd.read_csv('/Users/DELL1/Downloads/Telegram Desktop/Orbital 12 Jun CSV File.csv')

# Conversation states
START, FEATURE, CUISINE, DIETARY, LOCATION, RATING_SELECT, RATING_INPUT, TOP_THREE = range(8)

# Command Handler: start
def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Hello! Welcome to CuisineQuest bot. Type /features to see available instructions")
    return START

# Command Handler: features
def feature_command(update: Update, context: CallbackContext) -> int:
    features_text = (
        "/Location - Choose a location of your liking and discover the best restaurants\n"
        "/dietary_preference - Filter restaurants based on dietary preference\n"
        "/Cuisine - Filter restaurants based on cuisine!\n"
        "/Ratings - Review your favourite restaurants!\n"
        "/Top_three - The top 3 rated restaurants at the moment!"
    )
    update.message.reply_text(features_text)
    return FEATURE

# Command Handler: Dietary Preference
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
            rated = str(updated[rows, 13])
            update.message.reply_text("Your eatery is: " + updated[rows, 3] + " (Rated: " + rated + "/5)")
    else:
        update.message.reply_text('Invalid option! Please use the /dietary_preference command to choose again.')
    return ConversationHandler.END

# Command Handler: Cuisine
def cuisine(update: Update, context: CallbackContext) -> int:
    button1 = KeyboardButton('Asian')
    button2 = KeyboardButton('Western')
    button3 = KeyboardButton('Halal')
    button4 = KeyboardButton('Indian')
    button5 = KeyboardButton('Chinese')
    button6 = KeyboardButton('Korean')
    button7 = KeyboardButton('Japanese')
    button8 = KeyboardButton('Others (Click for surprise!)')
    keyboard = ReplyKeyboardMarkup(
        [[button1], [button2], [button3], [button4], [button5], [button6], [button7], [button8]],
        resize_keyboard=True, one_time_keyboard=True)
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
            rated = str(updated[rows, 13])
            update.message.reply_text("Your eatery is: " + updated[rows, 3] + " (Rated: " + rated + "/5)")
    else:
        update.message.reply_text('Invalid option! Please use the /cuisine command to choose again.')
    return ConversationHandler.END

# Command Handler: Location
def find_eatery(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'These are the available MRT stations you can key in: Admiralty, Aljunied, Ang Mo Kio, Bartley, Bayfront, '
        'Bedok, Bishan, Boon Keng, Boon Lay, Bras Basah, Braddell, Buangkok, Bugis, Buona Vista, Changi Airport, '
        'Choa Chu Kang, Chinese Garden, Chinatown, City Hall, Clarke Quay, Clementi, Commonwealth, Dover, Dhoby Ghaut, '
        'Eunos, Esplanade, Expo, Farrer Park, HarbourFront, Havelock, Hougang, Joo Koon, Jurong East, Kallang, '
        'Kembangan, Keppel, Khatib, Kovan, Kranji, Lakeside, Lavender, Little India, Lorong Chuan, Marina Bay, '
        'Marina South, Marine Parade, Marine Terrace, Marsiling, Maxwell, Mountbatten, Novena, Orchard, Pasir Ris, '
        'Paya Lebar, Pioneer, Potong Pasir, Promenade, Punggol, Queenstown, Raffles Place, Redhill, Sembawang, '
        'Sengkang, Shenton Way, Siglap, Simei, Somerset, Stadium, Suntec City, Tampines, Tanah Merah, Tanjong Katong, '
        'Tanjong Pagar, Toa Payoh, Tiong Bahru, VivoCity, Woodlands, Yew Tee, Yishun')
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
            rated = str(updated[rows, 13])
            update.message.reply_text("Your eatery is: " + updated[rows, 3] + " (Rated: " + rated + "/5)")
    else:
        update.message.reply_text('Invalid location. Please enter a valid location.')
    return ConversationHandler.END


# Command Handler: Top_three
def top_three(update: Update, context: CallbackContext) -> int:
    # Check if the necessary columns exist
    if 'address' not in hawkers.columns or 'rating' not in hawkers.columns:
        update.message.reply_text("Error: 'address' or 'rating' column not found in the data.")
        return ConversationHandler.END
    
    # Sort the DataFrame by the 'Rating' column in descending order and get the top 3 entries
    top_restaurants = hawkers.sort_values(by='rating', ascending=False).head(3)[['address', 'rating']]

    # Check if there are any top restaurants
    if top_restaurants.empty:
        update.message.reply_text("No top-rated restaurants found.")
    else:
        # Create the response message
        response = "Top 3 rated restaurants:\n\n"
        for index, row in top_restaurants.iterrows():
            response += f"{row['address']} - Rated: {row['rating']}/5\n"
        update.message.reply_text(response)
        
    return ConversationHandler.END



# Command Handler: Ratings
def rate_restaurants(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Please enter the name of the restaurant you wish to rate.')
    return RATING_SELECT

def handle_ratings(update: Update, context: CallbackContext) -> int:
    keywords = update.message.text
    pattern = re.compile(keywords, re.IGNORECASE)
    matching_restaurants = hawkers[hawkers['address'].apply(lambda x: bool(pattern.search(x)))]
    matching_names = matching_restaurants['address'].tolist()

    if matching_names:
        buttons = [
            [InlineKeyboardButton(name, callback_data=name)] for name in matching_names
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        update.message.reply_text("Select the restaurant you want to rate:", reply_markup=reply_markup)
        return RATING_INPUT
    else:
        update.message.reply_text("No matching restaurants found. Please send the name again.")
        return RATING_SELECT

def handle_rating(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    context.user_data['restaurant'] = query.data
    query.edit_message_text(text=f"Selected option: {query.data}\n\nPlease send the rating (0-5):")
    return RATING_INPUT

def save_rating(update: Update, context: CallbackContext) -> int:
    restaurant = context.user_data['restaurant']
    rating = update.message.text
    

    if rating.isdigit() and 0 <= int(rating) <= 5:
        total = hawkers.loc[hawkers['address'] == restaurant, 'rating'] * hawkers.loc[hawkers['address'] == restaurant, 'visited']
        hawkers.loc[hawkers['address'] == restaurant, 'visited'] = hawkers.loc[hawkers['address'] == restaurant, 'visited'] + 1
        hawkers.loc[hawkers['address'] == restaurant, 'rating'] = (int(rating) + total)/hawkers.loc[hawkers['address'] == restaurant, 'visited']
        this = float(hawkers.loc[hawkers['address'] == restaurant, 'rating'])
        hawkers.to_csv('/Users/DELL1/Downloads/Telegram Desktop/Orbital 12 Jun CSV File.csv', index=False)
        update.message.reply_text(f"Rating for {restaurant} updated to {this:.2f}.\n\nThank you for contributing!")
    else:
        update.message.reply_text("Invalid rating. Please send a number between 0 and 5.")

    return ConversationHandler.END


# Handles conversation states and interation with user
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        START: [CommandHandler('features', feature_command)],
        FEATURE: [
            CommandHandler('cuisine', cuisine),
            CommandHandler('dietary_preference', dietary_preference),
            CommandHandler('location', find_eatery),
            CommandHandler('Ratings', rate_restaurants),
            CommandHandler('Top_three', top_three)
        ],
        CUISINE: [MessageHandler(Filters.text & ~Filters.command, handle_cuisine)],
        DIETARY: [MessageHandler(Filters.text & ~Filters.command, handle_dietary_preference)],
        LOCATION: [MessageHandler(Filters.text & ~Filters.command, handle_location)],
        RATING_SELECT: [
            MessageHandler(Filters.text & ~Filters.command, handle_ratings),
        ],
        RATING_INPUT: [
            CallbackQueryHandler(handle_rating),
            MessageHandler(Filters.text & ~Filters.command, save_rating)
        ]
    },
    fallbacks=[CommandHandler('start', start)]
)

# Add the conversation handler to the dispatcher
dp.add_handler(conv_handler)

# Start the bot
updater.start_polling()
updater.idle()

















