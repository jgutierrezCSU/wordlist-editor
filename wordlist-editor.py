#!/usr/bin/python3.5
import sys
import argparse
import re
import os

def clean_lines(line):
    return re.findall(r'[^"\s]\S*|".+?"', line)


def epnd_at_end(filename, num_length):
   
  
    text =open(filename)
    #check if file is there , if true , delete (clear)
    if os.path.isfile("e_"+filename):
        os.remove("e_"+filename)

    newfile = open( "e_"+filename, 'a')
    for line in text:
        words=clean_lines(line) # parse " " & Spaces
    
        for word in words:
            print(word)
            counter=0
            while counter != 10**num_length:
                # concat and append nums to word
                newfile.write(word + str(counter) + '\n')
                counter += 1
    print('saved ...')
    

#check that filename was given
if len(sys.argv) == 1:
    print("Needs file name or path as argument")

# if len(sys.argv) == 2:
#     print("")    

#for argparser
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.add_argument("filename",help='File to edit') #required argument



parser.add_argument("--end",type =int ) 
parser.add_argument("--beg",type =int ) 
group.add_argument("--firstcap",type =int )
group.add_argument("--allcap",type =int )  


#bind the arguments
args = parser.parse_args();

epnd_at_end(args.filename,args.end)



