import webbrowser
from random import choice
random_page_generator = ['https://www.youtube.com/', 'https://www.amazon.com/',
                         'https://www.w3schools.com/', 'https://stackoverflow.com/',
                         'https://www.facebook.com/', 'https://twitter.com/',
                         'https://wuzzuf.net/', 'https://www.linkedin.com/']
webbrowser.open(choice(random_page_generator))