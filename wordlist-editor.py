#!/usr/bin/python3.5
import sys
import argparse
import re
import os

def clean_lines(line):
    return re.findall(r'[^"\s]\S*|".+?"', line) #clean spaces


def single_arg(filename, num_length):
     
    text =open(filename)
    
    if args.end:
        if os.path.isfile("e_"+filename): #check if file is there , if true , delete (clear)
            os.remove("e_"+filename)
        newfile = open( "e_"+filename, 'a')
    elif args.beg:
        if os.path.isfile("b_"+filename): #check if file is there , if true , delete (clear)
            os.remove("b_"+filename)
        newfile = open( "b_"+filename, 'a')
    elif args.firstupper:
        if os.path.isfile("fU_"+filename): #check if file is there , if true , delete (clear)
            os.remove("fU_"+filename)
        newfile = open( "fU_"+filename, 'a')
    elif args.allupper:
        if os.path.isfile("aU_"+filename): #check if file is there , if true , delete (clear)
            os.remove("aU_"+filename)
        newfile = open( "aU_"+filename, 'a')
    elif args.alllower:
        if os.path.isfile("aL_"+filename): #check if file is there , if true , delete (clear)
            os.remove("aL_"+filename)
        newfile = open( "aL_"+filename, 'a')
    elif args.firstlower:
        if os.path.isfile("fL_"+filename): #check if file is there , if true , delete (clear)
            os.remove("fL_"+filename)
        newfile = open( "fL_"+filename, 'a')
    
    for line in text:
        words=clean_lines(line) # parse " " & Spaces
        for word in words:
            print(word)
            counter=0

            if args.end:
                while counter != 10**num_length:
                    # concat and append nums to word
                    newfile.write(word + str(counter) + '\n')
                    counter += 1
            elif args.beg:
                while counter != 10**num_length:
                    # concat and append nums to word
                     newfile.write(str(counter) + word + '\n')
                     counter += 1        
            elif args.firstupper:
                newfile.write(word[0].upper() + word[1:]+ '\n')

            elif args.allupper:
                newfile.write(word.upper() + '\n')

            elif args.firstlower:
                newfile.write(word[0].lower() + word[1:]+ '\n')

            elif args.alllower:
                newfile.write(word.lower() + '\n')

    print('saved ...')


def two_arg(filename, num_length):

    text =open(filename)
    if args.end and args.beg:
        if os.path.isfile("eb_"+filename): #check if file is there , if true , delete (clear)
            os.remove("eb_"+filename)
        newfile = open( "eb_"+filename, 'a')

    if args.end and args.firstupper:
        if os.path.isfile("efU_"+filename): #check if file is there , if true , delete (clear)
            os.remove("efU_"+filename)
        newfile = open( "efU_"+filename, 'a')

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
            elif args.end and args.firstupper:
                while counter != 10**num_length:
                    # concat and append nums to word
                    newfile.write(word[0].upper() + word[1:]+ str(counter) + '\n')
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
group.add_argument("--firstupper",action="store_true",help='first letter to upper') #no argument needed w/ action="store_true"  
group.add_argument("--allupper",action="store_true" ,help='all letters to upper')  
group.add_argument("--firstlower",action="store_true",help='first letter to lower')
group.add_argument("--alllower",action="store_true",help='all letter to lower')  

#bind the arguments
args = parser.parse_args();
argument_length=len(sys.argv)

print(argument_length)

#single argument
if argument_length == 3 or argument_length == 4:
    if args.end:  # append at end
        single_arg(args.filename,args.end)
    elif args.beg:  # append at beg 
        single_arg(args.filename,args.beg)
    
    single_arg(args.filename,-1)
    

# two arguments
elif argument_length == 5 or argument_length == 6:
    if args.end and args.beg: # append at beg and end
        if args.end != args.beg:
            print("--> Num of digits need to be the same")
            exit()
        two_arg(args.filename,args.beg)
    elif args.end and args.firstupper:
        two_arg(args.filename,args.end)
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



