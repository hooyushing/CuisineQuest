Cuisine Quest


Hoo Yu Shing 
Wong Wai Hin 

Proposed level of achievement: Gemini
Aim: The aim of CuisineQuest is to provide personalized restaurant recommendations to users, making it easier for them to discover and choose dining options that suit their tastes and preferences. By leveraging technology and user input, the bot aims to enhance the dining experience by offering tailored suggestions.
Motivation: The motivation behind CuisineQuest is to address the challenge many people face when deciding where to eat. With countless dining options available, it can be overwhelming to choose the right restaurant. CuisineQuest was created to simplify this process by offering curated recommendations based on location, cuisine preferences, dietary needs, and user reviews. This helps users make informed decisions quickly and enjoy a satisfying dining experience.







Target Audience
The target audience for CuisineQuest includes:
Food Enthusiasts: Individuals who enjoy exploring new dining experiences and discovering diverse cuisines.
Travelers: People visiting new areas who need reliable restaurant recommendations.
Health-Conscious Individuals: Users with specific dietary preferences such as vegetarian, vegan, or gluten-free diets.
Social Diners: People who enjoy sharing their dining experiences and recommendations with friends and family via social media platforms like Telegram.
Local Residents: Those looking for top-rated dining spots within their vicinity or when exploring different neighborhoods.
By focusing on these groups, CuisineQuest aims to become a go-to resource for anyone looking to enhance their dining experiences with personalized and trustworthy recommendations.




User Stories
User Story for Location-Based Suggestions:
As a frequent traveler, I want the bot to pinpoint restaurants near me so that I can find great dining options quickly wherever I am.
User Story for Cuisine Filtering:
As a food enthusiast with varied tastes, I want the bot to filter restaurants by different cuisines so that I can explore new culinary experiences that match my preferences.
User Story for Dietary Preferences:
As a health-conscious diner, I want the bot to filter restaurants by dietary options like vegetarian, vegan, or gluten-free so that I can find meals that align with my dietary needs and preferences.
User Story for Social Sharing:
As a member of a food-loving community, I want the bot to allow me to share restaurant recommendations with my contacts on Telegram so that we can exchange dining insights and personal favorites.
User Story for Ratings and Reviews:
As a diner looking for the best spots, I want the bot to show user-generated ratings and reviews so that I can make informed decisions based on others' experiences.

Details of feature implementation
Location Based Suggestions (Completed): 
Currently our location based suggestion feature requires the user to input the MRT station closest to their current location. Using this information, the bot then searches through the data set we input to find a match. (our data set has a location column for every restaurant in the input) From here we narrow the list of restaurants that has matching information regarding the location. Our bot then randomly outputs anyone of the restaurants that matches the location input.
Cuisine/Dietary Based Suggestions (Completed):
Our Dietary based suggestion feature takes into account the user dietary requirements. Users are able to get a random restaurant based on their dietary preferences and cuisine that they selected, based on a button-based system. When users select the button of their preferred cuisine, a restaurant name and location is returned.
User Ratings (Almost Completed):
Our CSV file database approach allows us to update the ratings of a restaurant through indexing the column of the restaurant selected. Then, the total number of people who rated and the average ratings is collated based on the number of individuals who rated the restaurant. The rating system is out of a total score of 5.


Overall software: CSV database
We tested the CSV database by randomly indexing and selecting data from the database in jupyter notebook. By using basic data analysis tools with python, we were able to clean the dataset (Taken from Grab public dataset) and get a better overview on the details of the dataset. This gave us a better insight on the available information of the dataset. We also added in our own columns filled with specific data in order to aid querying from the dataset. This features will the explained in the following paragraphs
Feature 1: Location Based indexing
The initial idea of such a location based indexing system was to segregate the restaurants into North, South, East and West Areas. This would allow a simpler button based system that would allow user to pick a restaurant from the region they were in. However, upon further consideration, the North, South, East and West directions were too generic and the restaurant may not be near the user.

We decided to change the code such that a specific MRT station is used instead. We added a column to segregate the restaurants into regions belonging to specific MRT stations to the dataset. This allowed us to select restaurants from the nearest MRT station that the user input into the system. The evidence of unit testing of this function is shown below.





Feature 2: Cuisine Based/Dietary Preference Indexing:
The idea of such a feature was to allow users to pick a restaurant based on the specified cuisine of dietary requirements. We used a button based approach to limit users to specific dietary requirements or cuisine preferences. We created a new column to classify the restaurants based on the dietary requirements that were available. This was done using excel VBA to extract the data from other columns and classify the data into specific dietary preferences.
Next, based on the newly created columns, we were able to index and reduce the size of the dataset based on the preferences of the user. This allowed us to randomly select a good restaurant from the pool and recommend it to the user. The code is as such:










This was the evidence of unit testing:

Feature 3: User Ratings
The user ratings feature is still a work in progress. We decided to use regular expressions to narrow down the restaurants that the user would like to review, in order to select the accurate restaurant the user wanted to review. This allows the correct restaurant to be selected in the CSV file. We are still working on the storage of data for the past reviews.
Code:

Unit Testing:
    
Proof of Software Engineering
Modular Design: The code is organized into functions, each of which performs an individual task. Based on the separation of the code according to the features, this makes it easier to understand, test and maintain the code. Editing individual functions will not affect the functionality of the rest of the code.
State Management: The bot uses a ConversationHandler to manager the conversations with the user. The ConversationHandler has multiple states. This will each represent the multiple steps of the conversation. In relation to the conversation with the individual, each state is associated to a function which handles the user’s input.
Data Validation: The bot validates the user inputs before processing the information, it ascertain that a valid input is entered before carrying out the action, which prevents errors later into the process.
Error Handling: Using regular expression, the bot includes error handling code to deal with unexpected situations.
Tech Stack
Python: The bot is developed using python, which is a suitable language for data processing and automation.
Python-telegram-bot: The library provides a python interface for the Telegram Bot API and is compatible with the development of the project
Pandas and Numpy: Pandas and Numpy are effective libraries for data manipulation and extraction, in order to access the dataset and index the right restaurant
Regular Expression (re): Regular expression is commonly used to select similar words and phrases input into the system from the dataset. This will narrow down the search results in the dataset.
CSV: The dataset is stored in a CSV file.




