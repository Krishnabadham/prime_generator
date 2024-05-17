from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PrimesData
import time

# Create your views here.
# Normal Method 1

def normal_method1(start,end):
    for i in range(start,end+1):
        if i<=1:
            continue
        elif i%2==0 and i!=2:
            continue
        for j in range(3,int(i//2),2):
            if i%j==0:
                break
        else:
            yield i

# Normal method 2

def is_prime_NM2(num):
    if num<=1:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def normal_method2(start,end):
    primes=[]
    for x in range(start,end+1):
        if is_prime_NM2(x):
            primes.append(x)
    return primes

# trail devision Method

def is_prime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    i=5
    while i**2<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True

def trial_division(start,end):
    primes=[]
    for num in range(start,end+1):
        if is_prime(num):
            primes.append(num)
    return primes

# sieve eratosthenes method

def sieve_eratosthenes(start,end):
    primes=[]
    assume=[True]*(end+1) # here we assume all numbers from 0 to end are primes
    assume[0]=False
    assume[1]=False

    for i in range(2,int(end**0.5)+1):
        if assume[i]:
            for y in range(i**2,end+1,i):
                assume[y]=False

    for num in range(max(start,2),end+1):
        if assume[num]:
            primes.append(num)
    return primes

def generate_primes(request):
    start=int(request.GET.get('start'))
    end=int(request.GET.get('end'))
    algorithm=request.GET.get('algorithm')
    start_time=time.time()

    if algorithm=='normal_method1':
        result=normal_method1(start,end)
        primes=list(result)

    elif algorithm=='normal_method2':
        primes=normal_method2(start,end)

    elif algorithm=='trial_division':
        primes=trial_division(start,end)

    elif algorithm=='sieve_eratosthenes':
        primes=sieve_eratosthenes(start,end)

    else:
        return JsonResponse({'error':'Invalid algorithm'},status=400)
    
    end_time=time.time()
    time_elapsed=end_time-start_time
    primes_count=len(primes)

    PrimesData(
        start=start,
        end=end,
        algorithm=algorithm,
        count=primes_count,
        time_elapsed=time_elapsed,
        primes=','.join(map(str, primes))).save()

    return JsonResponse({'primes':primes,'count':primes_count,'time_elapsed':time_elapsed})