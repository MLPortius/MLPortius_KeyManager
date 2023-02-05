# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:04:19 2023

@author: Andriu
"""

#%% IMPORT LIBRARIES

import os
import argparse
from cryptography.fernet import Fernet


#%% SCRIPTS SETUP

parser = argparse.ArgumentParser(prog= 'encoder',
                                 description = 'Encrypts userkeys with a filekey',
                                 epilog = 'Created by Andriu')
    
parser.add_argument('-u','--user',required=True)
parser.add_argument('-v','--verbose',default=1)

args = parser.parse_args()

# ARGUMENTS
user = args.user
verb = int(args.verbose)


#%% SETUP

keyfoler = "filekeys/"
input_folder = "decode/input/"
output_folder = "decode/output/"

names = os.listdir(input_folder)
inpaths = [input_folder+x for x in names] 
outpaths = [output_folder + x.split('.crypt')[0] + ".key" for x in names] 


#%% FUNCTIONS

def load_fk(username, fkf='filekeys/'):
    
    print('\n Loading FILEKEY ...')
    
    path = fkf+username+'.key'
    
    with open(path, 'rb') as filekey:
        key = filekey.read()    
    filekey.close()
    
    print('     ...Done!')
    
    return key


def decode_file(key, infile, outfile):
    
    fernet = Fernet(key)
    
    with open(infile, 'rb') as file:
        encrypted = file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    with open(outfile, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
        

def decode_keys(k, i, o):
    
    print('\n Decoding USERKEYS ...')
    
    for ind in range(len(i)):
        decode_file(key=k, infile=i[ind], outfile=o[ind])
    
    print('     ...Done!')
    
    
#%% APPLY

fk = load_fk(user)
decode_keys(fk, inpaths, outpaths)

