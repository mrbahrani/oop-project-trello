from abstract_class import AbstractItem


class QueryHandler:
    def create_object(self, obj=AbstractItem()):
        obj.model_class.Create()

    def retrieve_object(self, model_class, obj):
        pass

    def delete_object(self, model_class, obj):
        pass

    def update_object(self, model_class, obj):
        pass