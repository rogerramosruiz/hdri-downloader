from fileinput import filename
from selenium import webdriver
from selenium.webdriver.common.by import By 
import concurrent.futures
import os 

allUrls = []

def PolyHeaven(br):
    downloadUrl = 'https://dl.polyhaven.org/file/ph-assets/HDRIs/exr/8k/{}_8k.exr'
    br.get('https://polyhaven.com/hdris')
    items = br.find_elements(By.CLASS_NAME, 'GridItem_gridItem__0cuEz')
    downloadUrls = []
    for i in items:
        name = i.get_attribute('href').split('/')[-1]
        downloadUrls.append(downloadUrl.format(name))
    return downloadUrls

def hdri_hub(br):
    br.get('https://www.hdri-hub.com/hdrishop/freesamples/freehdri')
    items = br.find_elements(By.CLASS_NAME, 'catItemBody')
    downloadUrls = []
    urls = [url.find_element(By.TAG_NAME, 'a').get_attribute('href') for url in items]
    for i in urls:   
        br.get(i)
        dowloadurl = br.find_element(By.XPATH, '//*[@id="btnBuyNow"]/a').get_attribute('href')
        downloadUrls.append(dowloadurl)
    return downloadUrls

def ambientcg(br):
    br.get('https://ambientcg.com/list?type=HDRI')
    items = br.find_elements(By.TAG_NAME, 'a')
    urls = [i.get_attribute('href') for i in items]
    downloadUrls = []
    for i in urls:
        if('https://ambientcg.com/view?' in i and 'SkyOnly' not in i):
            br.get(i)
            downloadurl = br.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[2]/a[4]').get_attribute('href')
            downloadUrls.append(downloadurl)
    return downloadUrls

def scrap(fun):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    br = webdriver.Chrome(options=op)
    urls = fun(br)
    allUrls.append(urls)
    br.close()
    return urls

def start(filename):
    execute = [PolyHeaven, hdri_hub, ambientcg]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scrap, execute)
    
    with open(filename, 'w') as f:
        for urls in allUrls:
            for url in urls:
                f.write(url)
                if url != allUrls[-1][-1]: 
                    f.write('\n')        
