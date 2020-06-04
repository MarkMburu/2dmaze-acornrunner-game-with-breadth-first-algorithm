import subprocess
from test_game import TestGame as test_game
from test_grid import TestGrid as test_grid
from test_parser import TestParser as test_parser

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_game()
test_grid()
test_parser()

# Run the e2e script
subprocess.call(['/test_e2e.sh'])