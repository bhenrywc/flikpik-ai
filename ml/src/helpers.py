import random
def streaming(title):
    random.seed(abs(hash(title))%100000)
    p=['Netflix','Prime Video','Max','Hulu','Disney+','Peacock']
    import random as r
    return r.sample(p,r.randint(1,3))
def buzz(title):
    random.seed(abs(hash(title))%100000)
    return {'X':random.randint(1000,50000),'Reddit':random.randint(500,12000),'Instagram':random.randint(2000,55000)}
