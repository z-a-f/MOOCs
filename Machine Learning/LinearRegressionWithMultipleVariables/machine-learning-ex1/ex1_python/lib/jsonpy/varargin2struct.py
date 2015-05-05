#!/usr/bin/env python

def varargin2struct(*arg):
	# len = len(arg)
    opt = dict()
    if len(arg) == 0:
    	return opt
    ii = 0
    while (ii < len(arg)):
    	# print opt
    	if isinstance(arg[ii], dict):
    		opt.update(arg[ii])
    	elif isinstance(arg[ii], basestring) & len(arg[ii]) == 2 & ii < len(arg)-1:
    		opt[arg[ii]] = arg[ii+1]
    		ii += 1
    	else:
    		raise Exception('input must be in the form of ...,''name'',value,... pairs or dictionaries.')
    	ii += 1
    return opt

def test():
	a = dict()
	a['c'] = 'CCC'
	print varargin2struct('a', 1, 'b', 'test', a, {'k'})

if __name__ == '__main__':
    test()
