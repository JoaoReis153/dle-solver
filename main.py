from OneAtATime import runOneAtATime
from getNames import loadDatabase
import concurrent.futures


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

answer = "Jesus Burgess"
site5 = "https://onepiecedle.net/classic"

sites = [site5, site1, site2, site3, site4]


runOneAtATime(sites)
#runAllAtOnce(sites)

#loadDatabase(answer, site5)

