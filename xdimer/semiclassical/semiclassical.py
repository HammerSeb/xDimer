

'''Excited State Energy of State n'''
def D(n,E0,De):
    return De+(2*n+1)*E0
'''Displacement as function of Emission Energy from excited state n'''
DE = lambda n,De: D(n,E_0,De)

def q(E,n,R,qe,De):
    return np.sqrt((DE(n,De)-E)/R)-qe

def Excimer_Emission_0(E,a,R,qe,De):
    return np.nan_to_num(0.5*np.sqrt(a/(m.pi*R*(DE(0,De)-E)))*np.exp(-a*q(E,0,R,qe,De)**2))

def Excimer_Emission_1(E,a,R,qe,De):
    return np.nan_to_num(np.sqrt(a**3/(m.pi*R*(DE(1,De)-E)))*q(E,1,R,qe,De)**2*np.exp(-a*q(E,1,R,qe,De)**2))

def Excimer_Emission_2(E,a,R,qe,De):
    return np.nan_to_num((1/4)*np.sqrt(a/(m.pi*R*(DE(2,De)-E)))*(2*a*q(E,2,R,qe,De)**2-1)**2*np.exp(-a*q(E,2,R,qe,De)**2))

def Excimer_Emission_3(E,a,R,qe,De):
    return np.nan_to_num((1/6)*np.sqrt(a/(m.pi*R*(DE(3,De)-E)))*(2*a*q(E,3,R,qe,De)**2-3)**2*a*q(E,3,R,qe,De)**2*np.exp(-a*q(E,3,R,qe,De)**2))

def Excimer_Emission_4(E,a,R,qe,De):
    return np.nan_to_num((1/48)*np.sqrt(a/(m.pi*R*(DE(4,De)-E)))*(4*a**2*q(E,4,R,qe,De)**4-12*a*q(E,4,R,qe,De)**2+3)**2*np.exp(-a*q(E,4,R,qe,De)**2))

def Excimer_Emission_5(E,a,R,qe,De):
    return np.nan_to_num((1/120)*np.sqrt(a/(m.pi*R*(DE(5,De)-E)))*a*q(E,5,R,qe,De)**2*((2*a*q(E,5,R,qe,De)**2-5)**2-10)**2*np.exp(-a*q(E,5,R,qe,De)**2))

def Excimer_Fit_Funtion(E,R,a,qe,De,P,T):
    return P[str(T)][1,0]*Excimer_Emission_0(E,a,R,qe,De)+P[str(T)][1,1]*Excimer_Emission_1(E,a,R,qe,De)+P[str(T)][1,2]*Excimer_Emission_2(E,a,R,qe,De)+P[str(T)][1,3]*Excimer_Emission_3(E,a,R,qe,De)+P[str(T)][1,4]*Excimer_Emission_4(E,a,R,qe,De)+P[str(T)][1,5]*Excimer_Emission_5(E,a,R,qe,De)