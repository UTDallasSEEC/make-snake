#!/usr/bin/env python

# theme.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import os
import sys
import curses
import shutil
import parser
import themes
import xml.etree.ElementTree as ET

from kano.utils import ensure_dir
themeName = 'custom_theme'
app_dir = os.path.expanduser('~/Snake-content')
custom_file = app_dir + '/' + themeName
colors_map = {}
theme = None
defaultThemes = ['classic', 'minimal', 'jungle', '80s']
themeList = []
def init():
    global theme, colors_map, themeList
    themeIn = parser.options.theme
    #populate the themeList
    update_theme_list()

    if themeIn in defaultThemes:
        #determine if input is a default
        try:
            theme = themes.game_themes[themeIn]
        except:
            print "Can't find theme: %s" %(themeIn)
            exit()
    elif themeIn in themeList:
        #Check it if exists in Snake-content
        themeName = themeIn
        try:
            load_custom_theme( themeName )
        except:
            print "Error opening theme: %s" %(themeIn)
    else:
        #if it is not a created theme let user know
        print "Can't find theme: %s" %(themeIn)

    colors_map = get_colors_map()

def update_theme_list():
    global themeList
    themeList = os.listdir(app_dir)

def get_color(key):
    return curses.color_pair(colors_map.get(key, 0))


def get_tile(key):
    return theme['tiles'].get(key, ' ')


def get_colors_map():
    out = {}

    i = 1
    for col in theme['colors'].iteritems():
        curses.init_pair(i, col[1][0], col[1][1])
        out[col[0]] = i
        i += 1

    return out


def load_custom_theme( themeName ):
    global theme
    custom_file = app_dir + '/' + themeName
    try:
        with open(custom_file):
            # Init theme
            theme = themes.game_themes['classic']
            # Parse XML
            tree = ET.parse(custom_file)
            root = tree.getroot()
            # Colors
            theme['colors']['bg'] = (get_curses_color(root[0][0].attrib.get('font')),
                                     get_curses_color(root[0][0].attrib.get('background')))
            theme['colors']['snake'] = (get_curses_color(root[0][1].attrib.get('font')),
                                        get_curses_color(root[0][1].attrib.get('background')))
            theme['colors']['apple'] = (get_curses_color(root[0][2].attrib.get('font')),
                                        get_curses_color(root[0][2].attrib.get('background')))
            theme['colors']['border'] = (get_curses_color(root[0][3].attrib.get('font')),
                                         get_curses_color(root[0][3].attrib.get('background')))
            theme['colors']['lives'] = (get_curses_color(root[0][4].attrib.get('font')),
                                        get_curses_color(root[0][4].attrib.get('background')))
            # Tiles
            theme['tiles']['bg'] = root[1][0].text
            theme['tiles']['snake-body'] = root[1][1].text
            theme['tiles']['apple'] = root[1][2].text
            theme['tiles']['border-h'] = root[1][3].text
            theme['tiles']['border-v'] = root[1][4].text
            theme['tiles']['border-c'] = root[1][5].text
            theme['tiles']['lives'] = root[1][6].text

    except IOError:
        pass


def get_curses_color(string):
    if string == 'Black':
        return curses.COLOR_BLACK
    elif string == 'Red':
        return curses.COLOR_RED
    elif string == 'Green':
        return curses.COLOR_GREEN
    elif string == 'Yellow':
        return curses.COLOR_YELLOW
    elif string == 'Blue':
        return curses.COLOR_BLUE
    elif string == 'Magenta':
        return curses.COLOR_MAGENTA
    elif string == 'Cyan':
        return curses.COLOR_CYAN
    else:
        return curses.COLOR_WHITE
