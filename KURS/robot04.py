#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  robot01.py
import rg
# 192.168.3.10:8000
class Robot:

    def czy_wejscie(self,poz):
        if 'spawn' rg.loc_types(poz)
        return, True

    def znajdz_wrogow_obok(self, game):
        wrogowie = []
        for poz in rg.locs_around(self.location, filter_out=('invalid', 'obstacle')):
            if game.robots.get(poz) and \
               game.robots[poz].player_id != self.player_id:
                   wrogowie.append(poz)
        return wrogowie

    def act(self, game):
        dzialanie = ['guard']
        
        wrogowie = self.znajdz_wrogow_obok(game)
        print(wrogowie)

        if self.location != rg.CENTER_POINT:
            dzialanie = ['move', rg.toward(self.location, rg.CENTER_POINT)]

        if len(wrogowie) == 1 and self.hp > 10:
            dzialanie = ['attack', wrogowie[0]]
        
        return dzialanie
        

        
