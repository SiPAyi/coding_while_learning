def nCr(n, r):
    n_factorial = 1
    for i in range(1,n+1):
        n_factorial *= i

    n_minus_r_factorial = 1
    for j in range(1, n-r+1):
        n_minus_r_factorial *= j

    r_factorial = 1
    for k in range(1, r+1):
        r_factorial *= k

    return n_factorial/(n_minus_r_factorial*r_factorial)

def binominal_expansion(n):
    sum = ''
    for r in range(n+1):
        ncr = int(nCr(n, r))
        x_power = int(n - r)
        y_power = int(r)
        r_th_term = str(ncr) + '(x**' + str(x_power) + ')X(y**' + str(y_power) + ') + '
        sum += r_th_term
    return sum

n = int(input('enter x + y whole power : '))
print(binominal_expansion(n))
