from litestar import Request, Response
from litestar.status_codes import HTTP_404_NOT_FOUND


def not_found_handler(_: Request, exc: ValueError) -> Response:
    return Response(
        content={'error': f'{exc}'},
        status_code=HTTP_404_NOT_FOUND,
    )
