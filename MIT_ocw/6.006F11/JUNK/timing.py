#!/usr/bin/env python

# timing.py
# Author: Ronald L. Rivest
# Date last modified: November 26, 2016
# Modified: Zafar Takhirov

# Routines to help in timing the execution of
# various code fragments or routines, and to
# infer a good formula for the resulting runtimes.

import math
import scipy.linalg
import string
import sys
import timeit

# Parameter generation routines

def lg(x):
    return math.log(x)/math.log(2.0)

def sqrt(x):
    return math.sqrt(x)

def make_param_list(spec_string,growth_factor):
    """
    Generate a list of dictionaries
    given maximum and minimum values for each range.
    Each min and max value is a *string* that can be evaluted;
    each string may depend on earlier variable values
    Values increment by factor of growth_factor from min to max
    Example:
       make_param_list("1<=n<=1000")
       make_param_list("1<=n<=1000;1<=m<=1000;min(n,m)<=k<=max(n,m)")
    """
    var_list = []
    spec_list = string.split(spec_string,";")
    D = {}
    D['lg']=lg
    D['sqrt'] = sqrt
    D_list = [D]
    for spec in spec_list:
        spec_parts = string.split(spec,"<=")
        assert len(spec_parts)==3
        lower_spec = spec_parts[0]
        var_name = spec_parts[1]
        assert len(var_name)==1
        var_list.append(var_name)
        upper_spec = spec_parts[2]
        new_D_list = []
        for D in D_list:
            new_D = D.copy()
            val = eval(lower_spec,D)
            while val<=eval(upper_spec,D):
                new_D[var_name] = val
                new_D_list.append(new_D.copy())
                val *= growth_factor
        D_list = new_D_list
    # for D in D_list: print D
    return (var_list,D_list)

# sample("1<=n<=1000;1<=m<=1000;min(n,m)<=k<=max(n,m)",2)

def fit(var_list,param_list,run_times,f_list):
    """
    Return matrix A needed for least-squares fit.
    Given:
        list of variable names
        list of sample dicts for various parameter sets
        list of corresponding run times
        list of functions to be considered for fit
            these are *strings*, e.g. "n","n**2","min(n,m)",etc.
    prints:
        coefficients for each function in f_list
    """
    print "var_list",var_list
    print "Function list:",f_list
    print "run times:",
    for i in range(len(param_list)):
        print
        for v in var_list:
            print v,"= %6s"%param_list[i][v],
        print ": %8f"%run_times[i],"microseconds",
        # print "  n = %(n)6s"%param_list[i],run_times[i],"microseconds"
    print
    rows = len(run_times)
    cols = len(f_list)
    A = [ [0 for j in range(cols)] for i in range(rows) ]
    for i in range(rows):
        D = param_list[i]
        for j in range(cols):
            A[i][j] = float(eval(f_list[j],D))
    b = run_times
    # print "A:"
    # print A
    # print "b:"
    # print b

    # (x,resids,rank,s) = scipy.linalg.lstsq(A,b)
    (x,resids,rank,s) = fit2(A,b)

    print "Coefficients as interpolated from data:"
    for j in range(cols):
        sign = ''
        if x[j]>0 and j>0:
            sign="+"
        elif x[j]>0:
            sign = " "
        print "%s%g*%s"%(sign,x[j],f_list[j])

    print "(measuring time in microseconds)"
    print "Sum of squares of residuals:",resids
    print "RMS error = %0.2g percent"%(math.sqrt(resids/len(A))*100.0)
    # print "Rank:",rank
    # print "SVD:",s
    sys.stdout.flush()

import scipy.optimize

def fit2(A,b):
    """ Relative error minimizer """
    def f(x):
        assert len(x) == len(A[0])
        resids = []
        for i in range(len(A)):
            sum = 0.0
            for j in range(len(A[0])):
                sum += A[i][j]*x[j]
            relative_error = (sum-b[i])/b[i]
            resids.append(relative_error)
        return resids
    ans = scipy.optimize.leastsq(f,[0.0]*len(A[0]))
    # print "ans:",ans
    if len(A[0])==1:
        x = [ans[0]]
    else:
        x = ans[0]
    resids = sum([r*r for r in f(x)])
    return (x,resids,0,0)

def test_misc():
    print
    print "Test Misc-1 -- running time should be n+2*m+7+3*n*lg(n)+17*n*m"
    spec_string = "1<=n<=100000;1<=m<=100000"
    growth_factor = 10
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list,param_list = make_param_list(spec_string,growth_factor)
    run_times = [ eval("n+2*m+7+3*n*lg(n)+17*n*m",D) for D in param_list ]
    f_list = ("(n*m)","n**2","n*lg(n)","n","m","1")
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Misc-2: pass"
    spec_string = "10000<=n<=1000000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("pass")
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

