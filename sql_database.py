import sqlite3
from queries import features_laptops, create_table_query, insert_query


class SQLDatabase:
    
    def __init__(self):
        self.__dataset = None
        self.__connection = None
        self.__is_conn = False
        self.__cursor = None

    def __create_connection(self):
        try:
            self.__connection = sqlite3.connect('Laptops_Flipkart.sqlite')
            self.__cursor = self.__connection.cursor()
            self.__is_conn = True
        except:
            print("Unable to connect to database.")
    
    def __create_table(self):
        if self.__is_conn:
            self.__cursor.executescript(create_table_query)
            self.__connection.commit()

    def __insert(self):
        total = len(self.__dataset['BrandName'])
        for i in range(total):
            values = tuple([self.__dataset[feature][i] for feature in features_laptops])
            self.__cursor.execute(insert_query, values)
            self.__connection.commit()

    def __close_connection(self):
        if self.__is_conn:
            self.__cursor.close()
            self.__connection.close()

    def create_database(self, dataset):
        self.__dataset = dataset
        self.__create_connection()
        if self.__is_conn:
            self.__create_table()
            self.__insert()
            self.__close_connection()
        return 