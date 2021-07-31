if __name__ == 'middlewares':
    from loader import dp
    from .throttling import ThrottlingMiddleware

    dp.middleware.setup(ThrottlingMiddleware())
