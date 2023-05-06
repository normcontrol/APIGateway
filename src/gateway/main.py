from fastapi import FastAPI
from router import normcontrol_router, clasify_router, parser_router, check_router
from bestconfig import Config
__config = Config('settings.ini').to_dict()

app = FastAPI(
    title= "Normcontrol GateWay"
)
app.config = __config
app.include_router(normcontrol_router)
app.include_router(clasify_router)
app.include_router(parser_router)
app.include_router(check_router)
