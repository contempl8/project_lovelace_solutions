def exponential_growth(x0, k, dt, N):
    ret=[x0]
    for i in range(1,N+1): ret.append(ret[i-1]+k*ret[i-1]*dt)
    return ret

print(exponential_growth(5,1,0.6,3))
print(exponential_growth(1,2.5,0.1,5))