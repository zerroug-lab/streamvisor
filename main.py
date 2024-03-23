import requests
from bs4 import BeautifulSoup

url = "https://yallalive.sx/"
new_telegram_link = "https://t.me/visorstream"

# Make a request to the target URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Remove the unwanted elements
for element in soup.select('#topnav, #AlbaSport\_header, #colophon, .AlbaSport-main'):
    element.extract()

# Replace the old Telegram link with the new one
for link in soup.find_all('a', href=True):
    if link['href'] == 'https://t.me/yallaosx':
        link['href'] = new_telegram_link

# Print the modified HTML content
print(soup.prettify())

# Write the modified HTML content to a file
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))