class Router():

    def __init__(self, name, dv, neighbours):
        self.name = name
        self.dv = dv
        self.neighbours = neighbours
        self.modified = []

    def update_dv_value(self, dest, val):

        for x in self.dv:

            if x[0] == dest:
                x[1] = val

    def show_details(self):
        print(f"Router Name - {self.name}")

        print(f"Distance Vector - ")

        len_dv = len(self.dv)

        for i in range(len_dv):

            if self.modified[i] == 0:
                mod = "NO"
            else:
                mod = "YES"
            
            print(f"{self.dv[i][0]} ---------- {self.dv[i][1]} ----------- {mod}")
