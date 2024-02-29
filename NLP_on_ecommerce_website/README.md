![image](https://github.com/dsrrenCodes/webscrapingprojects/assets/120300295/144a0295-56fd-46fa-8ed4-03daf369b903)
## Project 

This project represents my personal interest in integrating web scraping with sentiment analysis to gather a public consensus on a laptop that I am currently considering for purchase. Why watch youtube videos on it when i can code it!



The laptop in question:
Lenovo Legion 5 Pro





![Legion laptop](https://github.com/dsrrenCodes/webscrapingprojects/assets/120300295/6084ef1a-28fc-4fcd-a2ee-ed1049ad5a03)





I have seperated the project into 3 parts.

    1. Web scraping using BeautifulSoup and Selenium
    
    2. Cleaning Data using Pandas

    3. Sentimental Analysis using VADERS and WordCloud


# So Why VADERS ?

VADERS(Valence Aware Dictionary and sEntiment Reasoner) is tool designed for sentiment analysis in natural language processing.

It uses a lexicon to assign sentiment scores to words, considering intensity and context. It's effective for analyzing informal language due to its handling of slang, emoticons, and punctuation.

This makes it a perfect tool in empowering me to make better decisions in weather i should buy this laptop brand or not! 



## My Discoveries

 Among all the different models, I found that the Lenovo Legion 5 Pro AMD Ryzen 7 Octa Core 6800H 32GB/1TB model was the most well liked. This can be shown through the boxplot below.


![SentimentalAnalysis](https://github.com/dsrrenCodes/webscrapingprojects/assets/120300295/e5e64b05-c8d1-456a-b038-6821e17b8dd2)




 The higher-priced products utilized in this project have garnered a more favorable reception in comparison to their lower-priced counterparts. This is proven by the line plot below. There cpild be a presence of purchase bias that could skew the sentiment analysis results towards favoring more expensive products over their less pricey counterparts.

 


![LinePlot](https://github.com/dsrrenCodes/webscrapingprojects/assets/120300295/6494dbb7-f659-4f30-8d82-3f347a7436dc)


Overall, the laptop model tends to be highly favored by customers, with a higher frequency of positive words observed in their reviews. This can be seen using the Word Cloud Plot below.

![wordcloud](https://github.com/dsrrenCodes/webscrapingprojects/assets/120300295/b24fc151-406b-4f45-9b5d-e7269d370db6)

