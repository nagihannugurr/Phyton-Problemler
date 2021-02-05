import math
def pythagoreanTrio(n):
    for a in range (n):
        for b in range (1,a):
            c= math.sqrt((a**2)+(b**2))
            if c%1==0:
                if a+b+c==1000:
                    print("Trio's number 1 item is: ",a,"\nTrio's number 2 item is: ",b,"\nTrio's number 3 item is: ",int(c))
                    print("The result of a*b*c: ",int(a*b*c))
pythagoreanTrio(1000)
