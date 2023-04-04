import requests
import os 
import zipfile
import shutil

def unzip(dir, zip_name):
    """
    dir: Download directory
    zip_name: Zip file name
    """
    zip_name = f'{dir}/{zip_name}'
    unzip_file = type('obj', (object,), {'file_size' : 0})
    with zipfile.ZipFile(zip_name, 'r') as zip:
        for zinfo in zip.filelist:
            if zinfo.file_size > unzip_file.file_size:
                unzip_file = zinfo
        zip.extract(unzip_file.filename, dir)
    
    file_name = os.path.join(dir, unzip_file.filename.split('/')[-1])
    print(file_name)
    if not os.path.exists(file_name):
        os.rename(f'{dir}/{unzip_file.filename}', file_name)
    extract_dir = os.path.join(dir, unzip_file.filename.split('/')[0])
    if os.path.isdir(extract_dir): 
        shutil.rmtree(extract_dir)
    os.remove(zip_name)

def unzip_all(dir):
    """
    dir: directory where are the zipped files

    """
    print("------------------------------ Unziping files --------------------------------")
    list = os.listdir(dir)
    for i in list:
        if i.split('.')[-1] == 'zip':
            unzip(dir, i)
            print(f'unziped {i}')
def clean_string(str):
    wierd_chars = ['/', '\\', ':', '?', '"', '<','>','|', '=']
    s = ''
    for i in str:
        if i in wierd_chars:
            s = ''
        else:
            s += i
    return s

def download(url):
    dir = 'downloads'
    if not os.path.exists(dir):
        os.mkdir(dir)
    name = url.split('/')[-1]
    name = clean_string(name)
    file_name =  f'{dir}/{name}'
    if not os.path.exists(file_name):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        file = requests.get(url, headers= headers).content
        with open(file_name, 'wb') as f:
            f.write(file)
        print(f'Downloaded {name}')
    else:
        print(f'Skip {name}')

def chechk_downloaded(dir, urls):
    files = os.listdir(dir) 
    not_downloaded = []
    for url in urls:
        b = True
        for i in files:
            if i in url:
                b = False
                break
        if b:
            not_downloaded.append(url)  
    return not_downloaded

def read_urls(file):
    if not os.path.exists(file):
        print(f'No existe {file}')
        return 
    with open(file, 'r') as f:
        urls = f.read().splitlines()
    return urls