# This will calculate the value of a call and put for a European style option
# C = [S - PV(d)]*N(d1) - PV(K)*N(d2)
# d1 = (ln(S/K) + t(r - q + (s^2)/2)/(s * sqrt(t))
# d2 = d1 - (s * sqrt(t))

from math import log, sqrt, e
from scipy.stats import norm

print "Black-Scholes calculator for European Options"
print "----------------------------------------------"
S = float(raw_input("Stock Price: "))
K = float(raw_input("Strike Price: "))
sig = float(raw_input("Volatility (%): "))
sig = sig / 100
r = float(raw_input("Risk-free Rate (%): "))
r = r /100
d = float(raw_input("Dividend Yield (%): "))
d = d/100
t = float(raw_input("Time to Expiration: "))
print "----------------------------------------------"

def d1(S, K, sig, r, d, t):
    v1 = log(S/K)
    v2 = ((r - d + (pow(sig, 2) / 2)) * t)
    v3 = (sig * sqrt(t)) 
    return (v1 + v2)/v3
print "d1: " + str(d1(S, K, sig, r, d, t))

def d2(S, K, sig, r, d, t):
    return (d1(S, K, sig, r, d, t) - (sig * sqrt(t)))
print "d2: " + str(d2(S, K, sig, r, d, t))

def call(S, K, sig, r, d, t):
    v1 = pow(e, -d*t)
    v2 = S * norm.cdf(d1(S, K, sig, r, d, t))
    v3 = K * pow(e, -r * t) * norm.cdf(d2(S, K, sig, r, d, t))
    return ((v1 * v2) - v3)

print "Call value: " + str(call(S, K, sig, r, d, t))