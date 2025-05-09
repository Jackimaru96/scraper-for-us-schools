# 📚 Scraper for US Schools on GreatSchools.org

This Python-based scraper uses `selenium` and `beautifulsoup4` to extract school leader emails from [GreatSchools.org](https://www.greatschools.org/). It navigates through school listings for selected states and captures:

- School name
- School leader's name
- Email addresses

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/scraper-for-us-schools.git
cd scraper-for-us-schools
```

### 2. Install Required Python Packages

```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuration

### 1. Choose States to Scrape

- Open `states.json` and remove any states you **do not** want to scrape.
- To restore the full list of available states:

  ```bash
  python getstates.py
  ```

  This script populates `states.json` by scraping state links from GreatSchools.org.

### 2. Set Output File Name

- Open `scrape.py` and go to **line 75**.
- Change the filename (`us_school_emails.csv`) if you want to use a different output file.

---

## 🚀 Run the Scraper

Make sure you have `chromedriver` installed at the correct location:

- Mac: `/usr/local/bin/chromedriver`
- Windows: Update the path in the script if needed (`./chromedriver.exe`)

Then, run the main scraper:

```bash
python scrape.py
```

---

## 📁 Output

The script generates a CSV file with the following columns:

- State
- School URL
- School Name
- School Leader Name
- Email Address

---

## 🧪 Example Output

| State | URL          | School Name     | Leader Name | Email                                     |
| ----- | ------------ | --------------- | ----------- | ----------------------------------------- |
| CA    | https\://... | ABC High School | Jane Doe    | [jdoe@school.edu](mailto:jdoe@school.edu) |

---

## ⚠️ Notes

- The scraper runs headless via Chrome and uses `WebDriverWait` for dynamic page content.
- Pagination is handled automatically until the end of listings.
- Error handling is included to retry or skip failed pages.

---

## 🧼 Clean Exit

After scraping, the script ensures the Chrome driver is shut down to free system resources.

---

## 📌 Requirements

- Python 3.7+
- Google Chrome
- [chromedriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version
- Required packages (auto-installed via `requirements.txt`):

  - `selenium`
  - `beautifulsoup4`

---

## 🤝 Contributions

Feel free to fork and contribute via pull requests! Bug fixes, feature suggestions, and performance improvements are welcome.
