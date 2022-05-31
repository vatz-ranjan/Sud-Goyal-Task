from numpy import record
from queries import features_laptops
from pymongo import MongoClient


class MongoDB:
    
    def __init__(self):
        self.__dataset = None
        self.__connection = None
        self.__database = None
        self.__collection = None
        self.__is_conn = False

    def __create_connection(self):
        try:
            self.__connection = MongoClient(host='localhost', port=27017)
            self.__database = self.__connection['Flipkart']
            self.__collection = self.__database['Laptops']
            self.__is_conn = True
        except:
            print("Unable to connect to MongoDB.")
            self.__is_conn = False

    def __insert_values(self):
        if self.__is_conn:
            total = len(self.__dataset['ModelName'])
            for i in range(total):
                record = {}
                for feature in features_laptops:
                    record[feature] = self.__dataset[feature][i]
                self.__collection.insert_one(record)

    def __close_connection(self):
        if self.__is_conn:
            self.__connection.close()

    def create_database(self, dataset):
        self.__dataset = dataset
        self.__create_connection()
        if self.__is_conn:
            self.__insert_values()
            self.__close_connection()
        return