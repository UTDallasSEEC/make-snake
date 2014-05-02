#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import graphics
import theme
import gameloop
import game
import parser
import stage
import sys
import os

import gamestate as gs
from kano.utils import is_gui


def exit():
    graphics.exit()
    gs.save_state()

def run():
    try:
        # Init the game
        parser.init()
        #list themes if -c
        if parser.options.custom:
            #pull app_dir from theme file
            themeList = os.listdir( theme.app_dir )
            print '\t' + "Themes (python snake -t [THEME NAME] to use a theme):"
            for themes in themeList:
                print '\t\t' + themes
            return 
        stage.init()
        graphics.init()
        theme.init()
        game.reset()
        gs.load_state()
   
        # Start the game
        gameloop.start()

    except KeyboardInterrupt:
        exit()

if not is_gui():
    sys.exit("make-snake requires an X session")

run()
