class world_save():
    def __init__(self, name):
        self.name = name
        self.path = 'maps'

        self.dict = {}
        if not os.path.exists("%s/%s" % (self.path, self.name)):
            self.dict = read_dict("%s/%s" % (self.path, self.name))
        else:
            console.print('ERROR READ MAP (%s)' % self.name)
            exit()
