#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Sentiment:
    sdict = {}
    def __init__(self, sfile):
    #    print(sfile)
  
        with open(sfile) as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(" ")
                k = parts[2].split("=")[1]
                pnum = self.get_num(parts)
                self.sdict[k] = pnum

    def get_sent_by_string(self, s):
        if s in self.sdict:
            return self.sdict[s]
        else:
            return 0

   #TODO better to use grammer tool to clean string
    def clean_string(self, s):
        to_remove = [",","!","?","'",'"','@'] # <-- just an list of things..you know
        for t in to_remove:
            s = s.replace(t," ")
        return s

    def weight_by_string(self, s):
        clean_string = self.clean_string(s)
        words = clean_string.split(" ")
        s = 0
        maxneg = 0
        for w in words:
            #print(s)
            sent = self.get_sent_by_string(w.lower())
            if sent < 0 :
                maxneg = maxneg + sent
            s = s + sent
        return (s, maxneg)

    def get_num(self, parts):
        pstring = parts[5].split("=")[1].strip()
        pweight = parts[0].split("=")[1]
        psn = 0
        psw = 0

        if pstring == 'negative':
            psn = -1
        elif pstring == 'positive':
            psn =  1
        else:
            psn =  0

        if pweight == 'strongsubj':
            psw = 3 
        elif pweight == 'weaksubj':
            psw =  1
        else:
            psw = 0

        #print("psn, psw"+str(psn)+" "+str(psw))
        return psn*psw



if __name__ == '__main__':
    s = Sentiment("subjclueslen1-HLTEMNLP05.tff")
    import sys
    teststring = sys.argv[1]
    print(s.get_sent_by_string(teststring))
    print(s.weight_by_string(teststring))

