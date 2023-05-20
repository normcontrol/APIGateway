from fastapi import APIRouter, Response
from starlette.requests import Request
from starlette.responses import RedirectResponse

from common import router
from src.gateway.schemas import Document, DocumentData, AllData

clasify_router = APIRouter(prefix="/clasifier", tags=["clasifier"])
parser_router = APIRouter(prefix="/parser", tags=["parser"])
check_router = APIRouter(prefix="/check", tags=["check"])
normcontrol_router = APIRouter(prefix="", tags=["normcontrol"])
@router(
    method=clasify_router.post,
    path="/clasify",
    data_key='document'
)
async def clasify_element(
        request: Request,
        response: Response,
        document: Document,
):
    pass


@router(
    method=parser_router.post,
    path="/parse_document",
    data_key='document_data'
)
async def parse_document(
        request: Request,
        response: Response,
        document_data: DocumentData
):
    pass


@router(
    method=parser_router.get,
    path="/parse_paragraph",
    data_key='document_data'
)
async def parse_paragraph(
        request: Request,
        document_data: DocumentData
):
    pass


@router(
    method=parser_router.post,
    path="/parse_images",
    data_key='document_data'
)
async def parse_images(
        request: Request,
        document_data: DocumentData
):
    pass


@router(
    method=parser_router.post,
    path="/parse_table",
    data_key='document_data'
)
async def parse_table(
        request: Request,
        document_data: DocumentData
):
    pass


@router(
    method=parser_router.post,
    path="/parse_list",
    data_key='document_data'
)
async def parse_list(
        request: Request,
        document_data: DocumentData
):
    pass


@router(
    method=clasify_router.post,
    path="/thematics",
    data_key='document'
)
async def nlp_thematics(
        request: Request,
        response: Response,
        document: Document,
):
    pass


@router(
    method=clasify_router.post,
    path="/structure",
    data_key='document'
)
async def nlp_structure(
        request: Request,
        response: Response,
        document: Document,
):
    pass


@router(
    method=check_router.post,
    path="/check",
    data_key='all_data'
)
async def check_elements(
        request: Request,
        response: Response,
        all_data: AllData,
):
    pass


@normcontrol_router.post('/normocontroler')
async def normocontroler(
        response: Response,
        request: Request,
        all_data: AllData
):
    import requests
    parse_response = requests.post('http://127.0.0.1:8001/parse_document',
                             json={'document_type': all_data.document_type, 'path': all_data.path})
    clasify_response = requests.post('http://127.0.0.1:8002/clasify',
                             json=parse_response.json())
    json_text = {'gost_id': {'gost_id': all_data.gost}, 'origin_document': {'document_id': all_data.document_id}, 'document': clasify_response.json()}
    check_response = requests.post('http://127.0.0.1:8003/check',
                             json= json_text)
    return check_response.json()
