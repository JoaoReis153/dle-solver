from OneAtATime import runOneAtATime
from getNames import loadDatabase
import concurrent.futures


site1 = "https://loldle.net/classic"

site2 = "https://pokedle.net/classic"

site3="https://smashdle.net/classic"

site4 = "https://dotadle.net/classic"

site5 = "https://onepiecedle.net/classic"

site6 = "https://narutodle.net/classic"

sites = [ site2, site3, site4, site5, site6]

#loadDatabase(site6)
runOneAtATime(sites)