def test_number():

    print
    print "Test Number-1 -- time to compute int('1'*n)"
    spec_string = "1000<=n<=10000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n","1")
    f_list = ("n**2",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("string.atoi(x)","import string;x='1'*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-2 -- time to compute repr(2**n)"
    spec_string = "1000<=n<=10000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n","1")
    f_list = ("n**2",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("repr(x)","x=2**%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-3 -- time to convert (2**n) to hex"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n","1")
    f_list = ("n",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("'%x'%x","x=2**%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-4 -- time to add 2**n to itself"
    spec_string = "1000<=n<=1000000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list,param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n*lg(n)","n","1")
    f_list = ("n",)
    run_times = []
    trials = 10000
    for D in param_list:
        t = timeit.Timer("x+x","x=2**%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)


    print
    print "Test Number-5 -- time to multiply (2**n/3) by itself"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list,param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n*lg(n)","n","1")
    f_list = ("n**1.585",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("x*x","x=(2**%(n)s)/3"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-6 -- time to divide (2**(2n) by (2**n))"
    spec_string = "1000<=n<=50000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list,param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n*lg(n)","n","1")
    f_list = ("n**2",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("w/x","w=(2**(2*%(n)s));x=(2**(%(n)s))"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-7 -- time to compute remainder of (2**(2n) by (2**n))"
    spec_string = "1000<=n<=50000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list,param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n*lg(n)","n","1")
    f_list = ("n**2",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("w%x","w=(2**(2*%(n)s));x=(2**(%(n)s))"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-8 -- time to compute pow(x,y,z)"
    spec_string = "1000<=n<=5000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list,param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n*lg(n)","n","1")
    f_list = ("n**3",)
    run_times = []
    trials = 10
    for D in param_list:
        t = timeit.Timer("pow(x,y,z)","z=(2**%(n)s)+3;x=y=(2**%(n)s)+1"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-9 -- time to compute 2**n"
    spec_string = "1000<=n<=1000000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list,param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n**2","n*lg(n)","n","1")
    f_list = ("1",)
    run_times = []
    trials = 10000
    for D in param_list:
        t = timeit.Timer("2**%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

def test_string():
    print
    print "Test String-1: extract a byte from a string"
    spec_string = "1000<=n<=1000000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("s[500]","s='0'*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test String-2: concatenate two string of length n"
    spec_string = "1000<=n<=500000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("s+t","s=t='0'*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test String-3: extract a string of length n/2"
    spec_string = "1000<=n<=500000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("s[0:%(n)s/2]"%D,"s='0'*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test String-4: translate a string of length n"
    spec_string = "1000<=n<=500000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("string.translate(s,T)"%D,
                         "s='0'*%(n)s;import string;T=string.maketrans('1','2')"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

def test_list():
    print
    print "Test List-1: create an empty list"
    spec_string = "1<=n<=10"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("x = list()")
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-2: list (array) lookup"
    spec_string = "10000<=n<=1000000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("x=L[5]","L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-3: appending to a list of length n"
    spec_string = "10000<=n<=1000000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1")
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("L.append(0)","L=[0]*%(n)s;L.append(0)"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-4: Pop"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1",)
    run_times = []
    trials = 200
    for D in param_list:
        t = timeit.Timer("L.pop()","L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-5: concatenating two lists of length n"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 2000
    for D in param_list:
        t = timeit.Timer("L+L","L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-6: extracting a slice of length n/2"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 2000
    for D in param_list:
        t = timeit.Timer("L[0:%(n)s/2]"%D,"L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-7: copy"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 2000
    for D in param_list:
        t = timeit.Timer("L[:]","L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-8: assigning a slice of length n/2"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 2000
    for D in param_list:
        t = timeit.Timer("L[0:%(n)s/2]=L[1:1+%(n)s/2]"%D,"L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-9: Delete first"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 200
    for D in param_list:
        t = timeit.Timer("del L[0]","L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-10: Reverse"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 200
    for D in param_list:
        t = timeit.Timer("L.reverse()","L=[0]*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test List-11: Sort"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n*lg(n)",)
    run_times = []
    trials = 200
    for D in param_list:
        t = timeit.Timer("L.sort()","import random;L=[random.random() for i in range(%(n)s)]"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

def test_dict():
    print
    print "Test Dict-1: create an empty dictionary"
    spec_string = "1<=n<=1"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("x = dict()")
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Dict-2: dictionary lookup"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("1",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("x = d[1]",
                         "d = dict([(i,i) for i in range(%(n)s)])"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Dict-3: dictionary copy"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("d.copy()",
                         "d = dict([(i,i) for i in range(%(n)s)])"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Dict-4: dictionary list items"
    spec_string = "1000<=n<=100000"
    growth_factor = 2
    print "Spec_string: ",spec_string, "by factors of", growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    # f_list = ("n","1")
    f_list = ("n*lg(n)",)
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("d.items()",
                         "d = dict([(i,i) for i in range(%(n)s)])"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)

def main():
    test_misc()
    test_number()
    test_string()
    test_list()
    test_dict()

if False:
    import profile
    profile.run("main()")
else:
    main()



