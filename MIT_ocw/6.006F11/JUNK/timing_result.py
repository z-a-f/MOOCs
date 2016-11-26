
Test Misc-1 -- running time should be n+2*m+7+3*n*lg(n)+17*n*m
Spec_string:  1<=n<=100000;1<=m<=100000 by factors of 10
var_list ['n', 'm']
Function list: ('(n*m)', 'n**2', 'n*lg(n)', 'n', 'm', '1')
run times:
n =      1 m =      1 : 27.000000 microseconds
n =      1 m =     10 : 198.000000 microseconds
n =      1 m =    100 : 1908.000000 microseconds
n =      1 m =   1000 : 19008.000000 microseconds
n =      1 m =  10000 : 190008.000000 microseconds
n =      1 m = 100000 : 1900008.000000 microseconds
n =     10 m =      1 : 288.657843 microseconds
n =     10 m =     10 : 1836.657843 microseconds
n =     10 m =    100 : 17316.657843 microseconds
n =     10 m =   1000 : 172116.657843 microseconds
n =     10 m =  10000 : 1720116.657843 microseconds
n =     10 m = 100000 : 17200116.657843 microseconds
n =    100 m =      1 : 3802.156857 microseconds
n =    100 m =     10 : 19120.156857 microseconds
n =    100 m =    100 : 172300.156857 microseconds
n =    100 m =   1000 : 1704100.156857 microseconds
n =    100 m =  10000 : 17022100.156857 microseconds
n =    100 m = 100000 : 170202100.156857 microseconds
n =   1000 m =      1 : 47906.352854 microseconds
n =   1000 m =     10 : 200924.352854 microseconds
n =   1000 m =    100 : 1731104.352854 microseconds
n =   1000 m =   1000 : 17032904.352854 microseconds
n =   1000 m =  10000 : 170050904.352854 microseconds
n =   1000 m = 100000 : 1700230904.352854 microseconds
n =  10000 m =      1 : 578640.371386 microseconds
n =  10000 m =     10 : 2108658.371386 microseconds
n =  10000 m =    100 : 17408838.371386 microseconds
n =  10000 m =   1000 : 170410638.371386 microseconds
n =  10000 m =  10000 : 1700428638.371387 microseconds
n =  10000 m = 100000 : 17000608638.371386 microseconds
n = 100000 m =      1 : 6782901.142331 microseconds
n = 100000 m =     10 : 22082919.142331 microseconds
n = 100000 m =    100 : 175083099.142331 microseconds
n = 100000 m =   1000 : 1705084899.142331 microseconds
n = 100000 m =  10000 : 17005102899.142330 microseconds
n = 100000 m = 100000 : 170005282899.142334 microseconds
Coefficients as interpolated from data:
 17*(n*m)
-4.36072e-12*n**2
+3*n*lg(n)
+1*n
+2*m
+7*1
(measuring time in microseconds)
Sum of squares of residuals: 2.01144964616e-17
RMS error = 7.5e-08 percent

Test Misc-2: pass
Spec_string:  10000<=n<=1000000 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =  10000 : 0.017881 microseconds
n =  20000 : 0.018120 microseconds
n =  40000 : 0.017881 microseconds
n =  80000 : 0.017881 microseconds
n = 160000 : 0.016928 microseconds
n = 320000 : 0.016928 microseconds
n = 640000 : 0.016928 microseconds
Coefficients as interpolated from data:
 0.0174771*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.00595162]
RMS error = 2.9 percent

Test Number-1 -- time to compute int('1'*n)
Spec_string:  1000<=n<=10000 by factors of 2
var_list ['n']
Function list: ('n**2',)
run times:
n =   1000 : 9.906054 microseconds
n =   2000 : 38.905144 microseconds
n =   4000 : 135.867119 microseconds
n =   8000 : 491.173029 microseconds
Coefficients as interpolated from data:
 8.75504e-06*n**2
(measuring time in microseconds)
Sum of squares of residuals: [ 0.0442544]
RMS error = 11 percent

Test Number-2 -- time to compute repr(2**n)
Spec_string:  1000<=n<=10000 by factors of 2
var_list ['n']
Function list: ('n**2',)
run times:
n =   1000 : 1.737118 microseconds
n =   2000 : 6.268978 microseconds
n =   4000 : 26.947021 microseconds
n =   8000 : 101.315975 microseconds
Coefficients as interpolated from data:
 1.63693e-06*n**2
(measuring time in microseconds)
Sum of squares of residuals: [ 0.00724865]
RMS error = 4.3 percent

