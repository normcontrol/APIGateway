from fastapi import APIRouter, Response
from starlette.requests import Request
from common import router
from src.gateway.schemas import Document

normcontrol_router = APIRouter(prefix="", tags=["normcontrol"])


@router(
    method=normcontrol_router.post,
    path="/clasify",
)
async def clasify_element(
    request: Request,
    response: Response,
    user: str,
    document: Document,
):
    pass

@router(
    method=normcontrol_router.get,
    path="/parse_document",
)
async def parse_document(
    request: Request,
    response: Response,
    user: str,
    document_type:str,
    path: str,
):
    pass

@router(
    method=normcontrol_router.get,
    path="/parse_paragraph",
)
async def parse_paragraph(
    request: Request,
    response: Response,
    user: str,
    document_type:str,
    path: str,
):
    pass

@router(
    method=normcontrol_router.get,
    path="/parse_images",
)
async def parse_images(
    request: Request,
    response: Response,
    user: str,
    document_type:str,
    path: str,
):
    pass

@router(
    method=normcontrol_router.get,
    path="/parse_table",
)
async def parse_table(
    request: Request,
    response: Response,
    user: str,
    document_type:str,
    path: str,
):
    pass

@router(
    method=normcontrol_router.get,
    path="/parse_list",
)
async def parse_list(
    request: Request,
    response: Response,
    user: str,
    document_type:str,
    path: str,
):
    pass

@router(
    method=normcontrol_router.post,
    path="/thematics",
)
async def nlp_thematics(
    request: Request,
    response: Response,
    user: str,
    document: Document,
):
    pass

@router(
    method=normcontrol_router.post,
    path="/structure",
)
async def nlp_structure(
    request: Request,
    response: Response,
    user: str,
    document: Document,
):
    pass

@router(
    method=normcontrol_router.post,
    path="/check",
)
async def check_elements(
    request: Request,
    response: Response,
    gost: int,
    user: str,
    document: Document,
):
    pass

@router(
    method=normcontrol_router.post,
    path="/normocontroler",
)
async def normocontroler(
    request: Request,
    response: Response,
    user: str,
    document_type:str,
    path: str,
    gost: str,
):
    pass
