import aiohttp_jinja2
from aiohttp import web
from aiohttp import hdrs


import config
from .utils import logger


@aiohttp_jinja2.template('index.html')
async def index(request):
    logger.info('Accessing index page')
