from getNames import load_database, newDriver
from getSolution import get_solution


def run():

    options, driver, wait = newDriver()

    #load_database("https://loldle.net/classic")

    get_solution(options, driver, wait, "https://loldle.net/classic")

    driver.quit()

run()