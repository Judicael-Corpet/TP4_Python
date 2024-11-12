def Polynome (p) :
    polynome = [1]
    polynome[0] = "a0"
    for i in range (1,p+1) :
        polynome.append(f"a{i} X^{i}")
    return polynome

def afficher (p) :
    sum_poly = p[-1]
    for i in range (0, len(p)-1) :
        sum_poly += " + " + p[-2-i]  
    return sum_poly

def get_valeur (p, x) :
    for i in range (0,len(p)) :
        x_i = x**i
        p[i] = f"a{i} * {x_i}"
    return p

e = Polynome(7)
print (e)
affiche = afficher(e)
print (affiche)
f_2 = get_valeur(e, 2)
f_x =  afficher(f_2)
print(f_x) 

def deriver (p) :
    del p[0]
    p[0] = "a1"
    for i in range (1, len(p)) :
        p[i] = f"{i+1}*a{i+1} X^{i}"
    return p

dx_dt = afficher(deriver(e))
print(dx_dt) 