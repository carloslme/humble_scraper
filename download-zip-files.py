from bs4 import BeautifulSoup
import requests
import shutil

main_link = 'https://porn.jules-aubert.info/humble_bundle/applied_math_productivity_by_mercury/'

# Making a GET request
r = requests.get(main_link)

soup = BeautifulSoup(r.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')
#print(links)
i = 0
  
# From all links check for pdf link and
# if present download file
for link in links:
    # Uncomment the following line to process 
    # an specific number of files
    if i == 3:
        break
    
    if ('.zip' in link.get('href', [])):
        
        book_name = link.get('href')
        full_link = main_link + book_name
        
        print(f"Downloading file number {i+1}: {full_link}")
        
        # Get response object for link
        response = requests.get(full_link)

        # Write content in pdf file
        with open(f"{book_name}", 'wb') as pdf:
            pdf.write(response.content)

        print(f"File {i+1}: {book_name} downloaded")
        
        # Unzip the file
        shutil.unpack_archive(book_name, "./")
        print(f"File {i+1}: {book_name} unzipped.")
        i += 1