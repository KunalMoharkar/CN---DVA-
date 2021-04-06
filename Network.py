class Network():

    def __init__(self, routers):
        self.routers = routers

    def initialize_modified(self):
        for router in self.routers:
            len_dv = len(router.dv)
            router.modified = [0]*len_dv


    def get_router_by_name(self,name):
        for r in self.routers:
            if r.name == name:
                return r

    def show_details(self):

        for r in self.routers:
            r.show_details()
