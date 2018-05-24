#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@AUTHOR: Thierry FOSSO KENNE
"""

import sys

data = sys.stdin

#nice print of type tuple3 : expl  (standard,4,[12,14,19])
def print_result(output_array) :
    for value in output_array :
        if value :
            print('{0}\t{1}\t{2}'.format(value[0],value[1],','.join(set(value[2]))))

last_viewmode = ""
last_output = ""
final_output = []

for line in data:
    words = line.split()
    if len(words) > 2 : # check valid line
        splitted_tuile = words[2].split("/")
        if len(splitted_tuile) > 8 : # check valid tuile
            current_viewmode = splitted_tuile[4]
            zoom_level = splitted_tuile[6]
            if(current_viewmode != last_viewmode) :
                final_output.append(last_output)
                current_output = (current_viewmode,1,[zoom_level])
                last_viewmode = current_viewmode
            else :
                current_output = (current_viewmode,last_output[1] + 1, last_output[2] + [zoom_level] )
            last_output = current_output
            
final_output.append(last_output)

    
print_result(final_output)