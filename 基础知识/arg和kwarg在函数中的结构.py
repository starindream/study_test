def fn(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)


fn(1, 2, 3, nihao=1)
