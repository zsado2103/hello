#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  robot01.py
import rg
# 192.168.3.10:8000
class Robot:

    def czy_wejscie(self, poz):
        print(rg.loc_types(poz))
        if 'spawn' in rg.loc_types(poz):
            return True
        return False

    def czy_wrog(self, game, poz):
        if game.robots.get(poz) and \
           game.robots[poz].player_id != self.player_id:
               return True
        return False

    def znajdz_wrogow_obok(self, game, wrogowie, bezpieczne):
        for poz in rg.locs_around(self.location, filter_out=('invalid', 'obstacle')):
            if game.robots.get(poz) and \
               game.robots[poz].player_id != self.player_id:
                   wrogowie.append(poz)
            elif not czy_wejscie(poz):
                bezpieczne.append(poz)

    def act(self, game):
        dzialanie = ['guard']
        wrogowie = []
        bezpieczne = []
        
        self.znajdz_wrogow_obok(game, wrogowie, bezpieczne)
        
        if self.czy_wejscie(self.location):
            dzialanie = ['move', rg.toward(self.location, rg.CENTER_POINT)]

        # ~if self.location != rg.CENTER_POINT:
            # ~dzialanie = ['move', rg.toward(self.location, rg.CENTER_POINT)]

        if len(wrogowie) == 1 and self.hp > 10:
            dzialanie = ['attack', wrogowie[0]]

        return dzialanie
        
