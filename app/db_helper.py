import pymongo


class DbHelper:
    def __init__(self):  # , url, usr, password):
        self.client = pymongo.MongoClient(
            "mongodb+srv://admin:cVwJxEpNTkMqxbkT@cluster0.o0ofqfz.mongodb.net/?retryWrites=true&w=majority",
            timeoutMS=100000, socketTimeoutMS=100000)

    def get_client(self):
        """
        Function to return Pymongo client
        :return: returns success,pymongo client
        """
        if self.client:
            return True, self.client
        else:
            return False, None

    def get_db(self):
        """
        Function to get client cursor
        :return: success boolean, cursor
        """
        if self.client and self.check_db():
            print("DB not created")
            return True, self.client.malware
        else:
            return False, None

    def check_db(self):
        """
        Function to check if db exists
        :return: bool True if db exists
        """
        return 'malware' in self.client.list_database_names()

    def check_collection(self):
        """
        Internal function to check if collection and db exists
        :return: bool True if collection and db exists
        """
        return self.check_db() and 'urls' in self.client.malware.list_collection_names()

    def get_collection(self):
        """
        Function to access collection
        :return: bool,Cursor to Collection
        """
        if self.check_collection():
            return True, self.client.malware.urls
        else:
            print("Collection does not exist")
            return False, None

    def get_url(self, url):
        """
        Functionality to get url from db
        :param url: string of url
        :return: returns record if it exists
        """
        status, collection = self.get_collection()
        if status:
            return collection.find_one({"url": url})
        else:
            return None

    def update_url(self, url, url_info):
        pass

    def insert_url(self, url_info: dict):
        '''
        Functionality to insert a single url
        :param url_info:
        :return:
        '''
        status, collection = self.get_collection()
        if status:
            idx=collection.insert_one(url_info)
            return True, idx
        else:
            return False, None

    def insert_urls(self, urls_info_list: list):
        """
        Functionality to insert bulk urls
        :param urls_info_list: list of dictionaries
        :return:
        """
        status, collection = self.get_collection()
        if status:
            idx=collection.insert_many(urls_info_list)
            return True,idx
        else:
            return False,None


# client = pymongo.MongoClient(
#     "mongodb+srv://admin:cVwJxEpNTkMqxbkT@cluster0.o0ofqfz.mongodb.net/?retryWrites=true&w=majority")
# db = client.malware
# print(db)
# print(db.urls.find_one())
# return db.urls
# url_info = {'0': '24330000', '1': '2022-11-26 18:05:12', '2': 'http://222.138.204.19:39382/Mozi.m', '3': 'online',
#             '4': 'None', '5': 'malware_download', '6': 'elf,Mozi', '7': 'https://urlhaus.abuse.ch/url/2433019/',
#             '8': 'lrz_urlhaus'}
# DB = DbHelper()
# print(DB.get_client())
# print(DB.get_db())
# print(DB.get_collection())

# print(DB.insert_url(url_info=url_info))
# print(DB.get_url("http://222.138.204.19:39382/Mozi.m"))
