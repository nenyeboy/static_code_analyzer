# sample8.py
#Deep Nesting

def chaos():
    """Function with cursed nesting"""
    if True:
        for i in range(1):
            while i == 0:
                if i < 1:
                    print("Too deep!")

chaos()
