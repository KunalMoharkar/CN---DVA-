import sys
import math
from threading import Thread, Lock

from Buffer import *
from Network import *
from Router import *

PRINT_LOCK = Lock()



    



    




def print_dv(router):

    with PRINT_LOCK:

        print(f"Distance vector for router {router.name}")

        for x in router.dv:
            print(x)


def bellman_ford(router,dv_list):

    #router.name = 'B'
    #router.dv = [['A',8],['B',0],['C',1],['D',10000],['E',1],['F',10000],['G',10000],['H',10000],['I',10000]]

    num_routers = len(router.dv)

    for i in range(num_routers):

        for x in dv_list:

            for r_dv in router.dv:

                if r_dv[0] == x[0]:

                    val = r_dv[1]

            val = val + x[1][i][1]

            print(f"{i} --- {x[0]} --- {val}")

            print(router.dv[i][1])

            if val < (router.dv[i][1]):

                router.dv[i][1] = val
                router.modified[i] = 1

       

def get_tables_from_buffer(buffer, router):

    #print(f"Thread for router {router.name}")

    for x in buffer.queue:
        if x[0] == router.name:

            dv_list = []
            values = len(x[1])
            for i in range(values):
                dv_list.append(x[1].pop(0))
    
    print(f"calling bellamn ford for  {router.name}")
    bellman_ford(router, dv_list)
    

def forward_dv_to_neighbours(network, buffer, router):
    
    #print(f"Thread for router {router.name}")

    for n in router.neighbours:
        r = network.get_router_by_name(n)
        buffer.insert_buffer(router, r)


def initialize_modified(router_list):

    for router in router_list:

        len_dv = len(router.dv)
        router.modified = [0]*len_dv


        

def initialize_dv(network,router_names, edge_list, router_list):

    for router in router_list:

        dv = []

        for r in router_names:
            
            if r == router.name:
                dv.append([r,0])
            else:
                dv.append([r,math.inf])

        router.dv = dv

    for edge in edge_list:

        u = network.get_router_by_name(edge[0])
        v = network.get_router_by_name(edge[1])

        u.update_dv_value(edge[1], int(edge[2]))
        v.update_dv_value(edge[0], int(edge[2]))


def initialize_neighbours(router_names, edge_list):

    router_list = [] 
    

    for router in router_names:

        rt = Router(router,[],[])
        
        for edge in edge_list:

            if edge[0] == router:

                rt.neighbours.append(edge[1])
        
        for edge in edge_list:

            if edge[1] == router:

                rt.neighbours.append(edge[0])

        router_list.append(rt)

    
    return router_list

def scan_input(filename):

    #open the file
    f = open(filename, "r")

    #first line has number of routers
    num_routers = f.readline()
    router_names = f.readline()
    router_names = router_names.split()

    edge_list = []

    #read the  next lines till EOF
    for x in f:

        if x == 'EOF':
            break
        
        x = x.split()

        edge_list.append(x)

    #close file
    f.close()

    return router_names, edge_list


if __name__ == "__main__":


    #TESTING BELLMAN

    #router = Router('B',[],[])

    #dv_list = [('A',[['A',0],['B',8],['C',10000],['D',1],['E',10000],['F',10000],['G',10000],['H',10000],['I',10000]]),('C',[['A',10000],['B',1],['C',0],['D',10000],['E',10000],['F',10000],['G',10000],['H',10000],['I',10000]]),('E',[['A',10000],['B',1],['C',10000],['D',1],['E',0],['F',1],['G',10000],['H',1],['I',10000]])]

    #bellman_ford(router,dv_list)

    #router.show_details()



    #file name passed in cmd args
    filename =  sys.argv[1]

    

    router_names, edge_list = scan_input(filename)
    router_list = initialize_neighbours(router_names,edge_list)
    network = Network(router_list)
    initialize_dv(network, router_names, edge_list, router_list)
    initialize_modified(router_list)
    network.show_details()
    buffer = Buffer(router_names)
    buffer.show_buffer()

    #for router in router_names:

    #    r = network.get_router_by_name(router)
    #    print_th = Thread(target=print_dv,args=(r, ))
    #    print_th.start()

    #for router in router_names:

    #    r = network.get_router_by_name(router)
    #    print_th = Thread(target=forward_dv_to_neighbours,args=(network,buffer,r ))
    #    print_th.daemon = True
    #    print_th.start()

    for router in router_names:
        r = network.get_router_by_name(router)
        forward_dv_to_neighbours(network, buffer, r)

    buffer.show_buffer()

    for router in router_names:
        r = network.get_router_by_name(router)
        get_tables_from_buffer(buffer, r)
    
    
    


    network.show_details()

    initialize_modified(router_list)

    for router in router_names:
        r = network.get_router_by_name(router)
        forward_dv_to_neighbours(network, buffer, r)

    buffer.show_buffer()

    for router in router_names:
        r = network.get_router_by_name(router)
        get_tables_from_buffer(buffer, r)


    network.show_details()




