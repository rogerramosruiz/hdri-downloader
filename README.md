# HDRI DOWNLOADER
## Talbe of contents
- [Requirements](#requirements)
- [Warning](#warning)
- [clone repo](#clone-repo)
- [Set up](#set-up)
    - [Download driver](#download-driver)
    - [Create a virtual environmet](#create-a-virtual-environmet)
- [Run](#run)

## Requirements
- python
- google chrome

## Warning

Given that the websites may change, the scrapper might not work properly

## Clone repo

```bash
git clone https://github.com/rogerramosruiz/hdri-downloader.git
cd hdri-downloader
```

## Set up
### Download driver
Download selenium web driver depending on your Google chrome version:

https://chromedriver.chromium.org/downloads

Unzip the file and and copy the chromedriver in the directory

### Create a virtual environmet

```powershell
python -m venv venv
venv\Scripts\activate
pip3 install -r requirements.txt
```

## Run

```bash
python main.py
```