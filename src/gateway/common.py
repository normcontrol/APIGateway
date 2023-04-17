import logging
from datetime import date
from functools import wraps
from typing import Any, Optional
from fastapi import HTTPException, Request, Response
from starlette import status

from rabbit import send_request_to_queue

def router(
    method,
    path: str,
    data_key: Optional[str] = None,
    status_code: Optional[int] = status.HTTP_200_OK,
    response_model: Optional[Any] = None,
):
    """
    Обертка функции эндпоинта, реализующая обращение к RPC-серверу.

    :param method: Вызываемый объект (функция) реализующая тот или
                   иной метод http-запроса.
    :param path: Адрес эндпоинта.
    :param data_key: Имя ключа, в котором передаются данные
                     на эндпоинт.
    :param status_code: Ожидаемый код ответа сервера.
    :param response_model: Модель данных для преобразования ответа.
    """
    app_method = method(
        path, status_code=status_code, response_model=response_model
    )

    def wrapper(endpoint):
        @app_method
        @wraps(endpoint)
        async def decorator(request: Request, response: Response, **kwargs):
            request_method = request.scope["method"].lower()
            data = kwargs.get(data_key)
            data = data.dict() if data else {}
            logging.info(str(date.today()) + ' ' + request.scope["path"])
            response_data, response_status_code = await send_request_to_queue(
                config=request.app.config,
                message={
                    "method": request_method,
                    "path": request.scope["path"],
                    "params": dict(request.query_params),
                    "data": data,
                    "headers": {},
                },
            )
            if response_status_code >= status.HTTP_400_BAD_REQUEST:
                raise HTTPException(
                    status_code=response_status_code, detail=response_data
                )
            response.status_code = response_status_code
            return response_data
    return wrapper