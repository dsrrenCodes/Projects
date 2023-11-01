
# Scrapping Linkedin job offers using Selenium

Using Selenium, this sophisticated program seamlessly logs into the user's LinkedIn account via a headless browser, providing seamless access to the "Jobs" department.

Leveraging the power of Selenium, this application skillfully extracts valuable data from the website, including essential details such as the job title, job type (internship, full-time, part-time, etc.), the company name, the timestamp when the job was listed on the website (if available), and convenient links for users to access additional information

With the help of pandas, this program not only navigates LinkedIn effortlessly but also efficiently compiles the extracted data into a CSV file, making it easily readable in Excel or other compatible spreadsheet software.


![Screenshot (6)](https://github.com/dsrrenCodes/webscrapingprojects/assets/120300295/2abd2188-f5d7-4b39-a237-ba439ed9c73d)





## Setting up Selenium
To get started with Selenium, you'll need to set up two essential elements: the Selenium package designed for Python and the browser driver that corresponds to the web browser of your choice.

To download selenium, in your terminal, execute pip install selenium.

You can find the links to download the drivers for Firefox, Chrome, and Edge: https://pypi.org/project/selenium/#drivers

Ensure you download the correct version that corresponds to the version of your web browser you intend to use.

## Other requirements
Requires the time, random and pandas modules








## Tutorial/Modifying the program



To login to Linkedin, enter your user and password in line 12 and 14 respectively.

To modify the program according to number of pages to scrap / type of job / country, follow through my comments in my code (under line 20 and 21) 



