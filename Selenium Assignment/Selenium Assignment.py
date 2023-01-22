#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# # Answer: 1-

# In[3]:


## Let's connect to the driver
driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[4]:


## Opening the question link on automated chrome browser
driver.get=("https://www.naukri.com/")


# In[7]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[8]:


## absolute xpath=copy full xpath
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[9]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[10]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[11]:


## Relative XPATH= //tag_name[@class="class_name"] in search
## Scrap title from driver page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
## Scrap location from driver page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
## Scrap company name from driver page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
## Scrap experience req. from driver page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)    


# In[12]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[13]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# # Answer: 2- 

# In[14]:


## Let's connect to the driver
driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[15]:


## Opening the question link on automated chrome browser
driver.get=("https://www.naukri.com/")


# In[16]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[17]:


## absolute xpath=copy full xpath
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[18]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[19]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[20]:


## Relative XPATH= //tag_name[@class="class_name"] in search
## Scrap title from driver page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
## Scrap location from driver page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
## Scrap company name from driver page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
## Scrap experience req. from driver page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)    


# In[21]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[22]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# # Answer: 3-

# In[23]:


## Let's connect to the driver
driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[24]:


## Opening the question link on automated chrome browser
driver.get=("https://www.naukri.com/")


# In[25]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[26]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[27]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[28]:


## Relative XPATH= //tag_name[@class="class_name"] in search
## Scrap title from driver page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
## Scrap location from driver page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
## Scrap company name from driver page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
## Scrap experience req. from driver page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)    


# In[29]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[30]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# # Answer: 4-

# In[31]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[32]:


driver.get=("https://www.flipkart.com/")


# In[33]:


designation=driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys('sunglasses')


# In[34]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.submit()


# In[36]:


product_brand=[]
product_description=[]
offer_price=[]
original_price=[]
percent_off=[]


# In[37]:


## Scrap brand from driver page
brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    brand=i.text
    product_brand.append(brand)
    
## Scrap description from driver page
description_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in description_tags:
    description=i.text
    product_description.append(description)
    
## Scrap price name from driver page
off_price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in off_price_tags:
    off_price=i.text
    offer_price.append(off_price)
    
original_price_tags=driver.find_elements(By.XPATH,'//div[@class="_3I9_wc"]')
for i in original_price_tags:
    org_price=i.text
    original_price.append(org_price)
    
percent_off_tags=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
for i in percent_off_tags:
    perc_off=i.text
    percent_off.append(perc_off)    


# In[38]:


print(len(product_brand),len(product_description),len(offer_price),len(original_price),len(percent_off))


# In[56]:


product_brand


# In[57]:


product_description


# In[58]:


offer_price


# In[60]:


original_price


# In[61]:


percent_off


# # Answer: 5-

# In[40]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[42]:


driver.get=("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market")


# In[43]:


product_rating=[]
summary=[]
full_review=[]


# In[44]:


rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in rating_tags:
    rating=i.text
    product_rating.append(rating)
    
summary_tags=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in summary_tags:
    summ=i.text
    summary.append(summ)
    
review_tags=driver.find_elements(By.XPATH,'//div[@class=""]')
for i in review_tags:
    review=i.text
    full_review.append(review)    


# In[45]:


print(len(product_rating),len(summary),len(full_review))


# In[46]:


df=pd.DataFrame({'Rating':product_rating,'Summary':summary,'Full_review':full_review})
df


# In[50]:


product_rating=[]
summary=[]
full_review=[]


# In[51]:


start=0 
end=10 
for page in range(start,end):
    rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating:
        product_rating.append(i.text)
    
    summ=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in summ:
        summary.append(i.text)
    
    review=driver.find_elements(By.XPATH,'//div[@class=""]')
    for i in review:
        full_review.append(i.text)
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[52]:


print(len(product_rating),len(summary),len(full_review))


# In[53]:


product_rating


# In[54]:


summary


# In[55]:


full_review


# # Answer: 6-

# In[68]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[69]:


driver.get=("https://www.flipkart.com/")


# In[70]:


designation=driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys('sneakers')


# In[71]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.submit()


# In[72]:


product_brand=[]
product_description=[]
product_price=[]


# In[74]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    brand=i.text
    product_brand.append(brand)
    
description_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in description_tags:
    description=i.text
    product_description.append(description)
    
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags:
    price=i.text
    product_price.append(price)


# In[75]:


print(len(product_brand),len(product_description),len(product_price))


# In[76]:


product_brand


# In[77]:


product_description


# In[78]:


product_price


# In[79]:


prod_brand=[]
description=[]
prod_price=[]


# In[86]:


start=0 
end=3
for page in range(start,end):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand:
        prod_brand.append(i.text)
    
    desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in desc:
        description.append(i.text)
    
    price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price:
        prod_price.append(i.text)
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[85]:


print(len(prod_brand),len(description),len(prod_price))


# In[87]:


prod_brand


# In[88]:


description


# In[89]:


prod_price


# # Answer: 7-

# In[90]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[91]:


driver.get=("https://www.amazon.com/")


# In[95]:


prod_title=[]
prod_rating=[]
prod_price=[]


# In[100]:


title_tags=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in title_tags[0:10]:
    title=i.text
    prod_title.append(title)
    
rating_tags=driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')
for i in rating_tags[0:10]:
    rating=i.text
    prod_rating.append(rating) 
    
price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags[0:10]:
    price=i.text
    prod_price.append(price)    


# In[97]:


print(len(prod_title),len(prod_rating),len(prod_price))


# In[98]:


prod_title


# In[101]:


prod_rating


# In[102]:


prod_price


# # Answer: 8-

# In[103]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[104]:


driver.get=("https://www.azquotes.com/")


# In[108]:


top_quote=[]
quote_author=[]
type_of_quote=[]


# In[109]:


start=0 
end=10 
for page in range(start,end):
    quote=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote:
        top_quote.append(i.text)
    
    author=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in author:
        quote_author.append(i.text)
    
    type=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in type:
        type_of_quote.append(i.text)
        
    next_button=driver.find_element(By.XPATH,'//li[@class="next"]')
    next_button.click()
    time.sleep(3)


# In[110]:


print(len(top_quote),len(quote_author),len(type_of_quote))


# In[111]:


top_quote


# In[112]:


quote_author


# In[113]:


type_of_quote


# # Answer: 9-

# In[114]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[115]:


driver.get=("https://www.azquotes.com/")


# In[119]:


details=[]


# In[121]:


detail_tags=driver.find_elements(By.XPATH,'//div[@class="table-box"]')
for i in detail_tags:
    detail=i.text
    details.append(detail)


# In[123]:


print(len(details))


# In[124]:


df=pd.DataFrame({'Details':details})
df


# ##Didn't know how to scrap data from tags that are without class

# # Answer: 10-

# In[125]:


driver=webdriver.Chrome(r"C:\Users\anshu\Downloads\chromedriver_win32\chromedriver.exe")


# In[126]:


driver.get=("https://www.motor1.com/")


# In[127]:


name_of_car=[]
price_of_car=[]
detail_of_car=[]


# In[130]:


name_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in name_tags:
    name=i.text
    name_of_car.append(name)
    
price_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]/p')
for i in price_tags:
    price=i.text
    price_of_car.append(price)
    
detail_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]/p')
for i in detail_tags:
    detail=i.text
    detail_of_car.append(detail)    


# In[131]:


print(len(name_of_car),len(price_of_car),len(detail_of_car))


# ##Didn't know how to scrap data from tags that are without class

# In[132]:


name_of_car


# In[ ]:




