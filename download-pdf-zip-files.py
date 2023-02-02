
from typing_extensions import Literal
from bs4 import BeautifulSoup
import requests
import shutil

def download_file(link_str: any):
    """This function takes a BeautifulSoup string with
    the link and try download it. If it fails, it returns 
    the exception.

    Args:
        link_str (any): It is the file link.

    Returns:
        bool: True if all was correctly executed, str if error.
    """
    try:
        book_name = link_str.get('href')
        full_link = main_link + book_name
        
        print(f"Downloading file number: {full_link}")
        
        # Get response object for link
        response = requests.get(full_link)
        
        # Write content in pdf file
        with open(f"{book_name}", 'wb') as file:
            file.write(response.content)
    
        return True

    except Exception as err:
        #print(f"Unexpected {err}, {type(err)}")
        return err


def process_zip_file(book_name: str):
    """This function takes a zipe file path and
    try to unzip it.

    Args:
        book_name (str): It is the zip file path.

    Returns:
        bool: True if all was correctly executed, str if error.
    """
    try:
        # Unzip the file
        shutil.unpack_archive(book_name, "./")
        return True
    except Exception as err:
        return err

main_link = 'https://porn.jules-aubert.info/humble_bundle/applied_math_productivity_by_mercury/'

# Making a GET request
r = requests.get(main_link)

soup = BeautifulSoup(r.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

# List of allowed file types
file_types = [".zip", ".pdf"]

# From all links check for an allowed file link and
# if present download it and process if needed.
for link in links[6:7]:
    href = link.get('href', [])
    book_name = link.get('href')

    if file_types[0] in href or file_types[1] in href:
        result = download_file(link_str=link)
        if result == True:
            print(f"File {book_name} downloaded")
            
            # If file is zip, then unzip it
            if file_types[0] in href:
                result_unzip = process_zip_file(book_name)
                if result_unzip == True:
                    print(f"File: {book_name} unzipped.")
                else:
                    print(f"Error while unzipping the book {book_name}. Please contact your admin.")
        else:
            print(f"Error while downloading the book {book_name}. Please contact your admin.")
