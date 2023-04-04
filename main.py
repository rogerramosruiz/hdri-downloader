import concurrent.futures
import scrapper
from download import read_urls, download, unzip_all
import os

def main():
    urls_file = 'urls.txt'
    download_dir = 'downloads'
    if not os.path.exists(urls_file):
        print("-------------------- Scrapping --------------------------------------------------")
        scrapper.start(urls_file)
    urls = read_urls(urls_file)
    print('--------------------------- Downloading ---------------------------------------------')
    print(f'# Files to download: {len(urls)}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(download, urls)
    unzip_all(download_dir)
    os.remove(urls_file)

if __name__ == '__main__':
    main()