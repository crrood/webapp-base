from resources.ResourceBase import ResourceBase, ResourceBaseList


resource_name = "entities"


class Entity(ResourceBase):
    def __init__(self):
        super().__init__(resource_name)


class EntityList(ResourceBaseList):
    def __init__(self):
        super().__init__(resource_name)
