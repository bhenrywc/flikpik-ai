import random
def get_social_mentions(title:str):
    random.seed(abs(hash(title))%100000)
    return {"X":random.randint(1000,40000),"Reddit":random.randint(500,15000),"Facebook":random.randint(1000,25000),"Instagram":random.randint(2000,55000)}
def get_sentiment_score(title:str):
    random.seed(abs(hash(title))%100000); return random.randint(72,97)/100
def get_hype_score(title:str):
    m=sum(get_social_mentions(title).values()); s=get_sentiment_score(title)
    return round(((m/130000)*0.6+s*0.4)*100,2)
