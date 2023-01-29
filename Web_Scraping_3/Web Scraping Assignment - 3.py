#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import selenium
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import requests
import re
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


# # Answer: 1-

# In[29]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[30]:


url = "https://www.amazon.in/"
driver.get(url)


# In[31]:


user_input = input('Enter the product that we want to search : ')


# In[32]:


# searching the web element for user input
search=driver.find_element(By.ID,"twotabsearchtextbox")
search

# sending the user input to search bar
search.send_keys(user_input)

# locating the search button using xpath
search_btn = driver.find_element(By.XPATH,"//div[@class='nav-search-submit nav-sprite']/span/input")

# clicking on search button
search_btn.click()


# # Answer: 2-

# In[33]:


#collecting all the Product URLS
urls = []
for i in range(0,3):
    Page_urls=driver.find_elements(By.XPATH,"//a[@class='a-link-normal s-no-outline']")
    for i in Page_urls:
        urls.append(i.get_attribute('href'))
        
    #next button 
    nxt_btn=driver.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']") 
    url=nxt_btn.get_attribute('href')
    driver.get(url)
    time.sleep(2)


# In[35]:


#Making empty lists and scraping the required spots
Product_name = []
Brand_name= []
Ratings = []
No_Ratings = []
Price = []
Return = []
Expected_Delivery = []
Availability = []
Other_Details = []

#Start with for loop
for i in urls:
    driver.get(i)
    time.sleep(2)
    
    
    #Scraping data for product name
    try:
        prod=driver.find_element(By.XPATH,"//span[@id='productTitle']")
        Product_name.append(prod.text)
    except NoSuchElementException as e:
        Product_name.append("-")
        
        
    #Scraping data for brand name
    try:
        brand=driver.find_element(By.XPATH,"//div[@id='bylineInfo_feature_div']/div/a")
        Brand_name.append(brand.text)
    except NoSuchElementException as e:
        Brand_name.append("-")
        
        
     #Scraping data for Ratings
    try:
        rat=driver.find_element(By.XPATH,"//span[@id='acrPopover']")
        Ratings.append(rat.get_attribute("title"))   
    except NoSuchElementException as e:
        Ratings.append("-")
        
        
    #Scraping data for No of Ratings
    try:
        no_rat=driver.find_element(By.XPATH,"//a[@id='acrCustomerReviewLink']/span")
        No_Ratings.append(no_rat.text)
    except NoSuchElementException as e:
        No_Ratings.append("-")
        
        
    #Scraping data for Price
    try:
        pri=driver.find_element(By.XPATH,"//span[@id='priceblock_ourprice']")
        Price.append(pri.text)
    except NoSuchElementException as e:
        Price.append("-")
        
        
    #Scraping data for Return/Exchange
    try:
        ret=driver.find_element(By.XPATH,"//div[@data-name='RETURNS_POLICY']/span/div[2]/a")
        Return.append(ret.text)
    except NoSuchElementException as e:
        Return.append("-")
        
     
    #Scraping data for Expected_Delivary
    try:
        delivary=driver.find_element(By.XPATH,"//div[@id='ddmDeliveryMessage']/b")
        Expected_Delivery.append(delivary.text)
    except NoSuchElementException as e:
        Expected_Delivery.append("-")
        
        
    #Scraping data for Availability
    try:
        avai=driver.find_element(By.XPATH,"//div[@id='availability']/span")
        Availability.append(avai.text)
    except NoSuchElementException as e:
        Availability.append("-")
        
        
    #Scraping data for Other_Details
    try:
        details=driver.find_element(By.XPATH,"//ul[@class='a-unordered-list a-vertical a-spacing-mini']")
        Other_Details.append(details.text)
    except NoSuchElementException as e:
        Other_Details.append("-")
        
        
