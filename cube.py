def cube(x):
    results = x*x*x
    return results

print (int(cube(2)))

def converter_meter(x):
    results=x*1000
    return results


def count_steps():
    a=int(input("How much Km did you walk today?:"))
    a=converter_meter(a)
    b=int(input("What is the size of your average step(in meters)?:"))
    results = a/b
    return results

print("you have made:" +str(count_steps()) +"steps today.")