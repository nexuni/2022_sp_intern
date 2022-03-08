import string
from functools import reduce
# please reference https://www.trust.org.tw/upload/1100002250002.pdf
# or code in C++ https://cynthiachuang.github.io/Check-Tax-ID-Number/

def check_taiwan_tax_id(tax_id):
    """
    Input
        - tax_id: str
    Output
        - boolean
    """
    multiplier = [1,2,1,2,1,2,4,1]
    mod = 10

    assert len(multiplier) == len(tax_id), f"tax_id({len(tax_id)}) and multiplier({len(multiplier)}) length mismatch."
    
    product = [int(d) * m for (d,m) in zip(tax_id, multiplier)]
    s = sum(map(lambda x: x%10 + x//10, product))

    return s % mod == 0 or ( (s+1) % mod == 0 and tax_id[6] == '7' )

import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://sheethub.com/data.gcis.nat.gov.tw/統一編號列表"
)

soup = BeautifulSoup(response.text, "html.parser")
result = soup.find(id="table")
test_case = [id.getText() for id in result.select("a")]

for t in test_case:
    print(f"{t}: {check_taiwan_tax_id(t)}")
    
# Test data
print(check_taiwan_tax_id("53619559"))
print(check_taiwan_tax_id("53619549"))
print(check_taiwan_tax_id("64387543"))
print(check_taiwan_tax_id("23328674"))
print(check_taiwan_tax_id("23328673"))
print(check_taiwan_tax_id("19312376"))
print(check_taiwan_tax_id("10458575"))
print(check_taiwan_tax_id("04595257"))
print(check_taiwan_tax_id("00000000"))
print(check_taiwan_tax_id("23673"))