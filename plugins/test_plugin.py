#!/bin/env python3


def to_be_imported(arg1,arg2,arg3):
    '''
    this is documntary comment
    :param arg1: integer
    :param arg2: string

    :return: list
    '''
    return [*args]

def web_add(int1=0,int2=1):
	'''
    this is documntary comment
    :param int1: intiger
    :param int2: intiger

    :return: intiger
    '''


	return int1+int2

def web_mult(int1=0,int2=1):
	return int1*int2

def _no_to_be_imported():
    #you shoudn't see this
    return "err"