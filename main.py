from getNames import load_database
from getSolution import get_solution
from utils import newDriver


def run():

    options, driver, wait = newDriver(headless=True)

    #load_database("https://loldle.net/classic")

    get_solution(options, driver, wait, "https://loldle.net/classic")

    driver.quit()

run()