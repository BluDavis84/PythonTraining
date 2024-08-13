#interface = ["int0/1", "int0/2", "int0/3", "int0/4", "int0/5"]
# router = ["R1", "R2", "R3", "R4", "R5", "R6"]

# for routers in router:
#     print(f"ssh lavance.davis@{routers}\n enable\n config t ")
#     for interfaces in interface:
#         print(f"{interfaces}\n desc this is {interfaces}")


# for interfaces in interface:
#     if interfaces.endswith("5"):
#         continue
#     print(interfaces)

# mun = 4

# while mun < 20:
#     print(f"{mun} is right")
#     if mun == 14:
#         break
#     mun += 1


#routing = "ospf"

#if routing in ["ospf", "bgp"]:
    #print("we can route that mess")
#else:
    #print("you that we're can't route that mean")




#l= lambda p1, p2: p1 + p2
#print(l(3,5))





my_list = [1,2,3,6,5,6,6,9,10,11]

def number(my_lists):
    new_lists= []
    for i in my_lists:
        if i == 6:
         new_lists.append(i)

    print(new_lists)

      
   
number(my_list)






