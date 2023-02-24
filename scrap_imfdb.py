import requests
import shutil, os
from tqdm import tqdm

website = 'https://www.imfdb.org/wiki/1968_Tunnel_Rats'
website_imgs = 'https://www.imfdb.org'

folder_to_save = "images/"+website.split("/")[-1]
 
r = requests.get(website)

web_html = r.text

all_links = []
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for atr in attrs:
                if atr[0] == 'src':
                    image_link = atr[1].replace("thumb/","")
                    image_link = image_link.split("/")
                    image_link = "/".join(image_link[:-1])
                    # print(image_link)
                    all_links.append(website_imgs+image_link)      


parser = MyHTMLParser()
parser.feed(web_html)

if len(all_links):
    if not os.path.exists(folder_to_save):
        os.mkdir(folder_to_save)
# print(all_links)

for image_url in tqdm(all_links):
    filename = image_url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(folder_to_save+"/"+filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        # print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
        print(image_url)

