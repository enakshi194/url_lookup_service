from app.db_helper import DbHelper

db = DbHelper()


def check_malware(url: str):
    """
    Functionality to check if the url is malware.
    :param url: str of url to be checked
    :return: Bool if url is malware
    """
    url_info = db.get_url(url)
    if url_info:
        return True
    else:
        return False


def add_malware(url_info):
    """
    Functionality to add malware urls to the db
    :param url: can be a list of str or a single str
    :return:
    """
    if type(url_info)==list:
        success,id=db.insert_urls(urls_info_list=url_info)
    else:
        success,id=db.insert_url(url_info={'url':url_info})
    return success,id
