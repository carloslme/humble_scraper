import requests
from bs4 import BeautifulSoup

#main_link = 'https://porn.jules-aubert.info/humble_bundle/python_by_oreilly/'
main_link = 'https://porn.jules-aubert.info/humble_bundle/programming_by_packt/'

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
    #if i == 5:
    #    break
    
    if ('.pdf' in link.get('href', [])):
        
        book_name = link.get('href')
        full_link = main_link + book_name
        
        print(f"Downloading file number {i}: {full_link}")
        
        # Get response object for link
        response = requests.get(full_link)

        # Write content in pdf file
        with open(f"{book_name}.pdf", 'wb') as pdf:
            pdf.write(response.content)

        print(f"File {i}: {book_name} downloaded")
        
        i += 1