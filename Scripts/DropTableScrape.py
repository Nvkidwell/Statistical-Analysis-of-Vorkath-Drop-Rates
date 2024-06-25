import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'https://oldschool.runescape.wiki/w/Vorkath'

# Fetches the HTML content
response = requests.get(url)
html_content = response.text

# Parses HTML 
soup = BeautifulSoup(html_content, 'html.parser')

# Finds drop table
table = soup.find('table', class_='wikitable')

# Stores data in an empty lis
data = []

# Extracts data but exludes the header string
rows = table.find_all('tr')

# For loo[ that iteriates to skip the header
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) == 0:
        continue 
    
    item_name = cols[0].text.strip()
    quantity = cols[1].text.strip()
    rarity = cols[2].text.strip()
    price_range = cols[3].text.strip()
    
    # Clean and format the data
    rarity = re.sub(r'\s*x\s*', '/', rarity)
    price_range_clean = re.sub(r'[^\d,-]', '', price_range).replace(',', '').replace('-', ' - ')
    
    # Splits the price range if two ranges are present (i.e min/max)
    if ' - ' in price_range_clean:
        min_price, max_price = map(int, price_range_clean.split(' - '))
    else:
        min_price = max_price = int(price_range_clean)
    
    # append the data to a dictionary
    data.append({
        'Item Name': item_name,
        'Quantity': quantity,
        'Rarity': rarity,
        'Min Price': min_price,
        'Max Price': max_price
    })

# Creates the new data frame
df = pd.DataFrame(data)


print(df)
# Exports data frame to csv file
df.to_csv('Vorkath_Drop_Table.csv', index=False)
