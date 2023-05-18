from typing import Tuple

from aiohttp import ClientSession

SERVICE_MAP = {
    "clasify": "127.0.0.1:8002",
    "parser": "127.0.0.1:8001",
    "check": "127.0.0.1:8003",
}


async def resolve(
        method: str,
        path: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None
) -> Tuple[dict, int]:
    _, service_name, api = path.split("/")
    service_host = SERVICE_MAP[service_name]
    url = f"http://{service_host}/{api}"
    response, status_code = await make_request(
        url, method, params, data, headers
    )
    return response, status_code


async def make_request(
        url: str,
        method: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None
) -> Tuple[dict, int]:

    if not headers:
        headers = {}
    if not data:
        data = {}

    async with ClientSession() as session:
        request = getattr(session, method)
        async with await request(
                url, params=params, json=data, headers=headers
        ) as response:
            response_json = await response.json()
            return response_json, response.status
