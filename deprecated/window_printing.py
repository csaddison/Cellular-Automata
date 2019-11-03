#
# 6/3/19
#
# --------------------------------------------------------------------------------------
"""
Testing different ways to dynmically update console output.
"""
# --------------------------------------------------------------------------------------

# Method 1
"""
import sys
import time

for i in range(10):
    sys.stdout.write("\r{0}>".format("="*i))
    sys.stdout.flush()
    time.sleep(0.5)
"""

# Method 2

import time
import curses

def pbar(window):
    for i in range(10):
        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        window.refresh()
        time.sleep(0.5)

curses.wrapper(pbar)