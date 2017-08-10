import cProfile
from TextEditApp import run

pr = cProfile.Profile()
pr.enable()
run(True)
pr.disable()
pr.print_stats(sort="calls")
