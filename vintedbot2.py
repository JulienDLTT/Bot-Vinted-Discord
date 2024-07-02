from vinted_scraper import VintedScraper


def main():
    scraper = VintedScraper("https://www.vinted.fr/")  # init the scraper with the baseurl
    params = {
        "search_text": "adidas"
        # Add other query parameters like the pagination and so on
    }
    items = scraper.search(params)  # get all the items
    item = items[0]  # get the first Item of the list
    scraper.item(item.id)  # get more info about a particular item

    item = item.url
    print(item)

if __name__ == "__main__":
    main()