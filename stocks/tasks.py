print(__name__, "package initiated")
import datetime
import time
from celery import shared_task
from django.apps import apps

#from .models import PriceLookupEvent
from .scraper import StockTickerScraper



@shared_task
def hello_world(num=1):
    time.sleep(num)
    print(f"hello world {num}")

@shared_task
def hello_world_async(num=1):
    hello_world.delay(num=1)
    hello_world.delay(num=2)
    hello_world.delay(num=3)
    hello_world.apply_async(kwargs={'num': 4}, countdown=10)


@shared_task
def perform_scrape(ticker='AAPL',service='echo'):
    client = StockTickerScraper(service=service)
    name,price = client.scrape(ticker=ticker)
    price = price.replace(",", "")
    price = price.replace("$", "")
    price = price.replace(" ", "")
    #could use a django signal
    #PriceLookupEvent = apps.get_model("APP_DIR_NAME","PriceLookupEvent")
    print(f"task {name}, {price} ticker from task -> {ticker}")
    PriceLookupEvent = apps.get_model("stocks","PriceLookupEvent")
    PriceLookupEvent.objects.create_event(ticker,price,name=name,source=service)


@shared_task
def company_price_scrape_task(instance_id, service='echo'):
    #print(instance.id)
    """
    Think about intervals

    """
    Company = apps.get_model("stocks","Company")
    obj = Company.objects.get(id=instance_id)
    ticker = obj.ticker
    perform_scrape(ticker=ticker,service=service)


@shared_task
def company_granular_price_scrape_task(instance_id, service='echo'):
    """
    Perform company price scraping event.
    """
    Company = apps.get_model("stocks", "Company")
    obj = Company.objects.get(id=instance_id)
    ticker = obj.ticker
    perform_scrape(ticker=ticker, service=service)
    if obj.has_granular_scraping:
        now = datetime.datetime.now()
        expires = now + datetime.timedelta(seconds=65)
        for i in range(1, 60): # 1 - 59
            perform_scrape.apply_async(kwargs={
                "ticker": ticker,
                "service": service
            }, countdown=i, expires=expires)