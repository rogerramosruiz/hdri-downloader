from selenium import webdriver
from selenium.webdriver.common.by import By 
import concurrent.futures


allUrls = []

def poly_heaven(br):
    """
    br: Selnuim web driver

    Scraps in dl.polyhaven.org
    """
    download_url = 'https://dl.polyhaven.org/file/ph-assets/HDRIs/exr/8k/{}_8k.exr'
    br.get('https://polyhaven.com/hdris')
    items = br.find_elements(By.CLASS_NAME, 'GridItem_gridItem__0cuEz')
    download_urls = []
    for i in items:
        name = i.get_attribute('href').split('/')[-1]
        download_urls.append(download_url.format(name))
    return download_urls

def hdri_hub(br):
    """
    br: Selnuim web driver

    Scraps in hdri-hub.com
    """
    br.get('https://www.hdri-hub.com/hdrishop/freesamples/freehdri')
    items = br.find_elements(By.CLASS_NAME, 'catItemBody')
    download_urls = []
    urls = [url.find_element(By.TAG_NAME, 'a').get_attribute('href') for url in items]
    for i in urls:   
        br.get(i)
        dowload_url = br.find_element(By.XPATH, '//*[@id="btnBuyNow"]/a').get_attribute('href')
        download_urls.append(dowload_url)
    return download_urls

def ambientcg(br):
    """
    br: Selnuim web driver

    Scraps in ambientcg.com
    """
    br.get('https://ambientcg.com/list?type=HDRI')
    items = br.find_elements(By.TAG_NAME, 'a')
    urls = [i.get_attribute('href') for i in items]
    download_urls = []
    for i in urls:
        if('https://ambientcg.com/view?' in i and 'SkyOnly' not in i):
            br.get(i)
            download_url = br.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[2]/a[4]').get_attribute('href')
            download_urls.append(download_url)
    return download_urls

def scrap(fun):
    # Create a webdrider for google chrome in the background
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    br = webdriver.Chrome(options=op)
    # scrapped urls
    urls = fun(br)
    allUrls.append(urls)
    br.close()
    return urls

def start(file_name):
    """
    file_name: file to save hdri urls
    """
    # scrapper functions
    execute = [poly_heaven, hdri_hub, ambientcg]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scrap, execute)
    # Write all the urls could be scrapped in a file
    with open(file_name, 'w') as f:
        for urls in allUrls:
            for url in urls:
                f.write(url)
                if url != allUrls[-1][-1]: 
                    f.write('\n')        
