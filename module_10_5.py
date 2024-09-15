import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    obj_dir = dir(obj)

    attributes = [attr for attr in obj_dir if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in obj_dir if callable(getattr(obj, method)) and not method.startswith('__')]

    module = getattr(obj, '__module__', 'Модуль не найден')


    if inspect.isclass(obj):
        obj_type_info = "Это класс"
    elif inspect.ismodule(obj):
        obj_type_info = "Это модуль"
    elif inspect.isfunction(obj):
        obj_type_info = "Это функция"
    elif inspect.ismethod(obj):
        obj_type_info = "Это метод"
    else:
        obj_type_info = "Это объект экземпляра класса"


    introspection_data = {
        'type': obj_type,
        'module': module,
        'attributes': attributes,
        'methods': methods,
        'object_info': obj_type_info
    }

    return introspection_data


number_info = introspection_info(42)
print(number_info)

class_info = introspection_info(int)
print(class_info)


def example_func():
    pass


func_info = introspection_info(example_func)
print(func_info)
