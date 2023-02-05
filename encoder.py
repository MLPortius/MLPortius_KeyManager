# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:52:32 2023

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
    
parser.add_argument('-m','--mode',required=True)
parser.add_argument('-u','--user',required=True)
parser.add_argument('-v','--verbose',default=1)

args = parser.parse_args()

# ARGUMENTS
mode = args.mode.lower()
user = args.user
verb = int(args.verbose)


#%% SETUP

keyfoler = "filekeys/"
input_folder = "encode/input/"
output_folder = "encode/output/"


names = os.listdir(input_folder)
inpaths = [input_folder+x for x in names] 
outpaths = [output_folder + x.split('.key')[0] + ".crypt" for x in names] 


#%% FUNCTIONS

def generate_fk(username, kf='filekeys/'):
    
    if os.path.isfile(kf+username+'.key'):
        print('ERROR: Filekey already exists for this user...')
    
    else:
        print('\n Generating FILEKEY ...')
        
        key = Fernet.generate_key()
    
        with open(kf+str(username)+'.key', 'wb') as filekey:
            filekey.write(key)
        filekey.close()
       
        print('     ...Done!')
    

def load_fk(username, fkf='filekeys/'):
    
    print('\n Loading FILEKEY ...')
    
    path = fkf+username+'.key'
    
    with open(path, 'rb') as filekey:
        key = filekey.read()    
    filekey.close()
    
    print('     ...Done!')
    
    return key


def encode_file(key, infile, outfile):
    
    fernet = Fernet(key)
    
    with open(infile, 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)
    
    with open(outfile, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def encode_keys(k, i, o):
    
    print('\n Encoding USERKEYS ...')
    
    for ind in range(len(i)):
        encode_file(key=k, infile=i[ind], outfile=o[ind])
    
    print('     ...Done!')
    
    
#%% APPLY

if mode in ['generate','gen','g','get']:
    generate_fk(user)

elif mode in ['encode','e','encrpyt']:
    fk = load_fk(user)
    encode_keys(fk, inpaths, outpaths)

else:
    print('ERROR: Invalid mode... Try generate or encode!')