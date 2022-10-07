from importlib.metadata import entry_points

class MyClass:
    pass

if __name__ == '__main__':
    entry_points = entry_points(group='entry_point_isinstance')
    plugin_cls = next(iter(entry_points)).load()
    plugin_obj = plugin_cls()

    print(
            f'{MyClass=}',
            f'{plugin_cls=}',
            f'{plugin_obj=}',
            f'{plugin_cls is MyClass=}',
            f'{isinstance(plugin_obj, MyClass)=}',
            sep='\n',
    )
