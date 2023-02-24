import curses
import datetime

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Clear screen and draw border
    stdscr.clear()
    stdscr.border(0)

    # Display time and date
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stdscr.addstr(2, 2, "Current time: " + now)

        # Refresh the screen every second
        stdscr.refresh()
        curses.napms(1000)

curses.wrapper(main)