Test Number-3 -- time to convert (2**n) to hex
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 1.657009 microseconds
n =   2000 : 2.419949 microseconds
n =   4000 : 3.684998 microseconds
n =   8000 : 7.407904 microseconds
n =  16000 : 16.460180 microseconds
n =  32000 : 32.402039 microseconds
n =  64000 : 60.925007 microseconds
Coefficients as interpolated from data:
 0.00102962*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.1988802]
RMS error = 17 percent

Test Number-4 -- time to add 2**n to itself
Spec_string:  1000<=n<=1000000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 0.133395 microseconds
n =   2000 : 0.179505 microseconds
n =   4000 : 0.407195 microseconds
n =   8000 : 0.430298 microseconds
n =  16000 : 1.009297 microseconds
n =  32000 : 1.469898 microseconds
n =  64000 : 3.017306 microseconds
n = 128000 : 5.249906 microseconds
n = 256000 : 10.835195 microseconds
n = 512000 : 21.350622 microseconds
Coefficients as interpolated from data:
 5.04558e-05*n
(measuring time in microseconds)
Sum of squares of residuals: [ 1.02514192]
RMS error = 32 percent

Test Number-5 -- time to multiply (2**n/3) by itself
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n**1.585',)
run times:
n =   1000 : 0.880957 microseconds
n =   2000 : 3.242016 microseconds
n =   4000 : 11.452198 microseconds
n =   8000 : 40.688038 microseconds
n =  16000 : 128.160954 microseconds
n =  32000 : 386.171103 microseconds
n =  64000 : 1168.503046 microseconds
Coefficients as interpolated from data:
 2.1616e-05*n**1.585
(measuring time in microseconds)
Sum of squares of residuals: [ 0.36557272]
RMS error = 23 percent

Test Number-6 -- time to divide (2**(2n) by (2**n))
Spec_string:  1000<=n<=50000 by factors of 2
var_list ['n']
Function list: ('n**2',)
run times:
n =   1000 : 4.415989 microseconds
n =   2000 : 10.829926 microseconds
n =   4000 : 34.636021 microseconds
n =   8000 : 128.781080 microseconds
n =  16000 : 489.277840 microseconds
n =  32000 : 2420.450926 microseconds
Coefficients as interpolated from data:
 2.27196e-06*n**2
(measuring time in microseconds)
Sum of squares of residuals: [ 0.31784524]
RMS error = 23 percent

Test Number-7 -- time to compute remainder of (2**(2n) by (2**n))
Spec_string:  1000<=n<=50000 by factors of 2
var_list ['n']
Function list: ('n**2',)
run times:
n =   1000 : 3.303051 microseconds
n =   2000 : 10.090113 microseconds
n =   4000 : 35.374165 microseconds
n =   8000 : 124.793053 microseconds
n =  16000 : 488.425016 microseconds
n =  32000 : 1968.058825 microseconds
Coefficients as interpolated from data:
 2.14668e-06*n**2
(measuring time in microseconds)
Sum of squares of residuals: [ 0.18512943]
RMS error = 18 percent

Test Number-8 -- time to compute pow(x,y,z)
Spec_string:  1000<=n<=5000 by factors of 2
var_list ['n']
Function list: ('n**3',)
run times:
n =   1000 : 3808.712959 microseconds
n =   2000 : 30437.207222 microseconds
n =   4000 : 193213.796616 microseconds
Coefficients as interpolated from data:
 3.45781e-06*n**3
(measuring time in microseconds)
Sum of squares of residuals: [ 0.03792907]
RMS error = 11 percent

Test Number-9 -- time to compute 2**n
Spec_string:  1000<=n<=1000000 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =   1000 : 0.031686 microseconds
n =   2000 : 0.031495 microseconds
n =   4000 : 0.031495 microseconds
n =   8000 : 0.036097 microseconds
n =  16000 : 0.031996 microseconds
n =  32000 : 0.030589 microseconds
n =  64000 : 0.030303 microseconds
n = 128000 : 0.029898 microseconds
n = 256000 : 0.034118 microseconds
n = 512000 : 0.026512 microseconds
Coefficients as interpolated from data:
 0.0310415*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.06092236]
RMS error = 7.8 percent

Test String-1: extract a byte from a string
Spec_string:  1000<=n<=1000000 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =   1000 : 0.052214 microseconds
n =   2000 : 0.051022 microseconds
n =   4000 : 0.049829 microseconds
n =   8000 : 0.051022 microseconds
n =  16000 : 0.063181 microseconds
n =  32000 : 0.049114 microseconds
n =  64000 : 0.048876 microseconds
n = 128000 : 0.090122 microseconds
n = 256000 : 0.088930 microseconds
n = 512000 : 0.058889 microseconds
Coefficients as interpolated from data:
 0.0551965*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.37429307]
