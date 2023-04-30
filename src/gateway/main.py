from fastapi import FastAPI
from router import normcontrol_router
from bestconfig import Config
__config = Config('settings.ini').to_dict()

app = FastAPI(
    title= "Normcontrol GateWay"
)
app.config = __config
app.include_router(normcontrol_router)
