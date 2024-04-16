class BodyModel:
    def __init__(self, bodyId, englishName, isPlanet, gravity, discoveredBy, discoveryDate, density):
        self.bodyId = bodyId
        self.englishName = englishName
        self.isPlanet = isPlanet
        self.gravity = gravity
        self.discoveredBy = discoveredBy
        self.discoveryDate = discoveryDate
        self.density = density


    def to_dict(self):
        return self.__dict__
