# scraper-for-us-schools
Scraper built using python's `selenium` and `beautifulsoup4` packages to scrape School Leader's email from https://www.greatschools.org/

# Install pip packages from `requirements.txt`
In a terminal in the root folder, install the dependencies required using the following command
```bash
pip install -r requirements.txt
```

# Choosing the states to scrape for greatschools.org
In `states.json`, remove the states that you do not want to scrape from.
To get back all available states to scrape from, run the `getstates.py` python script.

```bash
python getstates.py
```

This will populate `states.json` back with the original list of states that are available to be scraped from. 
`states.json` is used in `scrape.py` script.

# Adding the file name to store data on line 75 of `scrape.py`

Change the name of the `csv` file you want to scrape the data into
![image](https://github.com/Jackimaru96/scraper-for-us-schools/assets/29891801/d819eb7b-76fd-4754-8b16-829fd2c40534)

# Run python script `scrape.py`
In a terminal in the root folder, install the dependencies required using the following command
```bash
python scrape.py
```
