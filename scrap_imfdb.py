import requests
import shutil

website = 'https://www.imfdb.org/wiki/1968_Tunnel_Rats'
website_imgs = 'https://www.imfdb.org/' 
r = requests.get(website)
# print(r.text)

web_html = r.text


# for tag in website:
#     print(tag)

all_links = []
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        
        if tag == 'img':
            # print("Encountered a start tag:", tag)
            # print(attrs)
            for atr in attrs:
                if atr[0] == 'src':
                    # print(atr[1])  
                    all_links.append(website_imgs+atr[1])      
    # def handle_endtag(self, tag):
    #     if tag == 'img':
    #         print("Encountered an end tag :", tag)

    # def handle_data(self, data):
    #     print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed(web_html)

print(all_links)

for image_url in all_links:

    # image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    filename = image_url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

# import urllib.request
# # open a connection to a URL using urllib
# webUrl  = urllib.request.urlopen(website)
# #get the result code and print it
# print ("result code: " + str(webUrl.getcode()))

# # read the data from the URL and print it
# data = webUrl.read()
# # print(data)    
# for d in data:
#     print(d)

# import requests
# from bs4 import BeautifulSoup


# html_text = requests.get(website).text
# soup = BeautifulSoup(html_text, 'html.parser')


# for link in soup.find_all():
#     print(link.get('src'))