#DATA FRAMEING
Guitar=pd.DataFrame({})
Guitar['Name'] = Product_name
Guitar['Brand'] = Brand_name
Guitar['Rating'] = Ratings
Guitar['No of Ratings'] = No_Ratings
Guitar['Price'] = Price
Guitar['Return'] = Return
Guitar['Expected_Delivery'] = Expected_Delivery
Guitar['Availability'] = Availability
Guitar['Other_Details'] = Other_Details
Guitar['Urls'] = urls


# In[36]:


Guitar


# In[37]:


#saving data to csv
Guitar.to_csv("Guitar.csv")


# In[42]:


driver.close()


# # Answer: 3-

# In[43]:


driver=webdriver.Chrome(r"C:/Users/anshu/Downloads/chromedriver_win32/chromedriver.exe")


# In[51]:


# getting images.google.com
url = "https://images.google.com/"
#Creating empty list and giving search items as list and creating loop
urls = []    
data = []
search_item = ["fruits", "cars", "Machine Learning"]
for item in search_item:
    driver.get(url)  
    time.sleep(5)
    search_bar = driver.find_element(By.TAG_NAME,"input") #Xpath for search bar
    
    search_bar.send_keys(str(item))      #sending key word for search item
    
    search_button =driver.find_element(By.XPATH,"//button[@class='Tg7LZd']").click() #Clicking on search button
    
    # scrolling the web page to get more images
    for _ in range(500):
        driver.execute_script("window.scrollBy(0,100)")
        
        imgs = driver.find_elements(By.XPATH,"//img[@class='rg_i Q4LuWd']")
    img_url = []
    for image in imgs:
        source = image.get_attribute('src')
        if source is not None:
                if(source[0:4] == 'http'):
                    img_url.append(source)
    for i in img_url[:100]:
        urls.append(i)
                    
for i in range(len(urls)):
    if i >= 300:
        break
    print("Downloading {0} of {1} images" .format(i, 300))
    response = requests.get(urls[i])

    file = open(r"F:\fliprobo\GoogleImages"+str(i)+".jpg", "wb")

    file.write(response.content)


# In[52]:


driver.close()


# # Answer: 4-

# In[53]:


# connecting to the webdriver
driver=webdriver.Chrome(r"C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")


# In[54]:


# getting the webpage of mentioned url
url = "https://www.flipkart.com/"
driver.get(url)


# In[55]:


# closing login popup button
lonin_x_btn = driver.find_element(By.XPATH,"//div[@class='_2QfC02']//button").click()


# In[57]:


# search for web element
search_bar = driver.find_element(By.XPATH,"//input[@class='_3704LK']")

# sending keys to search product
search_bar.send_keys("pixel")


# In[59]:


# location the search button using xpath
search_btn = driver.find_element(By.XPATH,"//button[@class='L0Z3Pu']")

# clicking on search button
search_btn.click()


# In[60]:


# fetching 1st page of URLs of smartphone
page1_url = []
urls = driver.find_elements(By.XPATH,"//a[@class='_1fQZEK']")
for url in urls:
    page1_url.append(url.get_attribute('href'))


# In[61]:


len(page1_url)


# In[62]:


# creating empty list
Smartphones = ({})
Smartphones['Brand'] = []
Smartphones['Phone name'] = []
Smartphones['Colour'] = []
Smartphones['RAM'] = []
Smartphones['Storage(ROM)'] = []
Smartphones['Primary Camera'] = []
Smartphones['Secondary Camera'] = []
Smartphones['Display Size'] = []
Smartphones['Display Resolution'] = []
Smartphones['Processor'] = []
Smartphones['Processor Cores'] = []
Smartphones['Battery Capacity'] = []
Smartphones['Price'] = []
Smartphones['URL'] = []


# In[68]:


