def solution(ineq, eq, n, m):

    # if (ineq+eq) == "<=":
    #     return int(n <= m)
    # elif (ineq+eq) == "<!":
    #     return int(n < m)
    # elif (ineq+eq) == ">=":
    #     return int(n >= m)
    # else:
    #     return int(n > m)
    
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
    
    # if eq == '!':
    #     eq = ''
    # return int(eval(f'{n} {ineq}{eq} {m}'))