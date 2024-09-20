import requests, string, os
from bs4 import BeautifulSoup
no_of_pages = int(input('Enter a number of pages: '))
type_of_article = input("Enter the types of articles: ")
base_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={}'
def scraper(page_num):
    os.mkdir(f"Page_{page_num}")
    url = base_url.format(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        article_type = article.find('span', {'data-test': 'article.type'})
        if article_type.text.strip() == type_of_article:
            article_tag = article.find('a')
            article_title = article_tag.text.strip()
            article_title = article_title.replace(' ', '_').replace(string.punctuation, '')
            link = article_tag.get('href')
            response2 = requests.get('https://www.nature.com' + link)
            soup2 = BeautifulSoup(response2.content, 'html.parser')
            article_body = soup2.find('p', {"class": "article__teaser"}).get_text().strip()
            # change the directory to Page_{page_num}
            os.chdir(f'{os.getcwd()}/Page_{page_num}')
            file_name = os.path.join(os.getcwd(), article_title)
            with open(F'{file_name}.txt', 'w', encoding='UTF-8') as file:
                file.write(article_body)
            os.chdir('/home/ahmad/Web Scraper/Web Scraper/task')

for i in range(1, (no_of_pages + 1)):
    scraper(i)
