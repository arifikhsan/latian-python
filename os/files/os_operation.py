import os
import datetime

os.remove('novel.txt')
os.rename('before.txt', 'after.txt')

os.path.exists('finished_masterpiece.txt')
os.path.getsize('spider.txt')
os.path.getmtime('spider.txt')

timestamp = os.path.getmtime('spider.txt')

datetime.datetime.fromtimestamp(timestamp)

os.path.abspath('spider.txt')
