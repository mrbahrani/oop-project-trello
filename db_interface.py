from abstract_class import AbstractItem
from model_map import db_map

class QueryHandler:
    def create_object(self, obj=AbstractItem()):
        parmeter_list = dict()
        model_class = obj.model_class
        for field in db_map[model_class]:
            parmeter_list[field] = getattr(obj, field)

        return model_class.create().where(**parmeter_list).get()

    def retrieve_object(self, obj=AbstractItem):
        parmeter_list = dict()
        model_class = obj.model_class
        for field in db_map[model_class]:
            if getattr(obj, field) is not None:
                parmeter_list[field] = getattr(obj, field)

        return model_class.select().where(**parmeter_list).get()

    def delete_object(self, model_class, obj):
        pass

    def update_object(self, model_class, obj):
        pass