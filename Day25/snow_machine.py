start = 20151125
mul = 252533
mod = 33554393

row = 2981
col = 3075

# Number of the code. Count starts from 0.
n_code = (row*(row + 2*col - 3) + (col-1)*(col-2))/2 + col - 1
n_code = int(n_code)

code = (start*pow(mul, n_code, mod)) % mod

print('The code Santa needs is %i.' %code)
