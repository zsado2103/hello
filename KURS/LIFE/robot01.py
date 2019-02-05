#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  robot01.py
import rg

class Robot:
    
    def act(self, game):
        # print(self.location)
        # print(rg.CENTER_POINT)
        x, y = self.location
        loc2 = (x-1, y)
        print(self.location, rg.loc_types(self.location))
        print(loc2, rg.loc_types(self.location))
        print(rg.locs_around(self.location, filter_out=('invalid', 'obstacle')))
        
        #print(game)
        if self.location != rg.CENTER_POINT:
            return['move', rg.toward(self.location, rg.CENTER_POINT)]
        
        return['guard']
        
