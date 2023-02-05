# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:56:58 2023

@author: Andriu
"""

#%% SCRIPT SETUP

import argparse

parser = argparse.ArgumentParser(prog= 'Keygen',
                                 description = 'Create users and passwords',
                                 epilog = 'Created by Andriu')

parser.add_argument('-n','--name',default="newkey")
parser.add_argument('-u','--user',default='0-0-0-0-0')
parser.add_argument('-p','--password',default='0-0-0-0-0')
parser.add_argument('-s','--seed',default=None)

parser.add_argument('-v','--verbose',default=1)

parser.add_argument('-H','--HELP',default=0)


args = parser.parse_args()


# ARGUMENTS

name = args.name

user = [int(x) for x in args.user.split("-")]
password = [int(x) for x in args.password.split("-")]

if args.seed == None:
    rseed = args.seed
else:
    rseed = int(args.seed)

v = int(args.verbose)

h = int(args.HELP)


#%% CLASS DEFINITION

class keygen:
    
    def __init__(self):
        
        import pandas
        self.pd = pandas
        
        self.lowers = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.uppers = [x.upper() for x in self.lowers]
        self.numbers = [0,1,2,3,4,5,6,7,8,9]
        self.symbols = ['#','%','$','&',';','.',',']
        
        self.user = None
        self.password = None 
        self.user_seed = None
        self.pw_seed = None
        self.user_weights = None
        self.pw_weights = None
        
        
    def get_user(self,size=10,lowers=1,uppers=1,numbers=0,symbols=0,seed=None,verbose=1):
        
        if verbose == 1:
            print('\nGenerating USERNAME ...')
        
        codes = self.lowers*lowers + self.uppers*uppers + self.numbers*numbers + self.symbols*symbols
        serie = self.pd.Series(codes)
        serie = serie.sample(frac=1,replace=False,random_state=seed)
        _list = list(serie.sample(n=size,replace=True,random_state=seed))
        
        output = ''
        for l in _list:
            output = output+str(l)
        
        self.user = output
        
        self.user_seed = str(seed)
        self.user_weights = str(size)+'-'+str(lowers)+'-'+str(uppers)+'-'+str(numbers)+'-'+str(symbols)
        
        if verbose == 1:
            print('     ...Done!')
        
    def get_password(self,size=24,lowers=1,uppers=1,numbers=1,symbols=1,seed=None,verbose=1):
        
        if verbose == 1:
            print('\nGenerating PASSWORD ...')
            
        codes = self.lowers*lowers + self.uppers*uppers + self.numbers*numbers + self.symbols*symbols 
        serie = self.pd.Series(codes)
        serie = serie.sample(frac=1,replace=False,random_state=seed)
        _list = list(serie.sample(n=size,replace=True,random_state=seed))
        
        output = ''
        for l in _list:
            output = output+str(l)
            
        self.password = output
        
        self.pw_seed = str(seed)
        self.pw_weights = str(size)+'-'+str(lowers)+'-'+str(uppers)+'-'+str(numbers)+'-'+str(symbols)

        if verbose == 1:
            print('     ...Done!')    
        
    def save_keys(self,folder='',title='newkey',ext='.key',verbose=1):
        
        if verbose == 1:
            print('\nSaving KEYS ...')
        
        if folder == '':    
            path = title+ext
        
        elif folder[-1]=='/':
            path = folder+title+ext
        
        else:
            path = folder+'/'+title+ext
            
        sep = ' | '
        with open(path,'w') as f:
            f.writelines('PURPOUSE'+sep+title)
            f.writelines('\n\n')
            f.writelines('USER'+sep+'w: '+self.user_weights+sep+'s: '+self.user_seed)
            f.writelines('\n')
            f.writelines(self.user)
            f.writelines('\n\n')
            f.writelines('PASSWORD'+sep+'w: '+self.pw_weights+sep+'s: '+self.pw_seed)
            f.writelines('\n')
            f.writelines(self.password)
        
        if verbose == 1:
            print('     ...Done!')

    
def HELP():

    print('\nArray shape is a string of 5 numbers')
    print('     [Size-Lowers-Uppers-Numbers-Symbols]')
    print('\nUse -u [array] for setup the generation of username...')
    print('\nUse -p [array] for setup the generation of password...')
    print('\nUse -s [int] for setup the generation random seed...')
    print('\nUse -v [1,0] for define verbosity level...')
    
    
#%% USE KEYGEN

if h == 1:
    HELP()

else:
    kg = keygen()
    kg.get_user(user[0],user[1],user[2],user[3],user[4],seed=rseed,verbose=v)
    kg.get_password(password[0],password[1],password[2],password[3],password[4],seed=rseed,verbose=v) 
    kg.save_keys(title=name)
