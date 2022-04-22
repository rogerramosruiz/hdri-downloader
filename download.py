import requests
import os 
import zipfile
import shutil

def unzip(dir, zipName):
    zipName = f'{dir}/{zipName}'
    unzipFile = type('obj', (object,), {'file_size' : 0})
    with zipfile.ZipFile(zipName, 'r') as zip:
        for zinfo in zip.filelist:
            if zinfo.file_size > unzipFile.file_size:
                unzipFile = zinfo
        zip.extract(unzipFile.filename, dir)
    
    fileName = os.path.join(dir, unzipFile.filename.split('/')[-1])
    print(fileName)
    if not os.path.exists(fileName):
        os.rename(f'{dir}/{unzipFile.filename}', fileName)
    extractDir = os.path.join(dir, unzipFile.filename.split('/')[0])
    if os.path.isdir(extractDir): 
        shutil.rmtree(extractDir)
    os.remove(zipName)

def unzipAll(dir):
    print("------------------------------ Unziping files --------------------------------")
    list = os.listdir(dir)
    for i in list:
        if i.split('.')[-1] == 'zip':
            unzip(dir, i)
            print(f'unziped {i}')
def cleanString(str):
    weirdChars = ['/', '\\', ':', '?', '"', '<','>','|', '=']
    s = ''
    for i in str:
        if i in weirdChars:
            s = ''
        else:
            s += i
    return s

def download(url):
    dir = 'downloads'
    if not os.path.exists(dir):
        os.mkdir(dir)
    name = url.split('/')[-1]
    name = cleanString(name)
    fileName =  f'{dir}/{name}'
    if not os.path.exists(fileName):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        file = requests.get(url, headers= headers).content
        with open(fileName, 'wb') as f:
            f.write(file)
        print(f'Downloaded {name}')
    else:
        print(f'Skip {name}')

def chechkDownloaded(dir, urls):
    files = os.listdir(dir) 
    nodownloaded = []
    for url in urls:
        b = True
        for i in files:
            if i in url:
                b = False
                break
        if b:
            nodownloaded.append(url)  
    return nodownloaded

def readUrls(file):
    if not os.path.exists(file):
        print(f'No existe {file}')
        return 
    with open(file, 'r') as f:
        urls = f.read().splitlines()
    return urls