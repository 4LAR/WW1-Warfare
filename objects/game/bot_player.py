class bot_player():
    def __init__(self):
        self.time = time.perf_counter() + 10

    def update_(self):
        if self.time <= time.perf_counter():
            get_obj_display('units').add_unit(random.randint(0, 4), flip=1)
            self.time = time.perf_counter() + random.uniform(15, 30)
