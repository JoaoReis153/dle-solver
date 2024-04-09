from OneAtATime import runOneAtATime
from getNames import loadDatabase
from AllAtOnce import getSolution
import concurrent.futures

from AllAtOnce import runAllAtOnce

#LOL
#answer = "Diana"
site1 = "https://loldle.net/classic"

#POKEMON
#answer = "Magneton"
site2 = "https://pokedle.net/classic"

#SMASH
#answer = "Kirby"
site3="https://smashdle.net/classic"

#answer = "Sand King"
site4 = "https://dotadle.net/classic"

#sites = [site1, site2, site4]
#sites = [site1,site2,site4, site3]
sites = [site1, site2, site3, site4]


runOneAtATime(sites)
#runAllAtOnce(sites)




#loadDatabase(answer, site4)
#getSolution(site1)
#getSolution(site2)
#getSolution(site4)
#getSolution(site3)
