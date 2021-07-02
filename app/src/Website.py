import time
from app.src import SiteEnum, Item

if __name__ == "__main__":
    pass

URL = 0
PRICE = 1

class Website:
    # list of tuples
    # [0] = url
    # [1] = price
    # TODO change to a dict in the future
    items: list = []
    item_list: list = []


    def __init__(self, html_item_grid: str, in_stock_text: str, html_price: str, site_enum: SiteEnum):
        self.html_item_grid = html_item_grid
        self.in_stock_text = in_stock_text
        self.html_price = html_price
        self.site = site_enum


    def add_item(self, url_price_tuple: tuple):
            self.items.append(url_price_tuple)


    def strip_price(self, price):
        return float(price.strip("€ ,-").replace(".", "").replace(",", "."))


    def get_items(self, driver) -> list:
        for item in self.items:
            driver.get(item[URL])
            time.sleep(1.0)
            html_item_grid = driver.find_elements_by_class_name(self.html_item_grid)
            for gpu in html_item_grid:
                if gpu.text.find(self.in_stock_text) > 0:
                    price = self.strip_price(gpu.find_element_by_class_name(self.html_price).text)
                    if price < item[PRICE]:
                        self.item_list.append(self.create_item(gpu, price, self.site))
        return self.item_list


    def create_item(self, gpu, price: float, site: SiteEnum) -> Item:
        if self.site is SiteEnum.SiteEnum.Alternate:
            gpu_name = gpu.find_element_by_class_name("product-name").text
            url = gpu.get_attribute("href")
            return Item.Item(url, gpu_name, price, self.site)
        elif site is SiteEnum.SiteEnum.Coolblue:
            gpu_name = gpu.find_element_by_class_name("product-card__title").text
            url = gpu.find_element_by_class_name("link").get_attribute("href")
            return Item.Item(url, gpu_name, price, self.site)
        elif site is SiteEnum.SiteEnum.Azerty:
            gpu_name = gpu.find_element_by_tag_name("h3").text
            url = gpu.find_element_by_class_name("item-img").get_attribute("href")
            return Item.Item(url, gpu_name, price, self.site)
        elif site is SiteEnum.SiteEnum.Megekko:
            gpu_name = gpu.find_element_by_tag_name("h2").text
            url = gpu.find_element_by_tag_name("a").get_attribute("href")
            return Item.Item(url, gpu_name, price, self.site)
