import random
PLATFORMS=["Netflix","Prime Video","Max","Hulu","Disney+","Peacock","Paramount+"]
def get_streaming_platforms(title:str):
    random.seed(abs(hash(title))%100000)
    return random.sample(PLATFORMS, random.randint(1,3))