# Scraping data from each url of page 1
for url in page1_url:
    driver.get(url)                                                        
    print("Scraping URL = ", url)
    Smartphones['URL'].append(url)                                                          
    time.sleep(2)
    
    
    #Clicking on read more button
    try:
        read_more = driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')     
        read_more.click()
    except NoSuchElementException:
        print("Exception occured while moving to next page")
    
    
    #Scraping brand name of phone data
    try:
        brand_tags = driver.find_element(By.XPATH,'//span[@class="B_NuCI"]')      
        Smartphones["Brand"].append(brand_tags.text.split()[0])
    except NoSuchElementException:
        Smartphones['Brand'].append('-')
    
    
    #Scraping phone name data
    try:
        name_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][1]/table/tbody/tr[3]/td[2]/ul/li')     
        Smartphones['Phone name'].append(name_tags.text)
    except NoSuchElementException:
        Smartphones['Phone name'].append('-')
    
    
    #Scraping phone color data
    try:
        color_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][1]/table/tbody/tr[4]/td[2]/ul/li')      
        Smartphones['Colour'].append(color_tags.text)
    except NoSuchElementException:
        Smartphones['Colour'].append('-')
     
    
    #Scraping RAM data
    try:
        ram_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][4]/table[1]/tbody/tr[2]/td[2]/ul/li')                
        Smartphones['RAM'].append(ram_tags.text)
    except NoSuchElementException:
        Smartphones['RAM'].append('-')
    
    
    #Scraping ROM data
    try:
        rom_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][4]/table[1]/tbody/tr[1]/td[2]/ul/li')        
        Smartphones['Storage(ROM)'].append(rom_tags.text)
    except NoSuchElementException:
        Smartphones['Storage(ROM)'].append('-')
        
        
    #Scraping Primary camera data
    try:                                                                                    
        pri_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table[1]/tbody/tr[2]/td[2]/ul/li')
        Smartphones['Primary Camera'].append(pri_tags.text)
    except NoSuchElementException:
        Smartphones['Primary Camera'].append('-')
        
        
    #Scraping secondary camera data
    try:                                                                                    
        sec_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table[1]/tbody/tr[6]/td[1]')
        if sec_tags != "Secondary Camera" : 
            if driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table[1]/tbody/tr[5]/td[1]').text == "Secondary Camera":
                sec_cam = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table[1]/tbody/tr[5]/td[2]/ul/li')
            else :
                raise NoSuchElementException
        else :
            sec_cam = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table[1]/tbody/tr[6]/td[2]/ul/li')
        Smartphones['Secondary Camera'].append(sec_cam.text)
    except NoSuchElementException:
        Smartphones['Secondary Camera'].append('-')
        
        
    #Scraping Display size data 
    try:
        disp_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][2]/div')
        if disp_tags.text != "Display Features" : raise NoSuchElementException
        disp_size = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][2]/table[1]/tbody/tr[1]/td[2]/ul/li')  
        Smartphones['Display Size'].append(disp_size.text)
    except NoSuchElementException:
        Smartphones['Display Size'].append('-')
    
    
    #Scraping display resolution data
    try:
        dires_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][2]/div')
        if dires_tags.text != "Display Features" : raise NoSuchElementException
        disp_reso = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][2]/table[1]/tbody/tr[2]/td[2]/ul/li')    
        Smartphones['Display Resolution'].append(disp_reso.text)
    except NoSuchElementException:
        Smartphones['Display Resolution'].append('-')
    
    
    
    #Scraping Processor data
    try:
        pro_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table[1]/tbody/tr[2]/td[1]')
        if pro_tags.text != "Processor Type" : raise NoSuchElementException
        processor = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table[1]/tbody/tr[2]/td[2]/ul/li')   
        Smartphones['Processor'].append(processor.text)
    except NoSuchElementException:
        Smartphones['Processor'].append('-')
        
    
    
    #Scraping Processor core data    
    try:                                                                                     
        core_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table[1]/tbody/tr[3]/td[1]')
        if core_tags.text != "Processor Core" :
            core_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table[1]/tbody/tr[2]/td[1]')
            if core_tags.text != "Processor Core" : 
                raise NoSuchElementException
            else :
                cores = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table[1]/tbody/tr[2]/td[2]/ul/li')
        else :
            cores = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table[1]/tbody/tr[3]/td[2]/ul/li')
        Smartphones['Processor Cores'].append(cores.text)
    except NoSuchElementException:
        Smartphones['Processor Cores'].append('-')
    
    
    
    #Scraping battery capacity data
    try:
        if driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][10]/div').text != "Battery & Power Features" :
            if driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][9]/div').text == "Battery & Power Features" :
                bat_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][9]/table/tbody/tr/td[1]')
                if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
                bat_capa = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][9]/table/tbody/tr/td[2]/ul/li')                
            elif driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][8]/div').text == "Battery & Power Features" :
                bat_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][8]/table/tbody/tr/td[1]')
                if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
                bat_capa = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][8]/table/tbody/tr/td[2]/ul/li')
            else:
                raise NoSuchElementException
        else :
            bat_tags = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][10]/table/tbody/tr/td[1]')
            if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
            bat_capa = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][10]/table/tbody/tr/td[2]/ul/li')              
        Smartphones['Battery Capacity'].append(bat_capa.text)
    except NoSuchElementException:
        Smartphones['Battery Capacity'].append('-')
        
        
        
    #Scraping Price data
    try:
        price_tags = driver.find_element(By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]')      
        Smartphones['Price'].append(price_tags.text)
    except NoSuchElementException:
        Smartphones['Price'].append('-')


