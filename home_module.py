    def GetSquare(self):
        return self.Square

    def AddInhabitant(self, name):
        self.Inhabitants.append(name)

    def RemoveInhabitant(self, name):
        if name in self.Inhabitants:
            self.Inhabitants.remove(name)
