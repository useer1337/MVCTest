class CPlusDModel:
    def __init__(self):
        self.c = 0
        self.d = 0
        self.sum = 0

        self.observers = []

    def set_c(self,c:float) -> None:
        self.c = c
        self._sum = self.c + self.d
        self.notify_observers()

    def set_d(self, d:float):
        self.d = d
        self.sum = self.c + self.d
        self.notify_observers()

    def get_sum(self):
        return self.sum

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.model_is_changed()