# In[71]:


print(len(Smartphones["Brand"]), len(Smartphones["Phone name"]), len(Smartphones["Colour"]), len(Smartphones["RAM"]), len(Smartphones["Storage(ROM)"]), len(Smartphones["Primary Camera"]), len(Smartphones["Secondary Camera"]), len(Smartphones["Display Size"]), len(Smartphones["Display Resolution"]), len(Smartphones["Processor"]), len(Smartphones["Processor Cores"]), len(Smartphones["Battery Capacity"]), len(Smartphones["Price"]), len(Smartphones["URL"])


# In[72]:


df = pd.DataFrame.from_dict(Smartphones)
df


# In[73]:


driver.close()


# # Answer: 5-

# In[74]:


# connecting to the webdriver
driver=webdriver.Chrome(r"C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")


# In[75]:


# getting mentioned url and opening google maps web page
url = 'https://www.google.co.in/maps'
driver.get(url)
time.sleep(2)


# In[77]:


# entering the city name in search bar
City = input('Enter City name that has to be searched : ')
search_bar = driver.find_element(By.ID,'searchboxinput')
search_bar.click()
time.sleep(2)

#sending keys to find cities
search_bar.send_keys(City)

#checking for webelement and clicking on search button
search_btn = driver.find_element(By.ID,"searchbox-searchbutton")
search_btn.click()
time.sleep(2)

try:
    url_str = driver.current_url
    print("URL Extracted: ", url_str)
    latitude_longitude = re.findall(r'@(.*)data',url_str)
    if len(latitude_longitude):
        lat_lng_list = latitude_longitude[0].split(",")
        if len(lat_lng_list)>=2:
            latitude = lat_lng_list[0]
            longitude = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(latitude, longitude))
except Exception as e:
        print("Error: ", str(e))


# In[78]:


driver.close()


# # Answer: 6-

# In[79]:


# connecting to the webdriver
driver=webdriver.Chrome(r"C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")


# In[92]:


url = "https://trak.in/india-startup-funding-investment-2015/"
driver.get(url)
time.sleep(2)


# Its not showing any results on the url that is given in question in funding section, therefore i searched on net and found this url that is showing result

# In[95]:


#Getting xpath for funding deals
fund_button = driver.find_element(By.XPATH,'//li[@id="menu-item-51510"]/a').get_attribute('href')
driver.get(fund_button)


# In[96]:


