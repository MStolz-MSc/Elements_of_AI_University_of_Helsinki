"""
Permutation of integers using different methods.
Example: A ship with different destination ports. Which route has the
         lowest emissions? 
"""

print("Looping through each element, creating every combination and print \
only unique combinations that begin with port PAN\n")  

def method1():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
    listA = [0,1,2,3,4] # ports/port numbers
    port1 = 0 # no loop here, all routes begin with PAN
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    if all(item in route for item in listA) is True:
                    # do not modify the print statement
                        print(' '.join([portnames[i] for i in route]))

method1()

print("-------------------------------------------------------------------") 
print("Recursive method\n")   

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    if len(ports) < 1:
        #print(*route)
        print(*[portnames[i] for i in route])
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i+1:])
            

permutations([0], list(range(1, len(portnames))))

print("-------------------------------------------------------------------") 
print("Using permutation package 'itertools'\n")          

import itertools
 
values = portnames[1:]
values = range(1,len(portnames))
per = itertools.permutations(values)
 
for val in per:
    print(0,*val)
 

print("-------------------------------------------------------------------") 
print("Creating all routes and calculating its emissions by using the recursive method. \
Finding the route with lowest emissions.\n")

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km
D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]   # https://timeforchange.org/co2-emissions-shipping-goods
     
co2 = 0.020 # assume 20g per km per metric ton (of pineapples)

smallest = 1000000
bestroute = None

def permutations(route, ports):
    global smallest, bestroute
    if len(ports) < 1:
        #score = co2 * (D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]])
        score = co2 * sum(D[i][j] for i, j in zip(route[:-1], route[1:])) 
        print(' '.join([portnames[i] for i in route]) + " %.1f kg" % score)
        if score < smallest:
            smallest = score
            bestroute = route
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])

def main():
    permutations([0], list(range(1, len(portnames))))
    print("\nThe best route and its emissions:")
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()

    