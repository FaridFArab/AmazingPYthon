import re
import requests

url = "https://www.pythonpool.com/contact-us"
email_regex = r"[\w\.-]+@[\w\.-]+"

r = requests.get(url)

for re_match in re.findall(email_regex, r.text):
    print(re_match)
