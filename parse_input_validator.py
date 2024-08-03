def parse_input_validator(func):
    def inner(*args, **kwargs):
        if(len(args[0]) == 0):
            return (None, None)
        return func(*args, **kwargs)
    return inner