RMS error = 19 percent

Test String-2: concatenate two string of length n
Spec_string:  1000<=n<=500000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 0.181913 microseconds
n =   2000 : 0.192881 microseconds
n =   4000 : 0.235081 microseconds
n =   8000 : 0.395060 microseconds
n =  16000 : 1.300097 microseconds
n =  32000 : 3.175974 microseconds
n =  64000 : 7.061958 microseconds
n = 128000 : 15.566111 microseconds
n = 256000 : 40.767193 microseconds
Coefficients as interpolated from data:
 7.74369e-05*n
(measuring time in microseconds)
Sum of squares of residuals: [ 1.32760226]
RMS error = 38 percent

Test String-3: extract a string of length n/2
Spec_string:  1000<=n<=500000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 0.533104 microseconds
n =   2000 : 0.354052 microseconds
n =   4000 : 0.378847 microseconds
n =   8000 : 0.432968 microseconds
n =  16000 : 0.519037 microseconds
n =  32000 : 0.829935 microseconds
n =  64000 : 2.048969 microseconds
n = 128000 : 3.884077 microseconds
n = 256000 : 8.933067 microseconds
Coefficients as interpolated from data:
 3.42262e-05*n
(measuring time in microseconds)
Sum of squares of residuals: [ 2.19611454]
RMS error = 49 percent

Test String-4: translate a string of length n
Spec_string:  1000<=n<=500000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 1.800060 microseconds
n =   2000 : 3.195047 microseconds
n =   4000 : 5.419970 microseconds
n =   8000 : 9.455919 microseconds
n =  16000 : 17.393112 microseconds
n =  32000 : 38.320065 microseconds
n =  64000 : 72.876215 microseconds
n = 128000 : 160.392046 microseconds
n = 256000 : 306.792974 microseconds
Coefficients as interpolated from data:
 0.00125359*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.18574468]
RMS error = 14 percent

Test List-1: create an empty list
Spec_string:  1<=n<=10 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =      1 : 0.125885 microseconds
n =      2 : 0.125885 microseconds
n =      4 : 0.124931 microseconds
n =      8 : 0.124931 microseconds
Coefficients as interpolated from data:
 0.125405*1
(measuring time in microseconds)
Sum of squares of residuals: [  5.78285384e-05]
RMS error = 0.38 percent

Test List-2: list (array) lookup
Spec_string:  10000<=n<=1000000 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =  10000 : 0.041008 microseconds
n =  20000 : 0.041008 microseconds
n =  40000 : 0.041008 microseconds
n =  80000 : 0.042915 microseconds
n = 160000 : 0.041008 microseconds
n = 320000 : 0.042915 microseconds
n = 640000 : 0.048876 microseconds
Coefficients as interpolated from data:
 0.0423896*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.02245192]
RMS error = 5.7 percent

Test List-3: appending to a list of length n
Spec_string:  10000<=n<=1000000 by factors of 2
var_list ['n']
Function list: 1
run times:
n =  10000 : 0.091076 microseconds
n =  20000 : 0.098944 microseconds
n =  40000 : 0.087023 microseconds
n =  80000 : 0.087976 microseconds
n = 160000 : 0.087023 microseconds
n = 320000 : 0.090122 microseconds
n = 640000 : 0.092983 microseconds
Coefficients as interpolated from data:
 0.0904161*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.01206343]
RMS error = 4.2 percent

Test List-4: Pop
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =   1000 : 0.164509 microseconds
n =   2000 : 0.159740 microseconds
n =   4000 : 0.159740 microseconds
n =   8000 : 0.144243 microseconds
n =  16000 : 0.144243 microseconds
n =  32000 : 0.145435 microseconds
n =  64000 : 0.145435 microseconds
Coefficients as interpolated from data:
 0.151028*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.0200471]
RMS error = 5.4 percent

Test List-5: concatenating two lists of length n
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 11.231065 microseconds
n =   2000 : 22.508502 microseconds
n =   4000 : 43.404460 microseconds
n =   8000 : 87.681532 microseconds
n =  16000 : 186.626554 microseconds
n =  32000 : 353.031993 microseconds
n =  64000 : 754.337072 microseconds
Coefficients as interpolated from data:
 0.0112356*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.00576425]
RMS error = 2.9 percent

