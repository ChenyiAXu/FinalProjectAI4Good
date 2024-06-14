# Project: Food Insecurity

## [Dataset](https://github.com/ChenyiAXu/FinalProjectAI4Good/blob/main/Scraped%20Data/product_data.csv)
This dataset features 16,277 everyday grocery items scraped from three prominent chains: No Frills, The Real Canadian Superstore, and Save On Foods, key players in British Columbia's grocery market. It offers a broad spectrum of products, ranging from standard essentials to specialty items, including halal, vegetarian, vegan, and kosher options. This diverse compilation provides valuable insights into consumer preferences and trends within the grocery industry, making it a rich resource for analysis and exploration.
## [Pre-data Processing](https://github.com/ChenyiAXu/FinalProjectAI4Good/blob/main/Data%20Processing/predata_processing.ipynb) 
The raw datasets obtained through web scraping are meticulously processed using the Python libraries pandas and numpy. This processing includes segregating the data into four distinct CSV files corresponding to the store origin: Save On Foods, Superstore, No Frills, and a combined file that aggregates the data from all sources.Each dataset comprises the following columns: Title, Price, Category, Store, Price per Unit, Per Unit Quantity, and Unit Type. 
## Frontend
### Contact Us Page
This is a contact form created using **CSS**, **HTML**, and **JavaScript**, utilizing **EmailJS** as an API. When the contact form is submitted, the information will be sent to the team as an email, and the sender will receive an automated email.
#### Setup Instructions
**EmailJS Setup:**
1. Create an account on EmailJS.
2. Set up a new service and a new email template on your EmailJS dashboard.
3. Copy your **Service ID**, **Template ID**, and **Public Key** from the dashboard.
**Update HTML:**
1. Replace `'YOUR_SERVICE_ID'` and `'YOUR_TEMPLATE_ID'` in the code with your actual Service ID and Template ID.
2. Ensure the Public Key in `emailjs.init("DeK-jvsecVsFBEyT3");` is correct or replace it with your own.

