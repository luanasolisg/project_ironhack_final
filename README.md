# final_project_ironhack

## Introduction

The objective of this final project is to carry out an automatic analysis of the prices of certain products. The structure of this project will have three different parts:
- Scrape three different product references on three different websites.
- Create a data base with the scrap results.
- Analyze if the different prices are the retail recomended price that the company gives for each retailer.
All this process will be automatically done every day.

## Scraping:

We are going to scrape three different website () and look in each of them three different products (). For the scraping we are going to use Selenium and the result of the scrape will be a csv for each website.

## Creating a data base:

Once the scraping has been done, our script will generate Total data base wich will include all the different csv that have been generetated from our scraping.

## Analyzing:

We will use Power BI to analyze if the different prices we hhave obtained are the retail recomended price that the company gives to each retailer or if there is any variance. If there is any variance on this we will see an alert that will help us internally to talk with the different retailers.

## Automatization:

As we want this process done every day, we will use crontab to mae it happen every day at 12:00.

 
