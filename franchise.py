class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus 

    def __repr__(self):
        return f"{self.address}"
    
    def available_menus(self, time):
        return [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]