import sys
from OneAtATime import runOneAtATime
from getNames import loadDatabase
import concurrent.futures


site1 = "https://loldle.net/classic"

site2 = "https://pokedle.net/classic"

site3="https://smashdle.net/classic"

site4 = "https://dotadle.net/classic"

site5 = "https://onepiecedle.net/classic"

site6 = "https://narutodle.net/classic"

sites = []

if len(sys.argv) > 1:
    first_arg = sys.argv[1]
    first_arg = first_arg.lower()
    print(f"First argument: {first_arg}")
    
    if "loldle" in first_arg:
        sites.append(site1)
    elif "pokedle" in first_arg:
        sites.append(site2)
    elif "smashdle" in first_arg:
        sites.append(site3)
    elif "dotadle" in first_arg:
        sites.append(site4)
    elif "onepiecedle" in first_arg:
        sites.append(site5)
    elif "narutodle" in first_arg:
        sites.append(site6)

    else:
      print("Not available")
      sys.exit(0)
else:
    sites = [site1,site2,site3,site4,site5, site6]
    


#loadDatabase(site6)
runOneAtATime(sites)