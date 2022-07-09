#WITH_CERTAINTY

#anonymous function

def f(x):
    print(3*x+1)
print(f(2))

#OH SHIT FUNCTIONS LIKE IN ALGEBRA

g = lambda x: 3*x +1
print(g(2)) #see, it's a different way to write functions. Just in one line. 

#Multiple parameters

full_name = lambda fn, ln: fn.strip().title()