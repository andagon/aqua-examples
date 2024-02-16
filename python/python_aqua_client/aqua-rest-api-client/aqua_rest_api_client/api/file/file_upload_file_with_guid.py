from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/File/{guid}".format(client.base_url, guid=guid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
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
) -> Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]:
    """Upload file with GUID

     Upload a file. This endpoint is used when the URL for a specific upload
    is created up front.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        guid=guid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]:
    """Upload file with GUID

     Upload a file. This endpoint is used when the URL for a specific upload
    is created up front.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        guid=guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]:
    """Upload file with GUID

     Upload a file. This endpoint is used when the URL for a specific upload
    is created up front.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        guid=guid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]:
    """Upload file with GUID

     Upload a file. This endpoint is used when the URL for a specific upload
    is created up front.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            guid=guid,
            client=client,
        )
    ).parsed