#Empty Lists
fund_deals = {}
fund_deals['Date'] = []
fund_deals['Startup Name'] = []
fund_deals['Industry/Vertical'] = []
fund_deals['Sub_Vertical'] = []
fund_deals['Location'] = []
fund_deals['Investor'] = []
fund_deals['Investment Type'] = []
fund_deals['Amount(in USD)'] = []


for i in range(48,51):
    
    # scraping data of data
    date = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[2]".format(i))
    for d in date:
        fund_deals['Date'].append(d.text)
        
    # scraping data of startup name
    startup_name = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[3]".format(i))
    for name in startup_name:
        fund_deals['Startup Name'].append(name.text)
        
    
    #scraping data of industry or vertical
    industry = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[4]".format(i))
    for ind in industry:
        fund_deals['Industry/Vertical'].append(ind.text)
        
    
    #scraping data of sub-vertical
    sub_vertical = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[5]".format(i))
    for sv in sub_vertical:
        fund_deals['Sub_Vertical'].append(sv.text)
        
        
    # scraping data of location
    location = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[6]".format(i))
    for loc in location:
        fund_deals['Location'].append(loc.text)
        
        
    # scraping data of investor
    investor = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[7]".format(i))
    for invest in investor:
        fund_deals['Investor'].append(invest.text)
        
        
    # scraping data of investment type
    investment_type = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[8]".format(i))
    for invtype in investment_type:
        fund_deals['Investment Type'].append(invtype.text)
        
        
    # scraping data of amount
    amount = driver.find_elements(By.XPATH,"//table[@id='tablepress-{}']/tbody/tr/td[9]".format(i))
    for amt in amount:
        fund_deals['Amount(in USD)'].append(amt.text)


# In[97]:


# checking lengths of all scraped data
print(len(fund_deals['Date']),
len(fund_deals['Startup Name']),
len(fund_deals['Industry/Vertical']),
len(fund_deals['Sub_Vertical']),
len(fund_deals['Location']),
len(fund_deals['Investor']),
len(fund_deals['Investment Type']),
len(fund_deals['Amount(in USD)'] 
))


# In[98]:


# creating DataFrame for scraped data
fund_data = pd.DataFrame(fund_deals)
fund_data


# In[99]:


# saving data in csv file
fund_data.to_csv("trak_in.csv")


# In[100]:


driver.close()


# # Answer: 7-

# In[101]:


driver=webdriver.Chrome(r"C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")


# In[102]:


#Opening the specified url
url = "https://www.digit.in/"
driver.get(url)
time.sleep(3)


# In[103]:


#searching for best laptop
best_gam_lap = driver.find_element(By.XPATH,"//div[@class='listing_container']//ul//li[9]").click()
time.sleep(4)


# In[109]:


# creating empty list
Laptop_Name = []
Operating_sys = []
Display = []
Processor = []
Memory = []
Weight = []


# In[113]:


#scraping the data of laptop names
laptop_name = driver.find_elements(By.XPATH,"//div[@class='right-container']/div/a/h3")
for name in laptop_name:
    Laptop_Name.append(name.text)
    
#scraping the data of display
try:
    op_sys = driver.find_elements(By.XPATH,"//div[@class='product-detail']/div/ul/li[2]/div/div")
    for disp in display:
        Display.append(disp.text)
except NoSuchElementException:
    pass


#scraping data of os of the Laptop
try:
    display = driver.find_elements(By.XPATH,"//div[@class='product-detail']/div/ul/li[1]/div/div")
    for os in op_sys:
        Operating_sys.append(os.text)
except NoSuchElementException:
    pass


# scraping data of memory
try:
    processor = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[6]/td[3]")
    for memo in memory:
        Memory.append(memo.text)
except NoSuchElementException:
    pass


# scraping the data of processor
try:
    memory = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[5]/td[3]")
    for pro in processor:
        Processor.append(pro.text)
except NoSuchElementException:
    pass


