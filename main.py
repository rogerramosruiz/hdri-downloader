import concurrent.futures
import scrapper
from download import readUrls, download, unzipAll
import os

def main():
    urlsFile = 'urls.txt'
    downloadDir = 'downloads'
    if not os.path.exists(urlsFile):
        print("-------------------- Scrapping --------------------------------------------------")
        scrapper.start(urlsFile)
    urls = readUrls(urlsFile)
    print('--------------------------- Downloading ---------------------------------------------')
    print(f'# Acrchivos a descargar: {len(urls)}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(download, urls)
    unzipAll(downloadDir)
    os.remove(urlsFile)

if __name__ == '__main__':
    main()