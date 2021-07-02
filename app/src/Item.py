from app.src.SiteEnum import SiteEnum
from app.src import mail


class Item:
    url: str
    item_name: str
    price: float
    site: SiteEnum


    def __str__(self) -> str:
        return "item_name: " + self.item_name + "\nurl: " + self.url +\
        "\nprice: " + str(self.price) + "\nsite: " + str(self.site)


    def get_url(self) -> str:
        return self.url


    def send_notification(self) -> None:
        mail.send_email(self.item_name, self.url, self.price)


    def __init__(self, url: str, item_name: str, price: float, site: SiteEnum) -> None:
        self.url = url
        self.item_name = item_name
        self.price = price
        self.site = site
