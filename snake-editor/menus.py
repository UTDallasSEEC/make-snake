
# menus.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
import os

colors = [["Black", None], ["Red", None], ["Green", None], ["Yellow", None],
          ["Blue", None], ["Magenta", None], ["Cyan", None], ["White", None]]

# Elements
snake = [["Background colour", colors], ["Snake body", "symbols"],
         ["Symbol colour", colors], ["Back", None]]
lives = [["Background colour", colors], ["Lives symbol", "symbols"],
         ["Symbol colour", colors], ["Back", None]]
apple = [["Background colour", colors], ["Apple symbol", "symbols"],
         ["Symbol colour", colors], ["Back", None]]
# Board
border = [["Background colour", colors], ["Corner symbol", "symbols"],
          ["Horizontal symbol", "symbols"], ["Vertical symbol", "symbols"],
          ["Corner symbol", "symbols"], ["Back", None]]
background = [["Background colour", colors], ["Symbol colour", colors],
              ["Background symbol", "symbols"], ["Back", None]]
# Main attributes menues

background = [["Background colour", colors], ["Background symbol", "symbols"],
              ["Symbol colour", colors], ["Back", None]]
# Main
elements = [["Snake", snake], ["Lives", lives], ["Apples", apple],
            ["Back", None]]
board = [["Background", background], ["Border", border], ["Back", 0]]

delete = [["Really Delete?","yep"],["Yes","delete"],["No",0]]

editMain = [["Board", board], ["Elements", elements],["Delete",delete], ["Back", 0]]

newName = [["Name","name"], ["Back", 0]]

#Setup for the theme menus
#pull list of other themes. Need to use OS
fileLocal = os.path.expanduser('~/Snake-content')
themes = os.listdir(fileLocal)
naming = []
#append list of themes
for theme in themes:
    naming.append([theme,"existing"])

naming.append(["Back", 0])

main = [["New Theme", newName], ["Current Themes", naming], ["Exit", None]]
