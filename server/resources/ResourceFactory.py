from resources.ResourceBase import ResourceBase, ResourceListBase


def ResourceFactory(resource_name):
    class Resource(ResourceBase):
      def __init__(self):
        super().__init__(resource_name)
    new_class = type(resource_name.capitalize(), (Resource,), {})
    return new_class


def ResourceListFactory(resource_name):
    class ResourceList(ResourceListBase):
        def __init__(self):
            super().__init__(resource_name)
    new_class = type(resource_name.capitalize() + "List", (ResourceList,), {})
    return new_class