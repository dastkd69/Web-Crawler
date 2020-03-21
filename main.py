import threading
from queue import Queue
from Spider import Spider
from domain import *
from general import *

FOLDER_NAME = input('Enter Folder Name: ')
MAIN_PAGE = input('Enter URL: ')
DOMAIN_NAME = get_domain_name(MAIN_PAGE)
QUEUE_FILE = FOLDER_NAME + '/queue.txt'
CRAWLED_FILE = FOLDER_NAME + '/crawled.txt'
NUMBER_OF_THREADS = int(input('How many threads do you want to assign? : '))
Q = Queue()
Spider(FOLDER_NAME, MAIN_PAGE, DOMAIN_NAME)


# Create threads (kill when main exits, use daemon)
def create_threads():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=task)
        t.daemon = True
        t.start()


# Do the next task in the queue
def task():
    while True:
        url = Q.get()
        Spider.crawl_page(threading.current_thread().name, url)
        Q.task_done()


# Each queued link is a new task for the spiders
def create_tasks():
    for link in file_to_set(QUEUE_FILE):
        Q.put(link)
    Q.join()
    crawl()


# Check for items in queue and deploy multi-threaded crawler
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_tasks()


create_threads()
crawl()