Test List-6: extracting a slice of length n/2
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 3.119469 microseconds
n =   2000 : 5.573511 microseconds
n =   4000 : 10.839939 microseconds
n =   8000 : 23.136497 microseconds
n =  16000 : 41.823506 microseconds
n =  32000 : 91.538548 microseconds
n =  64000 : 176.395893 microseconds
Coefficients as interpolated from data:
 0.00280483*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.01837267]
RMS error = 5.1 percent

Test List-7: copy
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 4.850507 microseconds
n =   2000 : 10.324478 microseconds
n =   4000 : 21.898985 microseconds
n =   8000 : 42.344570 microseconds
n =  16000 : 85.627437 microseconds
n =  32000 : 187.596083 microseconds
n =  64000 : 374.768019 microseconds
Coefficients as interpolated from data:
 0.00536474*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.02760799]
RMS error = 6.3 percent

Test List-8: assigning a slice of length n/2
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 4.927516 microseconds
n =   2000 : 10.747552 microseconds
n =   4000 : 21.926522 microseconds
n =   8000 : 44.520497 microseconds
n =  16000 : 80.990553 microseconds
n =  32000 : 162.637472 microseconds
n =  64000 : 353.747964 microseconds
Coefficients as interpolated from data:
 0.00526642*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.01472153]
RMS error = 4.6 percent

Test List-9: Delete first
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 0.200272 microseconds
n =   2000 : 0.324249 microseconds
n =   4000 : 0.704527 microseconds
n =   8000 : 2.593994 microseconds
n =  16000 : 5.164146 microseconds
n =  32000 : 10.889769 microseconds
n =  64000 : 30.000210 microseconds
Coefficients as interpolated from data:
 0.000220322*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.81047994]
RMS error = 34 percent

Test List-10: Reverse
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 0.549555 microseconds
n =   2000 : 0.960827 microseconds
n =   4000 : 1.970530 microseconds
n =   8000 : 4.105568 microseconds
n =  16000 : 8.025169 microseconds
n =  32000 : 15.225410 microseconds
n =  64000 : 46.169758 microseconds
Coefficients as interpolated from data:
 0.000516375*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.10052868]
RMS error = 12 percent

Test List-11: Sort
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n*lg(n)',)
run times:
n =   1000 : 16.225576 microseconds
n =   2000 : 29.054880 microseconds
n =   4000 : 66.775084 microseconds
n =   8000 : 141.814947 microseconds
n =  16000 : 348.435640 microseconds
n =  32000 : 824.389458 microseconds
n =  64000 : 1522.231102 microseconds
Coefficients as interpolated from data:
 0.00147436*n*lg(n)
(measuring time in microseconds)
Sum of squares of residuals: [ 0.05470526]
RMS error = 8.8 percent

Test Dict-1: create an empty dictionary
Spec_string:  1<=n<=1 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =      1 : 0.232935 microseconds
Coefficients as interpolated from data:
 0.232935*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.]
RMS error = 0 percent

Test Dict-2: dictionary lookup
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('1',)
run times:
n =   1000 : 0.090122 microseconds
n =   2000 : 0.061035 microseconds
n =   4000 : 0.060081 microseconds
n =   8000 : 0.107050 microseconds
n =  16000 : 0.068903 microseconds
n =  32000 : 0.067949 microseconds
n =  64000 : 0.070810 microseconds
Coefficients as interpolated from data:
 0.0700309*1
(measuring time in microseconds)
Sum of squares of residuals: [ 0.21975812]
RMS error = 18 percent

Test Dict-3: dictionary copy
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n',)
run times:
n =   1000 : 22.833109 microseconds
n =   2000 : 56.115866 microseconds
n =   4000 : 100.610018 microseconds
n =   8000 : 223.049164 microseconds
n =  16000 : 409.077883 microseconds
n =  32000 : 1311.012983 microseconds
n =  64000 : 2398.833990 microseconds
Coefficients as interpolated from data:
 0.0275799*n
(measuring time in microseconds)
Sum of squares of residuals: [ 0.23573228]
RMS error = 18 percent

Test Dict-4: dictionary list items
Spec_string:  1000<=n<=100000 by factors of 2
var_list ['n']
Function list: ('n*lg(n)',)
run times:
n =   1000 : 34.163952 microseconds
n =   2000 : 79.009056 microseconds
n =   4000 : 193.569899 microseconds
n =   8000 : 579.087019 microseconds
n =  16000 : 1165.333986 microseconds
n =  32000 : 3336.256981 microseconds
n =  64000 : 7348.698854 microseconds
Coefficients as interpolated from data:
 0.00442675*n*lg(n)
(measuring time in microseconds)
Sum of squares of residuals: [ 0.49260877]
RMS error = 27 percent
