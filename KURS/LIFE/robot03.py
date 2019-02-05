#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  robot01.py
import rg
# 192.168.3.10:8000
class Robot:
    
    def act(self, game):
        wrogowie = []
        for poz in rg.locs_around(self.location, filter_out('invalid', 'obstacle')):
            if game.robots.get(poz) and \
               game.robots[poz].player_id != self.player_id:
                   wrogowie.append(poz)
                    
        if self.location != rg.CENTER_POINT:
            return['move', rg.toward(self.location, rg.CENTER_POINT)]
        
        return['guard']
        
