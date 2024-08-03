def command_check_decorator(
        index_error_message = None,
        value_error_message = None,
        key_error_message = None,
        ): 
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except IndexError as e:
                return index_error_message if index_error_message != None else e
            except ValueError as e:
                return value_error_message if value_error_message != None else e
            except KeyError as e:
                return key_error_message if key_error_message != None else e
            except Exception as e:
                return e
        return wrapper
    return decorator