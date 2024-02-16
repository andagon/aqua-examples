from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_long_operation_info_base import ApiLongOperationInfoBase
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/System/LongOperation/{guid}".format(client.base_url, guid=guid)

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
    Union[
        ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiLongOperationInfoBase.from_dict(response.json())

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
    Union[
        ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError
    ]
]:
    """Get long operation information

     Get information (including status) of a long operation identified by given guid.
                The actual data returned from this call depends on operation type - please refer
                to documentation of the method that starts the operation for information what kind of
                information is returned in ApiLongOperationInfo.
                The information returned here might sometimes be heavyweight (e.g. include list of
    failures).
                Please consider using GET LongOperation/{guid}/Status if you are only interested
                in the current status of the operation.
                Please also consider using SignalR to receive an event when long operation finishes.
                Warning! Server keeps information about finished long operations only for certain time
    (few hours or until server is recycled).
                After that the information is not available any more.


    Args:
        guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError]]
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
    guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError
    ]
]:
    """Get long operation information

     Get information (including status) of a long operation identified by given guid.
                The actual data returned from this call depends on operation type - please refer
                to documentation of the method that starts the operation for information what kind of
                information is returned in ApiLongOperationInfo.
                The information returned here might sometimes be heavyweight (e.g. include list of
    failures).
                Please consider using GET LongOperation/{guid}/Status if you are only interested
                in the current status of the operation.
                Please also consider using SignalR to receive an event when long operation finishes.
                Warning! Server keeps information about finished long operations only for certain time
    (few hours or until server is recycled).
                After that the information is not available any more.


    Args:
        guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        guid=guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError
    ]
]:
    """Get long operation information

     Get information (including status) of a long operation identified by given guid.
                The actual data returned from this call depends on operation type - please refer
                to documentation of the method that starts the operation for information what kind of
                information is returned in ApiLongOperationInfo.
                The information returned here might sometimes be heavyweight (e.g. include list of
    failures).
                Please consider using GET LongOperation/{guid}/Status if you are only interested
                in the current status of the operation.
                Please also consider using SignalR to receive an event when long operation finishes.
                Warning! Server keeps information about finished long operations only for certain time
    (few hours or until server is recycled).
                After that the information is not available any more.


    Args:
        guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        guid=guid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: Optional[str],
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError
    ]
]:
    """Get long operation information

     Get information (including status) of a long operation identified by given guid.
                The actual data returned from this call depends on operation type - please refer
                to documentation of the method that starts the operation for information what kind of
                information is returned in ApiLongOperationInfo.
                The information returned here might sometimes be heavyweight (e.g. include list of
    failures).
                Please consider using GET LongOperation/{guid}/Status if you are only interested
                in the current status of the operation.
                Please also consider using SignalR to receive an event when long operation finishes.
                Warning! Server keeps information about finished long operations only for certain time
    (few hours or until server is recycled).
                After that the information is not available any more.


    Args:
        guid (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiLongOperationInfoBase, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            guid=guid,
            client=client,
        )
    ).parsed
