#!/bin/env python3

#will be imported into api
def to_be_imported(arg1:str="",arg2:int=0,arg3:list=[]):
    '''
    this is documntary comment
    :param arg1: integer
    :param arg2: string

    :return: list
    '''
    return {}

def web_add(int1:int=0,int2:int=1):
	'''
    simple
    :param int1: intiger
    :param int2: intiger

    :return: intiger
    '''


	return int1+int2+1

def web_mult(int1:int=0,int2:int=1):
	return int1*int2


#will not be imported into api because it starts with '_'
def _no_to_be_imported():
    #you shoudn't see this
    return "err"
