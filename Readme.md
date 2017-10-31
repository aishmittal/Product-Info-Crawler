# Product-Info-Crawler
Product-Info-Crawler is a python web crwaler developed using scrapy framework. It has four spiders for crawling the search results from olx.in, amazon.in, ebay.in and shopclues.com. The crawler extract the product names, price, image urls, product urls and source and stores them in a scv file named `results.csv`. It can be useful for comapairing the price of a particular product between different e-commerce websites.

## Install Dependencies

### Windows
1. Install Python2.7 (Download from https://www.python.org/downloads/)
2. Install pip (Follow instructions here https://pip.pypa.io/en/stable/installing/)
3. Install scrapy using `pip install scrapy`
4. Install flask using `pip install flask`

### Linux
1. Install pip using `sudo apt-get install python-pip`
3. Install scrapy using `sudo pip install scrapy`
4. Install flask using `sudo pip install flask`


## Running Crawler
1. Go to root directory i.e. Product-Info-Crawler
2. Run `python run_crawler.py`
3. Enter the search keyword (a product or brand name) in command line.
4. See the crawling results in `results.csv` file

## Running Demo
1. Go to root directory i.e. Product-Info-Crawler
2. Run `python demo/run.py`
3. Open http://127.0.0.1:5000/ in browser window
4. Enter the search keyword and click search button
5. The products found are displayed with images, price and source info