import requests
from bs4 import BeautifulSoup
import re


class webpage:

    def get_nytimes_headlines(self):
        base_url = 'http://www.nytimes.com'
        page = requests.get(base_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        story = soup.find_all('article', {'class': 'css-8atqhb'})
        regex = re.compile('css-*')
        dict = {}
        Story_rank = 0
        for story in story:
            Story_rank += 1
            print("This is a story")
            headline = story.find('div', {'class': regex})
            test =  headline.text
            to_write = headline.text.encode('utf8')
            dict[Story_rank] = to_write
            with open("News.txt", 'a') as f:
                f.write("\n")
                f.write(to_write)
        f.close()


webpage_obj = webpage()
webpage_obj.get_nytimes_headlines()



