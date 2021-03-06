import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from app import db
from app.models import Item
from app.src.SiteEnum import SiteEnum
from app.src.Website import Website

os.environ['WDM_LOG_LEVEL'] = '0'


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--lang=nl")
options.add_argument("--disable-extensions")
options.add_argument("test-type")
options.add_argument("--log-level=3")
options.add_argument("headless")

price_dict = {"RTX3070": 1000, "RTX3070TI": 900,
              "RTX3080": 1400, "RTX3080TI": 1550, "RTX3090": 2050}


def alternate(driver, gpus):
    alternate = Website(html_item_grid="productBox", in_stock_text="Direct leverbaar",
                        html_price="price", site_enum=SiteEnum.Alternate)
    if 'RTX3070' in gpus:
        alternate.add_item(
            ("https://www.alternate.nl/Grafische-kaarten/RTX-3070", price_dict["RTX3070"]))
    if 'RTX3070TI' in gpus:
        alternate.add_item(
            ("https://www.alternate.nl/Grafische-kaarten/RTX-3070-TI", price_dict["RTX3070TI"]))
    if 'RTX3080' in gpus:
        alternate.add_item(
            ("https://www.alternate.nl/Grafische-kaarten/RTX-3080", price_dict["RTX3080"]))
    if 'RTX3080TI' in gpus:
        alternate.add_item(
            ("https://www.alternate.nl/Grafische-kaarten/RTX-3080-TI", price_dict["RTX3080TI"]))
    if 'RTX3090' in gpus:
        alternate.add_item(
            ("https://www.alternate.nl/Grafische-kaarten/RTX-3090", price_dict["RTX3090"]))

    return alternate.get_items(driver)


def azerty(driver, gpus):
    azerty = Website(html_item_grid="item-container", in_stock_text="Volgende werkdag in huis",
                     html_price="price", site_enum=SiteEnum.Azerty)

    if 'RTX3070' in gpus:
        azerty.add_item(
            ("https://azerty.nl/category/componenten/videokaarten/nvidia_geforce/nvidia_geforce_rtx_3070#&limit=96", price_dict["RTX3070"]))
    if 'RTX3070TI' in gpus:
        azerty.add_item(
            ("https://azerty.nl/category/componenten/videokaarten/nvidia_geforce/nvidia_geforce_rtx_3070_ti#&limit=96", price_dict["RTX3070TI"]))
    if 'RTX3080' in gpus:
        azerty.add_item(
            ("https://azerty.nl/category/componenten/videokaarten/nvidia_geforce/nvidia_geforce_rtx_3080#&limit=96", price_dict["RTX3080"]))
    if 'RTX3080TI' in gpus:
        azerty.add_item(
            ("https://azerty.nl/category/componenten/videokaarten/nvidia_geforce/nvidia_geforce_rtx_3080_ti#&limit=96", price_dict["RTX3080TI"]))
    if 'RTX3090' in gpus:
        azerty.add_item(
            ("https://azerty.nl/category/componenten/videokaarten/nvidia_geforce/nvidia_geforce_rtx_3090#&limit=96", price_dict["RTX3090"]))

    return azerty.get_items(driver)


def megekko(driver, gpus):
    megekko = Website(html_item_grid="productList", in_stock_text="Uit eigen voorraad leverbaar",
                      html_price="euro", site_enum=SiteEnum.Megekko)

    if 'RTX3070' in gpus:
        megekko.add_item(
            ("https://www.megekko.nl/Computer/Componenten/Videokaarten/Nvidia-Videokaarten/Graphics-Engine/GeForce-RTX-3070", price_dict["RTX3070"]))
    if 'RTX3070TI' in gpus:
        megekko.add_item(
            ("https://www.megekko.nl/Computer/Componenten/Videokaarten/Nvidia-Videokaarten/Graphics-Engine/GeForce-RTX-3070-TI", price_dict["RTX3070TI"]))
    if 'RTX3080' in gpus:
        megekko.add_item(
            ("https://www.megekko.nl/Computer/Componenten/Videokaarten/Nvidia-Videokaarten/Graphics-Engine/GeForce-RTX-3080", price_dict["RTX3080"]))
    if 'RTX3080TI' in gpus:
        megekko.add_item(
            ("https://www.megekko.nl/Computer/Componenten/Videokaarten/Nvidia-Videokaarten/Graphics-Engine/GeForce-RTX-3080-TI", price_dict["RTX3080TI"]))
    if 'RTX3090' in gpus:
        megekko.add_item(
            ("https://www.megekko.nl/Computer/Componenten/Videokaarten/Nvidia-Videokaarten/Graphics-Engine/GeForce-RTX-3090", price_dict["RTX3090"]))

    return megekko.get_items(driver)


def coolblue(driver, gpus):
    coolblue = Website(html_item_grid="product-card", in_stock_text="Morgen bezorgd",
                       html_price="sales-price__current", site_enum=SiteEnum.Coolblue)

    if 'RTX3070' in gpus:
        coolblue.add_item(
            ("https://www.coolblue.nl/videokaarten/nvidia-chipset/nvidia-geforce-rtx-3000-serie/nvidia-geforce-rtx-3070", price_dict["RTX3070"]))
    if 'RTX3080' in gpus:
        coolblue.add_item(
            ("https://www.coolblue.nl/videokaarten/nvidia-chipset/nvidia-geforce-rtx-3000-serie/nvidia-geforce-rtx-3080", price_dict["RTX3080"]))
    if 'RTX3090' in gpus:
        coolblue.add_item(
            ("https://www.coolblue.nl/videokaarten/nvidia-chipset/nvidia-geforce-rtx-3000-serie/nvidia-geforce-rtx-3090", price_dict["RTX3090"]))

    return coolblue.get_items(driver)


async def run(input_get_form):
    driver = webdriver.Chrome(ChromeDriverManager(
        print_first_line=False, log_level=0).install(), options=options)
    items = []
    all_gpus_list = price_dict.keys()

    if len(input_get_form) == 0:
        items.extend(alternate(driver, all_gpus_list))
        items.extend(azerty(driver, all_gpus_list))
        items.extend(megekko(driver, all_gpus_list))
    else:
        items.extend(alternate(driver, input_get_form))
        items.extend(azerty(driver, input_get_form))
        items.extend(megekko(driver, input_get_form))

    add_item_list_to_db(items)
    driver.quit()


def add_item_list_to_db(items: list):
    for item in items:
        db.session.add(
            Item(name=item.item_name, url=item.url, price=item.price))
    db.session.commit()
