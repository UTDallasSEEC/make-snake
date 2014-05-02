
# menus.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
import os

colors = [["Black", None], ["Red", None], ["Green", None], ["Yellow", None],
          ["Blue", None], ["Magenta", None], ["Cyan", None], ["White", None]]

# Elements
snake = [["Background colour", colors], ["Symbol colour", colors],
         ["Snake body", "symbols"], ["Back", None]]
lives = [["Background colour", colors], ["Symbol colour", colors],
         ["Lives symbol", "symbols"], ["Back", None]]
apple = [["Background colour", colors], ["Symbol colour", colors],
         ["Apple symbol", "symbols"], ["Back", None]]
# Board
border = [["Background colour", colors], ["Symbol colour", colors],
          ["Horizontal symbol", "symbols"], ["Vertical symbol", "symbols"],
          ["Corner symbol", "symbols"], ["Back", None]]
background = [["Background colour", colors], ["Symbol colour", colors],
              ["Background symbol", "symbols"], ["Back", None]]
# Main
elements = [["Snake", snake], ["Lives", lives], ["Apples", apple],
            ["Back", None]]
board = [["Background", background], ["Border", border], ["Back", 0]]

main = [["Board", board], ["Elements", elements], ["Name","name"], ["Back", 0]]

newName = [["Name","name"], ["Back", 0]]
fileLocal = os.path.expanduser('~/Snake-content')
themes = os.listdir(fileLocal)
naming = []
naming.append(["New Theme",newName])
#append list of themes
for theme in themes:
    naming.append([theme,"existing"])

naming.append(["Exit", None])
