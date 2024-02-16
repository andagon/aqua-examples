from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_paginated_result_of_api_login_incident import ApiPaginatedResultOfApiLoginIncident
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    start_at: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 50,
    filter_: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/System/License/Incidents".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["filter"] = filter_

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiPaginatedResultOfApiLoginIncident.from_dict(response.json())

        return response_200
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
    Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 50,
    filter_: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]
]:
    """Get login incidents

     Get a list with all the login incidents.
    The results are ordered descending from the .

    Args:
        start_at (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 50.
        filter_ (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        start_at=start_at,
        max_results=max_results,
        filter_=filter_,
        order_by=order_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_at: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 50,
    filter_: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]
]:
    """Get login incidents

     Get a list with all the login incidents.
    The results are ordered descending from the .

    Args:
        start_at (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 50.
        filter_ (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        start_at=start_at,
        max_results=max_results,
        filter_=filter_,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 50,
    filter_: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]
]:
    """Get login incidents

     Get a list with all the login incidents.
    The results are ordered descending from the .

    Args:
        start_at (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 50.
        filter_ (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        start_at=start_at,
        max_results=max_results,
        filter_=filter_,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 50,
    filter_: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]
]:
    """Get login incidents

     Get a list with all the login incidents.
    The results are ordered descending from the .

    Args:
        start_at (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 50.
        filter_ (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiPaginatedResultOfApiLoginIncident, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_at=start_at,
            max_results=max_results,
            filter_=filter_,
            order_by=order_by,
        )
    ).parsed
