# Swami
[![scraper: gazpacho](https://img.shields.io/badge/scraper-gazpacho-C6422C)](https://github.com/maxhumber/gazpacho)
## Intro
In a world encompassed in probabilities and statistics all stacked against you, many people are looking for any type of slim edge to get ahead of their opponent to beat them at their own game. Machine learning and artificial intelligence have become double agents in the world of gambling and gambling theory; helping both sides get the edge over their opponent. We will explore the present role Machine learning has had on the gambling industry and its role in influencing the future of the gambling industry.
Being able to predict the outcome of a game that has several unquantifiable and unpredictable components is innately difficult, but can become easier with the use of the vast data available on the internet and machine learning. Since pro-football is the most popular major sport in the United States in both terms of views and to bet on; this paper will primarily focus on predicting the outcome of NFL games using many methods in machine learning.  
The purpose of this project is to investigate the influence and impact of Artificial Intelligence within the gaming industry and gambling theory. While probing what current impacts Artificial Intelligence has within the gaming industry and what potential authority it might assemble in the coming years. Machine learning within the industry is already here but the better question should how will it transform the landscape of gambling and will it shift the power to the consumer/bettor or will the same power dynamics exist in 10 years?
Can Artificial Intelligence consistently predict who will win an NFL game and if so can that same model be used to predict if that winner will cover the vegas spread? A similar study, a machine learning model was developed to predict outcomes of the English twenty over county cricket cup over the years 2009-2014(Kampakis & Thomas, 2015). Will the best model for predicting a different sport be the same?
Predicting the new emerging and quickly expanding industry of sports betting has become the new and hot industry to get into before the market gets too saturated. Investors and sports betting companies are running up the score when it comes to sports betting, predicting the fast-growing industry will be a $7 billion to $8 billion business in the U.S. within five years (Associated Press, 2019).  Forecasting the winner or loser correctly using machine learning can generate significant profit if done correctly.

## Data collection
The dataset i used for this project with the help of webscaping python library gazpacho and the wounderful stat collection website [Pro-Football-Reference](https://www.pro-football-reference.com/)

I ultimately retrieving data from 2002 to 2019 and ran into a few road blocks along the way. The first issue i ran into was assuming all of the pages from 2002 to current were the same layout and i figure that out really fast when testing a look for 2017-2019. The main issues were coming from the boxscore links and mainly the the advanced Passing Table. The advanced passers table was only available for the most current year so i forewent that table and decided to focus on the 3 other tables (Game Info, Team Stats, and Passing/Rushing/and Receiving)


## Data Cleaning

I ended up collecting every single game played from 2002 to 2019/2020 seasons which means there are duplicate game stats. To remove these duplicate games I decided to drop every away game row. Which a "smaller" dataset and some EDA/Visualization done i mored onto model Selection. And this was the moment i realized i need to do more data engineering if i wanted to be able to predict the outcome **BEFORE** the game started. Everything collected up to this point were post game / in game stats and since i am not Miss Cleo and know these number before the game i had to create a dataset that i could train with data i would know before the game. To fix this issue I had to go back to the source data and create a rolling mean using the first four games of the season.

## Models

SVM <br>
Random Forests <br>
NN


## To-Do
- [ ] Cut down massive number of features
- [ ] S3 for data storage (boto)
- [ ] Sage maker to host and deploy trained models
