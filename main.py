from getNames import load_database
from getSolution import get_solution
from utils import newDriver


def run():

    url = "https://dotadle.net/classic"

    options, driver, wait = newDriver(headless=True)

    load_database(url)

    get_solution(options, driver, wait, url)

    driver.quit()

run()