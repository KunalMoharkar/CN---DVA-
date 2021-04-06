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
