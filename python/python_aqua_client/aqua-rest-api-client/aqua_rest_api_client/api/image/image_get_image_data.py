from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
    resize: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/Image/{id}/{checksum}/data".format(client.base_url, id=id, checksum=checksum)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["resize"] = resize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[File, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(str, response.text)
        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(str, response.text)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(str, response.text)
        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = cast(str, response.text)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[File, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
    resize: Union[Unset, None, bool] = True,
) -> Response[Union[File, str]]:
    """Get image by id and checksum

     Get content of the image with the given *id* and *checksum*. When possible, the Content-Type
    will be correctly set to match the type of the image.

    Args:
        id (int):
        checksum (Optional[str]):
        resize (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        id=id,
        checksum=checksum,
        client=client,
        resize=resize,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
    resize: Union[Unset, None, bool] = True,
) -> Optional[Union[File, str]]:
    """Get image by id and checksum

     Get content of the image with the given *id* and *checksum*. When possible, the Content-Type
    will be correctly set to match the type of the image.

    Args:
        id (int):
        checksum (Optional[str]):
        resize (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return sync_detailed(
        id=id,
        checksum=checksum,
        client=client,
        resize=resize,
    ).parsed


async def asyncio_detailed(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
    resize: Union[Unset, None, bool] = True,
) -> Response[Union[File, str]]:
    """Get image by id and checksum

     Get content of the image with the given *id* and *checksum*. When possible, the Content-Type
    will be correctly set to match the type of the image.

    Args:
        id (int):
        checksum (Optional[str]):
        resize (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        id=id,
        checksum=checksum,
        client=client,
        resize=resize,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
    resize: Union[Unset, None, bool] = True,
) -> Optional[Union[File, str]]:
    """Get image by id and checksum

     Get content of the image with the given *id* and *checksum*. When possible, the Content-Type
    will be correctly set to match the type of the image.

    Args:
        id (int):
        checksum (Optional[str]):
        resize (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return (
        await asyncio_detailed(
            id=id,
            checksum=checksum,
            client=client,
            resize=resize,
        )
    ).parsed
