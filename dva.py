import sys
import math


class Network():

    def __init__(self, routers):
        self.routers = routers

    def get_router_by_name(self,name):
        for r in self.routers:
            if r.name == name:
                return r

    def show_details(self):

        for r in self.routers:
            r.show_details()
        
    

class Router():

    def __init__(self, name, dv, neighbours):
        self.name = name
        self.dv = dv
        self.neighbours = neighbours

    def update_dv_value(self, dest, val):

        for x in self.dv:

            if x[0] == dest:

                x[1] = val



    def show_details(self):

        print(f"Name - {self.name} -- dv -- {self.dv} -- neighbours -- {self.neighbours}")



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

        u.update_dv_value(edge[1], edge[2])
        v.update_dv_value(edge[0], edge[2])




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

    #file name passed in cmd args
    filename =  sys.argv[1]

    

    router_names, edge_list = scan_input(filename)
    router_list = initialize_neighbours(router_names,edge_list)
    network = Network(router_list)
    initialize_dv(network, router_names, edge_list, router_list)
    network.show_details()



