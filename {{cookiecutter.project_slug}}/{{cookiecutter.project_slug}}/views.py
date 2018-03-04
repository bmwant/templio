from aiohttp import web
from aiohttp import hdrs

import config
from utils import log


async def index(request):
    # Content-Type: text/html;
    headers = {
        hdrs.CONTENT_TYPE: 'text/html',
    }
    response = web.FileResponse('index.html', headers=headers)
    return response
