from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import File, Response


def _get_kwargs(
    export_file_guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/ExportItems/{exportFileGuid}".format(client.base_url, exportFileGuid=export_file_guid)

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
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiNotFoundError.from_dict(response.json())

        return response_404
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
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    export_file_guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]
]:
    """Download the Result of an Export

    Args:
        export_file_guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    kwargs = _get_kwargs(
        export_file_guid=export_file_guid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    export_file_guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]
]:
    """Download the Result of an Export

    Args:
        export_file_guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    return sync_detailed(
        export_file_guid=export_file_guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    export_file_guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]
]:
    """Download the Result of an Export

    Args:
        export_file_guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    kwargs = _get_kwargs(
        export_file_guid=export_file_guid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    export_file_guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]
]:
    """Download the Result of an Export

    Args:
        export_file_guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    return (
        await asyncio_detailed(
            export_file_guid=export_file_guid,
            client=client,
        )
    ).parsed
