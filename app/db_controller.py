from app.db_helper import DbHelper

db = DbHelper()
url_queue=[]
url_list=[]
def check_malware(url: str):
    """
    Functionality to check if the url is malware.
    :param url: str of url to be checked
    :return: Bool if url is malware
    """
    url_info = db.get_url(url)
    if url_info or url in url_list:
        return True
    else:
        return False


def add_malware(url_info):
    """
    Functionality to add malware urls to the db
    :param url: can be a list of str or a single str
    :return:
    """
    global url_queue
    if type(url_info)==list:
        for url in url_info:
            url_queue.append({'url':url_info})
            url_list.append(url)
        # success,id=db.insert_urls(urls_info_list=url_info)
    else:
        url_queue.append({'url': url_info})
        url_list.append(url_info)
        # success,id=db.insert_url(url_info={'url':url_info})
    if len(url_queue)>200:
        success,id=db.insert_urls(urls_info_list=url_queue)
        url_queue=[]
        return success,id
    else:
        return True, None
