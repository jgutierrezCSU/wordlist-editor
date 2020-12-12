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
group.add_argument("--firstupper",action="store_true") #no argument needed w/ action="store_true"  
group.add_argument("--allupper",action="store_true" )  
group.add_argument("--firstlower",action="store_true")
group.add_argument("--alllower",action="store_true")  

#bind the arguments
args = parser.parse_args();
argument_length=len(sys.argv)

print(argument_length)

#single argument
if argument_length == 3 or argument_length == 4:
    if args.end:  # append at end
        appnd_nums(args.filename,args.end)
    elif args.beg:  # append at beg 
        appnd_nums(args.filename,args.beg)
    elif args.firstupper:
        print("firstupper")
    elif args.allupper:
        print("allupper")
    elif args.firstlower:
        print("firstlower")
    elif args.alllower:
        print("alllower")
# two arguments
elif argument_length == 5 or argument_length == 6:
    if args.end and args.beg: # append at beg and end
        if args.end != args.beg:
            print("--> Num of digits need to be the same")
            exit()
        appnd_nums(args.filename,args.beg)
    elif args.end and args.firstupper:
        print("end firstupper")
    elif args.end and args.allupper:
        print("end allupper")
    elif args.end and args.firstlower:
        print("end firstlower")
    elif args.end and args.alllower:
        print("end alllower")

    
    elif args.beg and args.firstupper:
        print("beg firstupper")
    elif args.beg and args.allupper:
        print("beg allupper")
    elif args.beg and args.firstlower:
        print("beg firstlower")
    elif args.beg and args.alllower:
        print("beg alllower")

elif argument_length == 7 or argument_length == 8:
    print("here")



