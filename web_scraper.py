from bs4 import BeautifulSoup
import requests


class WebScraper():

    def __init__(self):
        self.__url = None
        self.__brandName = []
        self.__modelName = []
        self.__processor = []
        self.__ram = []
        self.__operating_system = []
        self.__memory = []
        self.__display = []
        self.__originalPrice = []
        self.__discount = []
        self.__offerPrice = []
        self.__dataset = None

    def __scrape_website(self):
        page_no = 0
        while True:
            # if page_no > 10: break
            page_no += 1
            cur_page = f'search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_no}'
            cur_url = self.__url + cur_page
            print(f'Scanning {cur_url}')
            req = requests.get(cur_url)
            if req.status_code == 200:
                soup = BeautifulSoup(req.content, features='lxml')
                entries = soup.findAll('div', attrs={'class': '_3pLy-c row'})

                if len(entries) > 0:
                    for entry in entries:

                        model_name = entry.find('div', attrs={'class': '_4rR01T'}).text.upper()
                        brand_name = model_name.split(" ")[0]

                        features = entry.find('ul', attrs={'class': '_1xgFaf'})
                        features_list = [feature.text for feature in features]

                        while 'processor' not in features_list[0].lower():
                            features_list.pop(0)

                        processor = features_list[0]

                        while 'ram' not in features_list[1].lower():
                            features_list.pop(1)
                           
                        ram = features_list[1]                           
                        operating_system = features_list[2]   
                        memory = features_list[3] 
                        display = features_list[4]   

                        try:
                            offer_price = int(entry.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text[1:].replace(',', ''))
                        except:
                            offer_price = "?"

                        try:
                            discount = int(entry.find('div', attrs={'class': '_3Ay6Sb'}).string[:-5])
                        except:
                            discount = 0

                        if discount == 0:
                            original_price = offer_price
                        else:
                            try:
                                original_price = int(entry.find('div', attrs={'class': '_3I9_wc _27UcVY'}).text.strip()[1:].replace(',', ''))
                            except:
                                original_price = "?"

                        
                        self.__brandName.append(brand_name)
                        self.__modelName.append(model_name)
                        self.__processor.append(processor)
                        self.__ram.append(ram)
                        self.__operating_system.append(operating_system)
                        self.__memory.append(memory)
                        self.__display.append(display)
                        self.__originalPrice.append(original_price)
                        self.__discount.append(discount)
                        self.__offerPrice.append(offer_price)
                
                else:
                    break

    
    def scrape(self):
        self.__url = 'https://www.flipkart.com/'
        self.__scrape_website()
        self.__dataset = {
            'BrandName': self.__brandName,
            'ModelName': self.__modelName,
            'Processor': self.__processor,
            'RAM': self.__ram,
            'OperatingSystem': self.__operating_system,
            'Memory': self.__memory,
            'Display': self.__display,
            'OriginalPrice': self.__originalPrice,
            'Discount': self.__discount,
            'OfferPrice': self.__offerPrice
        }
        return self.__dataset

