#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: A.Akdogan
"""

import os
import sys
import inspect

class Path:
    
    @staticmethod
    def get_base_path():
        
        return os.path.abspath(os.path.split(sys.argv[0])[0])
    
    @staticmethod
    def move_back(path):
    
        return os.path.normpath(os.path.dirname(path))
    
    @staticmethod
    def move_forward(path, forward_path):
    
        return os.path.join(path, forward_path)
    
    def get(self, str_path):
        
        base_path = Path.get_base_path()
        route_list = str_path.split(os.sep)
        for i in range(len(route_list)):
            if route_list[i] == "" or route_list[i] == ".":
                continue

            if route_list[i] == "..":
                base_path = Path.move_back(base_path)
            elif route_list[i] == ".":
                pass
            else:
                base_path = Path.move_forward(base_path, route_list[i])
                
        return base_path
    
    
    def importer(self, str_path):
        
        path = self.get(str_path)
        path_list = path.split(os.sep)
        ext_list = path_list[len(path_list) -1].split(".")
        new_path = self.get(str_path +  os.sep + "..")
        sys.path.insert(1, new_path)
        
        if len(ext_list) == 2:
            
            package = __import__(ext_list[0])
            return getattr(package, ext_list[1])
        elif len(ext_list) == 1:
            package = __import__(ext_list[0])

            return package
        else:
            raise Exception("The extension should consist of a maximum of 2 parts.")
            
            
        
        
        

    
    
    
    
    
    
    
    
    
    