from flask_restful import Resource
from resources.ResourceBase import ResourceBase, ResourceListBase


def ResourceFactory(resource_name):
    class Resource(ResourceBase):
      def __init__(self):
        super().__init__(resource_name)
    return Resource


def ResourceListFactory(resource_name):
    class ResourceList(ResourceListBase):
        def __init__(self):
            super().__init__(resource_name)
    return ResourceList