import bs4, requests

def getURL(url): 
    res = requests.get(url)
    if not res.raise_for_status():
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        elems = soup.select("#ViewItemPage > div:nth-child(5) > div.itemTitleWrapper-4111598823 > div.mainColumn-1522885425 > div > div > span > span:nth-child(1)")
        return elems[0].text.strip()

price = getURL("https://www.kijiji.ca/v-laptops/markham-york-region/lenovo-x220-laptop/1493225213")