# scraping data of weight
try:
    weight = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[7]/td[3]")
    for wgt in weight:
        Weight.append(wgt.text)
except NoSuchElementException:
    pass


# In[118]:


print(len(Laptop_Name),
len(Display),
len(Operating_sys),
len(Memory),
len(Processor),
len(Weight))


# In[119]:


#Printing data frame
Gaming_Laptop


# In[120]:


# saving the data to csv
Gaming_Laptop.to_csv("Gaming_Laptops.csv")


# In[121]:


driver.close()


# # Answer: 8-

# In[133]:


# connecting to the webdriver
driver=webdriver.Chrome(r"C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")


# In[134]:


# getting the specified url
url = "https://www.forbes.com/?sh=220c77632254"
driver.get(url)


# In[136]:


opt_btn = driver.find_element(By.XPATH,"//div[@class='_8FT-x3t4']//button")
opt_btn.click()
time.sleep(3)


# # Answer: 9- 

# In[166]:


# connecting to the webdriver
driver=webdriver.Chrome(r"C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")


# In[167]:


# opening the youtube.com
url = "https://www.youtube.com/"
driver.get(url)
time.sleep(2)


# In[168]:


# finding element for search bar
search_bar = driver.find_element(By.XPATH,"//div[@class='ytd-searchbox-spt']/input")
search_bar.send_keys("GOAT")      # entering video name
time.sleep(2)


# In[169]:


#clicking on search button
search_btn = driver.find_element(By.ID,"search-icon-legacy")
search_btn.click()
time.sleep(2)


# In[170]:


# clicking on first video
video = driver.find_element(By.XPATH,"//yt-formatted-string[@class='style-scope ytd-video-renderer']")
video.click()


# In[171]:


# 1000 times we scroll down in order to generate more comments
for _ in range(500):
    driver.execute_script("window.scrollBy(0,1000)")


# In[172]:


# creating empty lists
comments = []
comment_time = []
Time = []
Likes = []
No_of_Likes = []

# scrape comments
cm = driver.find_elements(By.ID,"content-text")
for i in cm:
    if i.text is None:
        comments.append("--")
    else:
        comments.append(i.text)
time.sleep(4)


# scrape time when comment was posted
tm = driver.find_elements(By.XPATH,"//a[contains(text(),'ago')]")
for i in tm:
    Time.append(i.text)
    
for i in range(0,len(Time),2):
    comment_time.append(Time[i])
time.sleep(4)


# scrape the comment likes
like = driver.find_elements(By.XPATH,"//span[@class='style-scope ytd-comment-action-buttons-renderer']")
for i in like:
    Likes.append(i.text)
    
for i in range(1,len(Likes),2):
    No_of_Likes.append(Likes[i])


# In[173]:


print(len(comments),len(comment_time),len(No_of_Likes))


# In[174]:


# creating dataframe for scraped data

Youtube = pd.DataFrame({})
Youtube['Comment'] = comments[:500]
Youtube['Comment Time'] = comment_time[:500]
Youtube['Comment Upvotes'] = No_of_Likes[:500]
Youtube


# # Answer: 10-

# In[175]:


# connecting to the webdriver
driver=webdriver.Chrome(r"C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")


# In[176]:


# getting the web page of mentioned url
url = "https://www.hostelworld.com/"
driver.get(url)
time.sleep(3)


# In[181]:


# locating the location search bar
search_bar = driver.find_element(By.ID,"search-input-field")

# entering London in search bar
search_bar.send_keys("London")


# In[182]:


# select London
London = driver.find_element(By.XPATH,"//ul[@id='predicted-search-results']//li[2]")
#clicking on button
London.click()

# do click on Let's Go button
search_btn = driver.find_element(By.ID,'search-button')
search_btn.click()


# In[183]:


# creating empty list & find required data
hostel_name = []
distance = []
pvt_prices = []
dorms_price = []
rating = []
reviews = []
over_all = []
facilities = []
description = []
url = []


