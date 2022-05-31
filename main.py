from warnings import filterwarnings
import pandas as pd
from web_scraper import WebScraper
from sql_database import SQLDatabase
from mongo_db import MongoDB


class Task():
    
    def __init__(self):
        self.__dataset = None

    def scrape(self):
        scraper = WebScraper()
        self.__dataset = scraper.scrape()
    
    def excel(self):
        dataset = pd.DataFrame(self.__dataset)
        dataset.to_excel('Laptops.xlsx', index=False)
    
    def sql_database(self):
        sql = SQLDatabase()
        sql.create_database(self.__dataset)

    def mongo_db(self):
        no_sql = MongoDB()
        no_sql.create_database(self.__dataset)
    

if __name__ == '__main__':
    filterwarnings('ignore')
    task = Task()
    task.scrape()
    task.excel()
    task.sql_database()
    task.mongo_db()