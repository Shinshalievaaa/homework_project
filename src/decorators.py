def log(filename = ''):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                text_output = f'{func.__name__} ok'
                if filename != '':
                    with open(filename, 'w') as f:
                        f.write(text_output)
                else:
                    print(text_output)
                return result
            except Exception as e:
                text_output = f'{func.__name__} error: {e}. Inputs: {args}'
                if filename != '':
                    with open(filename, 'w') as f:
                        f.write(text_output)
                else:
                    print(text_output)

        return inner

    return wrapper




# @log(filename="mylog.txt")