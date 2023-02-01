from bs4 import BeautifulSoup
import requests
import shutil

def download_file(link_str: str):
    book_name = link_str.get('href')
    full_link = main_link + book_name
    
    print(f"Downloading file number: {full_link}")
    
    # Get response object for link
    response = requests.get(full_link)
    
    # Write content in pdf file
    with open(f"{book_name}", 'wb') as file:
        file.write(response.content)

    print(f"File {book_name} downloaded")
    

def process_zip_file(book_name: str):
    # Unzip the file
    shutil.unpack_archive(book_name, "./")
    print(f"File: {book_name} unzipped.")

main_link = 'https://porn.jules-aubert.info/humble_bundle/applied_math_productivity_by_mercury/'

# Making a GET request
r = requests.get(main_link)

soup = BeautifulSoup(r.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

file_types = [".zip", ".pdf"]

# From all links check for pdf link and
# if present download file
for link in links:
    href = link.get('href', [])
    book_name = link.get('href')

    if file_types[0] in href or file_types[1] in href:
        download_file(link_str=link)
    
    if file_types[0] in href:
        process_zip_file(book_name)