import unittest

from app.db_controller import *
from app.db_helper import *


class Testdb_helper(unittest.TestCase):
    def setUp(self):
        self.DB = DbHelper()

    def test_get_client(self):
        success, client = self.DB.get_client()
        assert success == True

    def test_get_db(self):
        success, db = self.DB.get_db()
        assert success == True

    def test_check_db(self):
        success = self.DB.check_db()
        assert success == True

    def test_check_collection(self):
        success = self.DB.check_collection()
        assert success == True

    def test_get_collection(self):
        success, cursor = self.DB.get_collection()
        assert success == True

    def test_get_url(self):
        url_info = self.DB.get_url("http://222.138.204.19:39382/Mozi.m")
        assert url_info != None

    def test_insert_url(self):
        url_info = { 'url': 'http://222.138.204.19:39382/Mozi.m'}

        success, idx = self.DB.insert_url(url_info)
        assert success == True

    def test_insert_urls(self):
        url_info = [
            {'url': 'http://222.138.204.19:39382/Mozi.m'}]
        success, idx = self.DB.insert_urls(url_info)
        assert success == True


class Testdb_controller(unittest.TestCase):

    def test_malware(self):
        success = check_malware("http://222.138.204.19:39382/Mozi.m")
        assert success == True

    def test_malware_negetive(self):
        success = check_malware("")
        assert success == False

    def test_add_malware_dict(self):
        url_info = [
            {'0': '24330000', '1': '2022-11-26 18:05:12', '2': 'http://222.138.204.19:39382/Mozi.m', '3': 'online',
             '4': 'None', '5': 'malware_download', '6': 'elf,Mozi', '7': 'https://urlhaus.abuse.ch/url/2433019/',
             '8': 'lrz_urlhaus'}]
        success, id = add_malware(url_info)
        assert success == True

    def test_add_malware_list(self):
        url_info = {'0': '24330000', '1': '2022-11-26 18:05:12', '2': 'http://222.138.204.19:39382/Mozi.m',
                    '3': 'online',
                    '4': 'None', '5': 'malware_download', '6': 'elf,Mozi', '7': 'https://urlhaus.abuse.ch/url/2433019/',
                    '8': 'lrz_urlhaus'}
        success, id = add_malware(url_info)
        assert success == True
