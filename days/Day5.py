# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay
from langdetect import detect
from spellchecker import SpellChecker

class Day5(GenericDay):
    def __init__(self, message):
        GenericDay.__init__(self, "Day5 solution")
        self.cypher = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ."
        self.message = message

    def getSolution(self):
        result = ""
        check = SpellChecker()
        max_known = 0
        
        for offset in range(len(self.cypher)):
            decrypted_message = ""
            for i in range(len(self.message)):
                pos = self.cypher.find(self.message[i])
                decrypted_message += self.cypher[(pos + offset)%len(self.cypher)]
            lang = detect(decrypted_message)
            
            if lang == "en":
                #There is a decent chance this is English
                words = decrypted_message.split(" ")
                known = check.known(words)
                
                # The sentence with most known English words is _probably_ our solution
                if len(known) > max_known:
                    max_known = len(known)
                    result = decrypted_message
        
        return result
    
