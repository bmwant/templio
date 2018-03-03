import os
from functools import partial

import aiohttp
from aiohttp import web


def run():
    app = web.Application()

    uprint = partial(print, flush=True)
    port = int(os.environ.get('PORT', 8080))

    uprint('Running aiohttp {}'.format(aiohttp.__version__))
    web.run_app(app, print=uprint, port=port)


if __name__ == '__main__':
    run()
