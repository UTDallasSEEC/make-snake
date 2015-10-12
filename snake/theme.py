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
<<<<<<< HEAD
#from kano.utils import ensure_dir

CUSTOM_THEME_PATH = '/usr/share/make-snake/custom-theme.xml'
DEFAULT_THEMES = ['classic', 'minimal', 'jungle', '80s']
=======
>>>>>>> parent of b280dda... Added print argument to list themes, also added ability to play a saved theme @alexaverill

from kano.utils import ensure_dir
app_dir = os.path.expanduser('~/Snake-content')
<<<<<<< HEAD
CUSTOM_FILE = app_dir + '/custom-theme.xml'
=======
custom_file = app_dir + '/custom_theme'
>>>>>>> parent of b280dda... Added print argument to list themes, also added ability to play a saved theme @alexaverill
colors_map = {}
theme = None


def init():
    global theme, colors_map

    if parser.args.theme != 'custom':
        try:
            theme = themes.game_themes[parser.args.theme]
        except:
            theme = themes.game_themes['minimal']
    else:
<<<<<<< HEAD
        # copy custom-theme.xml if it doesn't exist
        if not os.path.exists(CUSTOM_FILE):
            if not os.path.exists(CUSTOM_THEME_PATH):
                sys.exit('Error: custom-theme.xml missing from home and /usr/share/make-snake')
            #ensure_dir(app_dir)
            shutil.copyfile(CUSTOM_THEME_PATH, CUSTOM_FILE)
        # Load the customn theme
        load_theme()
=======
        # copy custom_theme if it doesn't exist
        if not os.path.exists(custom_file):
            src_file = '/usr/share/make-snake/custom_theme'
            if not os.path.exists(src_file):
                sys.exit('Error: custom_theme missing from home and /usr/share')
            ensure_dir(app_dir)
            shutil.copyfile(src_file, custom_file)
        load_custom_theme()
>>>>>>> parent of b280dda... Added print argument to list themes, also added ability to play a saved theme @alexaverill

    colors_map = get_colors_map()


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


def load_custom_theme():
    global theme

    try:
<<<<<<< HEAD
        name = parser.args.theme
        if not name.endswith('.xml'):
            name += '.xml'

        theme_file = app_dir + '/' + name
        if not os.path.exists(theme_file):
            webload_file = app_dir + '/webload/' + name
            if os.path.exists(webload_file):
                theme_file = webload_file

        with open(theme_file):
=======
        with open(custom_file):
>>>>>>> parent of b280dda... Added print argument to list themes, also added ability to play a saved theme @alexaverill
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
<<<<<<< HEAD


def update_theme_list():
    # User themes
    themes = os.listdir(app_dir)
    # Remove everything that is not xml
    for t in themes:
        if not t.endswith('.xml'):
            themes.remove(t)
    # Internet themes
    shared_themes_dir = app_dir + '/webload'
    if os.path.isdir(shared_themes_dir):
        # remove folder name from list if it has been added
        try:
            themes.remove("webload")
        except:
            pass
        shared_themes = os.listdir(shared_themes_dir)
        # Add xmls in webload
        for s in shared_themes:
            if s.endswith('.xml'):
                themes.append(s)
    return themes
=======
>>>>>>> parent of b280dda... Added print argument to list themes, also added ability to play a saved theme @alexaverill
