# Introduction 
This webscrapper scraps data from https://stackoverflow.com and converts it into a readable csv file. Data scrapped includes question links, the question titles as well as the time the question was created.
# Requirements
Involves requests ,bs4 and pandas modules for program to work.
# Guide
In the get_questions fucntion, change the tag according to the category you want to scrap. For example, get_questions("python",page) or get_questions("c",page).


To choose the number of pages you want to scrape, in the main function, edit the range parameters accordingly. For example ,for x in range(1,4) will call the program to scrape from page 1 to page 3.
