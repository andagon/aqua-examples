from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    image_name: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/Image/Temp/{imageName}".format(client.base_url, imageName=image_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    image_name: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[Union[File, str]]:
    """Get image by imageName

    Args:
        image_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        image_name=image_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    image_name: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[Union[File, str]]:
    """Get image by imageName

    Args:
        image_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return sync_detailed(
        image_name=image_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    image_name: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[Union[File, str]]:
    """Get image by imageName

    Args:
        image_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        image_name=image_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    image_name: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[Union[File, str]]:
    """Get image by imageName

    Args:
        image_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return (
        await asyncio_detailed(
            image_name=image_name,
            client=client,
        )
    ).parsed