from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_image_info import ApiImageInfo
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/Image/{id}/{checksum}".format(client.base_url, id=id, checksum=checksum)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiImageInfo.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiNotFoundError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ApiUnauthorizedError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiInternalError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ApiBackendNotAvailableError.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
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
) -> Response[
    Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Get image metadata by id and checksum

     Get the metadata for the image with the given *id* and *checksum*. The image content
    must be retrieved separately.

    Args:
        id (int):
        checksum (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        checksum=checksum,
        client=client,
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
) -> Optional[
    Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Get image metadata by id and checksum

     Get the metadata for the image with the given *id* and *checksum*. The image content
    must be retrieved separately.

    Args:
        id (int):
        checksum (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        id=id,
        checksum=checksum,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Get image metadata by id and checksum

     Get the metadata for the image with the given *id* and *checksum*. The image content
    must be retrieved separately.

    Args:
        id (int):
        checksum (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        checksum=checksum,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    checksum: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Get image metadata by id and checksum

     Get the metadata for the image with the given *id* and *checksum*. The image content
    must be retrieved separately.

    Args:
        id (int):
        checksum (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiImageInfo, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            id=id,
            checksum=checksum,
            client=client,
        )
    ).parsed
