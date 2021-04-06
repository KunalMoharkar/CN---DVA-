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
    
    def has_changed(self):

        for mod in self.modified:

            if mod == 1:
                return True

        return False

    def show_details(self):

        print(f"\nRouter Name - {self.name}")
        print(f"Distance Vector - \n")

        len_dv = len(self.dv)

        for i in range(len_dv):

            if self.modified[i] == 0:
                mod = " "
            else:
                mod = "*"
            
            print(f"{self.dv[i][0]} \t\t {self.dv[i][1]} \t\t {mod}")
