import math
import string
import timeit
import scipy.optimize

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
    return (var_list,D_list)

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
    print
    rows = len(run_times)
    cols = len(f_list)
    A = [ [0 for j in range(cols)] for i in range(rows) ]
    for i in range(rows):
        D = param_list[i]
        for j in range(cols):
            A[i][j] = float(eval(f_list[j],D))
    b = run_times

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

# def int2str(num):
#     result = ''
#     while num > 0:
#         result += str(num %10);
#         num /= 10
#     return result[::-1]

int2str = """\
def int2str(num):
    result = ''
    while num > 0:
        result += str(num %10);
        num /= 10
    return result[::-1]

"""

def test_number():
    print
    print "Test Number-1 -- time to compute int('1'*n)"
    spec_string = "1000<=n<=10000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    f_list = ("n**2","n","1")
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("string.atoi(x)","import string;x='1'*%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)
    f_list = ("n","1")
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-2 -- time to compute repr(2**n)"
    spec_string = "1000<=n<=10000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    f_list = ("n**2","n","1")
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("repr(x)","x=2**%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)
    f_list = ("n","1")
    fit(var_list,param_list,run_times,f_list)

    print
    print "Test Number-3 -- time to compute int2str(2**n)"
    spec_string = "1000<=n<=10000"
    growth_factor = 2
    print "Spec_string: ",spec_string,"by factors of",growth_factor
    var_list, param_list = make_param_list(spec_string,growth_factor)
    f_list = ("n**2","n","1")
    run_times = []
    trials = 1000
    for D in param_list:
        t = timeit.Timer("int2str(x)", int2str+"x=2**%(n)s"%D)
        run_times.append(t.timeit(trials)*1e6/float(trials))
    fit(var_list,param_list,run_times,f_list)
    f_list = ("n","1")
    fit(var_list,param_list,run_times,f_list)




if __name__ == '__main__':
    test_number()
