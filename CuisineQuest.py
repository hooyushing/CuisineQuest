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
    button8 = KeyboardButton('Others (Click for surprise!)')
    
    keyboard = ReplyKeyboardMarkup([[button1], [button2], [button3], [button4], [button5], [button6], [button7], [button8]], resize_keyboard=True, one_time_keyboard=True)
    
    update.message.reply_text('Choose a cuisine to enjoy!', reply_markup=keyboard)

def handle_message(update, context):
    text = update.message.text
    if text == 'Asian':
        update.message.reply_text('Searching for Asian restaurants')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Asian"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Halal':
        update.message.reply_text('Searching for Halal restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Halal"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Western':
        update.message.reply_text('Searching for Western restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Western"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Japanese':
        update.message.reply_text('Searching for Japanese restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Japanese"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Korean':
        update.message.reply_text('Searching for Korean restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Korean"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Chinese':
        update.message.reply_text('Searching for Chinese restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Chinese"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Indian':
        update.message.reply_text('Searching for Indian restaurants!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Indian"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Others':
        update.message.reply_text('Surprise!')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Others"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    else:
        update.message.reply_text('Invalid option! Please use the /location command to choose again.')
        


def location(update, context):
    update.message.reply_text('These are the available MRT stations you can key in: Admiralty, Aljunied, Ang Mo Kio, Bartley, Bayfront, Bedok, Bishan, Boon Keng, Boon Lay, Bras Basah, Braddell, Buangkok, Bugis, Buona Vista, Changi Airport, Choa Chu Kang, Chinese Garden, Chinatown, City Hall, Clarke Quay, Clementi, Commonwealth, Dover, Dhoby Ghaut, Eunos, Esplanade, Expo, Farrer Park, HarbourFront, Havelock, Hougang, Joo Koon, Jurong East, Kallang, Kembangan, Keppel, Khatib, Kovan, Kranji, Lakeside, Lavender, Little India, Lorong Chuan, Marina Bay, Marina South, Marine Parade, Marine Terrace, Marsiling, Maxwell, Mountbatten, Novena, Orchard, Pasir Ris, Paya Lebar, Pioneer, Potong Pasir, Promenade, Punggol, Queenstown, Raffles Place, Redhill, Sembawang, Sengkang, Shenton Way, Siglap, Simei, Somerset, Stadium, Suntec City, Tampines, Tanah Merah, Tanjong Katong, Tanjong Pagar, Toa Payoh, Tiong Bahru, VivoCity, Woodlands, Yew Tee, Yishun')
    update.message.reply_text('Please enter your closest MRT Station name.')
    
    

def handle_message(update, context):
    text = update.message.text
    if text == 'VivoCity':
        update.message.reply_text('Searching for restaurants near VivoCity')
        updated = np.array(hawkers.loc[hawkers["Location"] == "VivoCity"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'HabourFront':
        update.message.reply_text('Searching for restaurants near HabourFront')
        updated = np.array(hawkers.loc[hawkers["Location"] == "HabourFront"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Keppel':
        update.message.reply_text('Searching for restaurants near Keppel')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Keppel"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Tanjong Pajar':
        update.message.reply_text('Searching for restaurants near Tanjong Pajar')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Tanjong Pajar"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Shenton Way':
        update.message.reply_text('Searching for restaurants near Shenton Way')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Shenton Way"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Tiong Bahru':
        update.message.reply_text('Searching for restaurants near Tiong Bahru')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Tiong Bahru"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Clementi':
        update.message.reply_text('Searching for restaurants near Clementi')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Clementi"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Jurong East':
        update.message.reply_text('Searching for restaurants near Jurong East')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Jurong East"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Maxwell':
        update.message.reply_text('Searching for restaurants near Maxwell')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Maxwell"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Toa Payoh':
        update.message.reply_text('Searching for restaurants near Toa Payoh')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Toa Payoh"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Buona Vista':
        update.message.reply_text('Searching for restaurants near Buona Vista')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Buona Vista"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Boon Lay':
        update.message.reply_text('Searching for restaurants near Boon Lay')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Boon Lay"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Somerset':
        update.message.reply_text('Searching for restaurants near Somerset')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Somerset"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Orchard':
        update.message.reply_text('Searching for restaurants near Orchard')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Orchard"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Choa Chu Kang':
        update.message.reply_text('Searching for restaurants near Choa Chu Kang')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Choa Chu Kang"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Commonwealth':
        update.message.reply_text('Searching for restaurants near Commonwealth')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Commonwealth"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Chinatown':
        update.message.reply_text('Searching for restaurants near Chinatown')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Chinatown"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Marina South':
        update.message.reply_text('Searching for restaurants near Marina South')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Marina South"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Havelock':
        update.message.reply_text('Searching for restaurants near Havelock')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Havelock"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Pioneer':
        update.message.reply_text('Searching for restaurants near Pioneer')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Pioneer"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Boon Keng':
        update.message.reply_text('Searching for restaurants near Boon Keng')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Boon Keng"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Redhill':
        update.message.reply_text('Searching for restaurants near Redhill')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Redhill"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Clarke Quay':
        update.message.reply_text('Searching for restaurants near Clarke Quay')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Clarke Quay"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Queenstown':
        update.message.reply_text('Searching for restaurants near Queenstown')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Queenstown"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])   
    elif text == 'Dover':
        update.message.reply_text('Searching for restaurants near Dover')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Dover"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4]) 
    elif text == 'Eunos':
        update.message.reply_text('Searching for restaurants near Eunos')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Eunos"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])      
    elif text == 'Bedok':
        update.message.reply_text('Searching for restaurants near Bedok')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Bedok"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])    
    elif text == 'Marina Bay':
        update.message.reply_text('Searching for restaurants near Marina Bay')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Marina Bay"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4]) 
    elif text == 'Raffles Place':
        update.message.reply_text('Searching for restaurants near Raffles Place')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Raffles Place"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4]) 
    elif text == 'Suntec City':
        update.message.reply_text('Searching for restaurants near Suntec City')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Suntec City"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4]) 
    elif text == 'Bugis':
        update.message.reply_text('Searching for restaurants near Bugis')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Bugis"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4]) 
    elif text == 'Dhoby Ghaut':
        update.message.reply_text('Searching for restaurants near Dhoby Ghaut')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Dhoby Ghaut"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])  
    elif text == 'Kallang':
        update.message.reply_text('Searching for restaurants near Kallang')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Kallang"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4]) 
    elif text == 'City Hall':
        update.message.reply_text('Searching for restaurants near City Hall')
        updated = np.array(hawkers.loc[hawkers["Location"] == "City Hall"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Esplanade':
        update.message.reply_text('Searching for restaurants near Esplanade')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Esplanade"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4]) 
    elif text == 'Sembawang':
        update.message.reply_text('Searching for restaurants near Sembawang')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Sembawang"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])    
    elif text == 'Hougang':
        update.message.reply_text('Searching for restaurants near Hougang')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Hougang"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])      
    elif text == 'Lavender':
        update.message.reply_text('Searching for restaurants near Lavender')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Lavender"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])                                   
    elif text == 'Woodlands':
        update.message.reply_text('Searching for restaurants in Woodlands')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Woodlands"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Ang Mo Kio':
        update.message.reply_text('Searching for restaurants in Ang Mo Kio')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Ang Mo Kio"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Joo Koon':
        update.message.reply_text('Searching for restaurants in Joo Koon')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Joo Koon"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Yishun':
        update.message.reply_text('Searching for restaurants in Yishun')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Chinese"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Admiralty':
        update.message.reply_text('Searching for restaurants in Admiralty')
        updated = np.array(hawkers.loc[hawkers["CuisineUpdated"] == "Indian"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Marsiling':
        update.message.reply_text('Searching for restaurants in Marsiling')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Marsiling"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Canberra':
        update.message.reply_text('Searching for restaurants in Canberra')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Canberra"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Lakeside':
        update.message.reply_text('Searching for restaurants in Lakeside')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Lakeside"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Yew Tee':
        update.message.reply_text('Searching for restaurants in Yew Tee')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Yew Tee"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Farrer Park':
        update.message.reply_text('Searching for restaurants in Farrer Park')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Farrer Park"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Siglap':
        update.message.reply_text('Searching for restaurants in Siglap')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Siglap"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Marine Terrace':
        update.message.reply_text('Searching for restaurants in Marine Terrace')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Marine Terrace"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Kembangan':
        update.message.reply_text('Searching for restaurants in Kembangan')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Kembangan"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Tampines':
        update.message.reply_text('Searching for restaurants in Tampines')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Tampines"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Simei':
        update.message.reply_text('Searching for restaurants in Simei')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Simei"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Changi Airport':
        update.message.reply_text('Searching for restaurants in Changi Airport')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Changi Airport"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Pasir Ris':
        update.message.reply_text('Searching for restaurants in Pasir Ris')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Pasir Ris"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Expo':
        update.message.reply_text('Searching for restaurants in Expo')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Expo"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Chinese Garden':
        update.message.reply_text('Searching for restaurants in Chinese Garden')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Chinese Garden"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Tanah Merah':
        update.message.reply_text('Searching for restaurants in Tanah Merah')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Tanah Merah"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Bishan':
        update.message.reply_text('Searching for restaurants in Bishan')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Bishan"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Potong Pasir':
        update.message.reply_text('Searching for restaurants in Potong Pasir')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Potong Pasir"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Braddell':
        update.message.reply_text('Searching for restaurants in Braddell')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Braddell"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Bras Basah':
        update.message.reply_text('Searching for restaurants in Bras Basah')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Bras Basah"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Potong Pasir':
        update.message.reply_text('Searching for restaurants in Potong Pasir')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Potong Pasir"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Lorong Chuan':
        update.message.reply_text('Searching for restaurants in Lorong Chuan')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Lorong Chuan"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Bartley':
        update.message.reply_text('Searching for restaurants in Bartley')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Bartley"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Little India':
        update.message.reply_text('Searching for restaurants in Little India')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Little India"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Kovan':
        update.message.reply_text('Searching for restaurants in Kovan')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Kovan"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Punggol':
        update.message.reply_text('Searching for restaurants in Punggol')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Punggol"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Buangkok':
        update.message.reply_text('Searching for restaurants in Buangkok')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Buangkok"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Sengkang':
        update.message.reply_text('Searching for restaurants in Sengkang')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Sengkang"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Khatib':
        update.message.reply_text('Searching for restaurants in Khatib')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Khatib"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Tanjong Katong':
        update.message.reply_text('Searching for restaurants in Tanjong Katong')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Tanjong Katong"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Aljunied':
        update.message.reply_text('Searching for restaurants in Aljunied')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Aljunied"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Mountbatten':
        update.message.reply_text('Searching for restaurants in Mountbatten')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Mountbatten"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Marine Parade':
        update.message.reply_text('Searching for restaurants in Marine Parade')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Marine Parade"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Stadium':
        update.message.reply_text('Searching for restaurants in Stadium')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Stadium"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Bayfront':
        update.message.reply_text('Searching for restaurants in Bayfront')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Bayfront"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Novena':
        update.message.reply_text('Searching for restaurants in Novena')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Novena"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Paya Lebar':
        update.message.reply_text('Searching for restaurants in Paya Lebar')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Paya Lebar"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    elif text == 'Promenade':
        update.message.reply_text('Searching for restaurants in Promenade')
        updated = np.array(hawkers.loc[hawkers["Location"] == "Promenade"])
        size = updated.shape
        rows = random.randint(0, size[0] - 1)
        update.message.reply_text("Your eatery is: " + updated[rows, 4])
    else:
        update.message.reply_text('Enter a valid restaurant')



dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("features", feature_command))
dp.add_handler(CommandHandler("Cuisine", cuisine))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
dp.add_handler(CommandHandler("Location", location))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()





