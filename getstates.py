import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.greatschools.org/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Use a set to store unique states
states = set()

# Find div with class 'col-sm-12'
for div in soup.find_all('div', class_='col-sm-12'):
    # Iterate over all the <a> tags within the found div
    for link in div.find_all('a', href=True):
        href = link.get('href')
        
        parts = href.split('/')  # split the URL by '/'
        if len(parts) > 3:  # a valid URL in the specified format should have more than 3 parts
            state = parts[3]  # the state is the fourth part (index 3) of the URL
            states.add(state)
# Convert the set to a list, if needed
states_list = list(states)

with open('states.json', 'w') as f:
    json.dump(states_list, f)

print("States have been written to states.json")
