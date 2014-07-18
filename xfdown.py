#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urwid
import urwid.raw_display
import getopt,sys,os,subprocess,thread,time
from xfdown_api import XF
    
if '__main__'==__name__:

    s = XF()

    results = s.getlist()
    count = len(results)
    list = [x for x in range(0, count)]
    s.gethttp(list)

    potentialFileCommands = []
    index = 0
    for result in results:
        fileName = result[2]
        ftn5k = s.filecom[index]
        fileHttp = s.filehttp[index]
        aria2Command = "aria2c -c -s10 -x10 -d /Users/GongLi/Downloads   -o '" +fileName+ "' --header 'Cookie: FTN5K=" +ftn5k+ "' " +fileHttp
        print aria2Command
        potentialFileCommands.append(aria2Command)

        index += 1

    while True:
        userInput = input("Enter a number: ")
        if int(userInput) == -1:
            print "End!"
            break
        number = int(userInput)
        os.system(potentialFileCommands[number])