# In[187]:


# scraping the required informations
for i in driver.find_elements(By.XPATH,"//div[@class='pagination-item pagination-current' or @class='pagination-item']"):
    i.click()
    time.sleep(3)
    
    
    # scraping  hostel name
    try:
        name = driver.find_elements(By.XPATH,"//h2[@class='title title-6']")
        for i in name:
            hostel_name.append(i.text)
    except NoSuchElementException:
        hostel_name.append('-')
        
        
    # scraping distance from city centre
    try:
        dist = driver.find_elements(By.XPATH,"//div[@class='subtitle body-3']//a//span[1]")
        for i in name:
            distance.append(i.text.replace('Hostel - ',''))
    except NoSuchElementException:
        distance.append('-')
        
   
    for i in driver.find_elements(By.XPATH,"//div[@class='prices-col']"):   
    # scraping privates from price
        try:
            pvt_price = driver.find_element(By.XPATH,"//a[@class='prices']//div[1]//div")
            pvt_prices.append(pvt_price.text)
        except NoSuchElementException:
            pvt_prices.append('-')
   

    for i in driver.find_elements(By.XPATH,"//div[@class='prices-col']"):          
    # scraping dorms from price
        try:
            dorms = driver.find_element(By.XPATH,"//a[@class='prices']//div[2]/div")
            dorms_price.append(dorms.text)
        except NoSuchElementException:
            dorms_price.append('-')
            
            
    # scraping facilities
    try:
        fac1 = driver.find_elements(By.XPATH,"//div[@class='has-wifi']")
        fac2 = driver.find_elements(By.XPATH,"//div[@class='has-sanitation']")
        for i in fac1:
            for j in fac2:
                facilities.append(i.text +', '+ j.text)
    except NoSuchElementException:
        facilities.append('-')
     
            
    #fetching url of each hostel
    p_url = driver.find_elements(By.XPATH,"//div[@class='prices-col']//a[2]")
    for i in p_url:
        url.append(i.get_attribute("href"))
        
for i in url:
    driver.get(i)
    time.sleep(3)
    

    # scraping ratings
    try:
        rat = driver.find_element(By.XPATH,"//div[@class='score orange big' or @class='score gray big']")
        rating.append(rat.text)
    except NoSuchElementException:
        rating.append('-')
        
        
    # scraping total review
    try:
        rws = driver.find_element(By.XPATH,"//div[@class='reviews']")
        reviews.append(rws.text.replace('Total Reviews',''))
    except NoSuchElementException:
        reviews.append('-')
        
        
    # fetching over all review
    try:
        overall = driver.find_element(By.XPATH,"//div[@class='keyword']//span")
        over_all.append(overall.text)
    except NoSuchElementException:
        over_all.append('-')
        
        
    # fetching property description
    try:
        disc = driver.find_element(By.XPATH,"//div[@class='content']")
        description.append(disc.text)
    except NoSuchElementException:
        over_all.append('-')
    
    # do click on show more button for description
    try:
        driver.find_element(By.XPATH,"//a[@class='button primary small full-width']").click()
        time.sleep(4)
    except NoSuchElementException:
        pass


# In[188]:


print(len(hostel_name),
len(distance),
len(pvt_prices),
len(dorms_price),
len(rating),
len(reviews),
len(over_all),
len(facilities),
len(description),
len(url))


# In[189]:


# creating DataFrame
Hostel = pd.DataFrame({})
Hostel['Hostel Name'] = hostel_name
Hostel['Distance from City Centre'] = distance
Hostel['Ratings'] = rating
Hostel['Total Reviews'] = reviews
Hostel['Overall Reviews'] = over_all
Hostel['Privates from Price'] = pvt_prices
Hostel['Dorms from Price'] = dorms_price
Hostel['Facilities'] = facilities[:74]
Hostel['Description'] = description
Hostel


# In[ ]:




