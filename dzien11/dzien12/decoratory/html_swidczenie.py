def bold(f):
    def wrapper(arg):
        return f'<b>{f(arg)}</b>'
    return wrapper


def italik(f):
    return lambda arg: f'<i>{f(arg)},</i>'

@italik
@bold
def foo(arg):
    return f"To est {arg}"

foo("Ala")
print(foo("Ola"))