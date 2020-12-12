#!/usr/bin/python3.5
import sys
import argparse
import re
import os

def clean_lines(line):
    return re.findall(r'[^"\s]\S*|".+?"', line) #clean spaces


def appnd_nums(filename, num_length):
     
    text =open(filename)
    if args.end and args.beg:
        if os.path.isfile("eb_"+filename): #check if file is there , if true , delete (clear)
            os.remove("eb_"+filename)
        newfile = open( "eb_"+filename, 'a')
    elif args.end:
        if os.path.isfile("e_"+filename): #check if file is there , if true , delete (clear)
            os.remove("e_"+filename)
        newfile = open( "e_"+filename, 'a')
    elif args.beg:
        if os.path.isfile("b_"+filename): #check if file is there , if true , delete (clear)
            os.remove("b_"+filename)
        newfile = open( "b_"+filename, 'a')
    
    for line in text:
        words=clean_lines(line) # parse " " & Spaces
        for word in words:
            print(word)
            counter=0
            if args.end and args.beg:
                while counter != 10**num_length:
                    # concat and append nums to word
                     newfile.write(str(counter) + word + str(counter)+'\n')
                     counter += 1
            elif args.end:
                while counter != 10**num_length:
                    # concat and append nums to word
                    newfile.write(word + str(counter) + '\n')
                    counter += 1
            elif args.beg:
                while counter != 10**num_length:
                    # concat and append nums to word
                     newfile.write(str(counter) + word + '\n')
                     counter += 1
            

    print('saved ...')

    

#check that filename was given
if len(sys.argv) == 1:
    print("Needs file name or path as argument")

    

#for argparser
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("filename",help='File to edit') #required argument
parser.add_argument("--end",type =int,help='adds digits (0-9) at end of each word.Pass in Num of digits' ) 
parser.add_argument("--beg",type =int ,help='adds digits (0-9) at beginning of each word.Pass in Num of digits') 

#exclusive
group.add_argument("--firstcap",type =int )
group.add_argument("--allcap",type =int )  

#bind the arguments
args = parser.parse_args();


if args.end and args.beg: # append at beg and end
    if args.end != args.beg:
        print("--> Num of digits need to be the same")
        exit()
    appnd_nums(args.filename,args.beg)
elif args.end:  # append at end
    appnd_nums(args.filename,args.end)
elif args.beg:  # append at beg 
    appnd_nums(args.filename,args.beg)

