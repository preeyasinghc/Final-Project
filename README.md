**Project Title**: Optimising User Engagement for App Subscription Conversion

**Case Study**:
In today's market many companies have a mobile presence. Often, these companies provide free products/services in their mobile apps in an attempt to transition their customers to a paid membership. Some examples of paid products, which originate from free ones, are YouTube Red, Pandora Premium, Audible Subscription, YouTube Premium, and You Need a Budget. Since marketing efforts are never free, these companies need to know exactly who to target with offers and promotions
**Market**: The target audience is customers who use a company's free products. In this case study, this refers to users who installed (and used) the companies free mobile app.
**Product:** The paid memberships often provide enhanced versions of the free products already given for free, alongside new features. For example, Youtube Red allows you to leave the app while still listening to a video.
**Goal:** The objective of this model is to predict which users will not subscribe to the paid membership, so that greater marketing efforts can go into trying to convert them to paid users.


**Business Challenge:**
In this Case Study we will be working for a fintech company that wants to provide its customers with a paid mobile app subscription that will allow them to track all of their finances in one place. To attract customers, the company releases a free version of their app with some of the main features unlocked.
The company has tasked you to identify which users will mostly likely NOT enroll in paid products, so that additional offers can be given to them. Because of the costs of these offers, the company does not want to offer them to everybody, especially customers who were going to enroll anyways.

**Dataset**: Source Kaggle.com

**App Data:**
By working for the company. We have access to each customer's app behavior data. This data allows us to see the date & time of app installation, as well as the features the users engaged with within the app. App behavior is characterized as the list of app screens the user looked at, and whether the user played the financial mini-games available.
The app usage data is only from the user's first day in the app. This limitation exists because users can enjoy a 24-hour free trial of the premium features, and the company wants to target them with new offers shortly after the trail is over.
The Data for this project is from manufacturing fields based on trends found in real world case studies. The fields describe what companies usually track from their users.

**Data Description:**
**User** : this is Unique id of each perticuter user of app
**first_open** :this is the date/month/year, time the user frist time open the app
**dayofweek** : this shows the day out of 7 days a week an user join the app where 0:Sunday & 6:Saturday
**hour**: This is outoff 24 hour of day the user 1st open the app
**age** : This is simply the age of the user
**screen_list** : This describe the every single screen name the user visited in that 1st 24-hour (screen name seperated by comma)
**numscreens** : The Number of screen the user visited in 1st 24 hour
**minigame** : The app has minigame feature, this shows whether the player played any minigame of Not (1:Played, 0: Not Played)
**liked** : There are like button for each feature in the app, shows whether the user cliked any like button of any feature in app or NOT (1: click like button, 0: Not clicked)
**used_premium_feature** : This shows whether the user used any premium feature (that is for free in 1st 24 hour) or not in 1st 24 hour (1: used, 0: not used)
**enrolled** : This is target that shows whether the user enrolled to premium after the free trial (1: enrolled, 0: not enrolled)
**enrolled_date** : date & time of enrollment to premium product if they enrolled to premium

**Getting Started**: Performed Data Cleaning, Data Preprocessing, Feature Engineering and Data visualisations on Tableau
 
**Models and Predictions:**
We did Model Building using Logistic Regression, Random Forest and XGBoost classifier
1. Evaluated the Results
2. HeatMap Visualisation using confusion matrix
3. Applied K-fold cross Validation
4. Hyperparameter Tuning
5. Format the Results in three columns: User, Enrolled and Predicted Results

**Project Deliverables:**
A python notebook in github
Power point presentation of the project
Analysis on Tableau of different parameters and in dashboard for the comparison.
Tableau Link: (https://public.tableau.com/app/profile/preeya.singh.chauhan/viz/Customer_App_Subscription/Dashboard1?publish=yes
Final product: 
Sreamlit App: https://customer-app-subscription-prediction.onrender.com/







