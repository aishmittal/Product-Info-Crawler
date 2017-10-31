# Product-Info-Crawler
We developed a program named Product-Info-Crawler. Which is a python web crawler developed using scrapy framework. It has four spiders for crawling the search results from olx.in, amazon.in, ebay.in and shopclues.com. The crawler extract the product names, price, image urls, product urls and source and stores them in a csv file named `results.csv`. It can be useful for comparing the price of a particular product between different e-commerce websites.

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
1. Open command line
2. Go to root directory i.e. Product-Info-Crawler
3. Run `python run_crawler.py`
4. Enter the search keyword (a product or brand name) in command line.
5. See the crawling results in `results.csv` file

## Running Demo
1. Open Terminal
2. Go to demo directory i.e. Product-Info-Crawler/demo
3. Run `python run.py`
4. Open http://127.0.0.1:5000/ in browser window
5. Enter the search keyword and click search button
6. The products found are displayed with images, price and source info