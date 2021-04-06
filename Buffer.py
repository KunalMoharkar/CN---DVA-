class Buffer():

    def __init__(self,router_names):
        self.queue = []

        for router in router_names:

            self.queue.append((router,[]))


    def all_tables_received(self, router):

        for x in self.queue:
            if x[0] == router.name:
                if len(x[1]) == len(router.neighbours):
                    return True
        
        return False

    def insert_buffer(self, router, r):
        for x in self.queue:
            if x[0] == router.name:
                x[1].append((r.name, r.dv))

    

    def show_buffer(self):

        print("------- BUFFER ------ ")

        for x in self.queue:

            print(f"Queue for {x[0]}")
            print(x[1])
