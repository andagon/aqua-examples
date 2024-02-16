from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_dashboard_ng import ApiDashboardNG
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    include_widgets: Union[Unset, None, bool] = True,
    include_shares: Union[Unset, None, bool] = False,
    include_data: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/DashboardNG/{dashboardId}".format(client.base_url, dashboardId=dashboard_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["includeWidgets"] = include_widgets

    params["includeShares"] = include_shares

    params["includeData"] = include_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiDashboardNG,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiDashboardNG.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiForbiddenError.from_dict(response.json())

        return response_403
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiDashboardNG,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    include_widgets: Union[Unset, None, bool] = True,
    include_shares: Union[Unset, None, bool] = False,
    include_data: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiDashboardNG,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get dashboard

     Get dashboard with the given *dashboardId*.
    Depending on parameters the actual parts of the dashboard data can be filled or not (null).

    Args:
        dashboard_id (int):
        include_widgets (Union[Unset, None, bool]):  Default: True.
        include_shares (Union[Unset, None, bool]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiDashboardNG, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        client=client,
        include_widgets=include_widgets,
        include_shares=include_shares,
        include_data=include_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    include_widgets: Union[Unset, None, bool] = True,
    include_shares: Union[Unset, None, bool] = False,
    include_data: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiDashboardNG,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get dashboard

     Get dashboard with the given *dashboardId*.
    Depending on parameters the actual parts of the dashboard data can be filled or not (null).

    Args:
        dashboard_id (int):
        include_widgets (Union[Unset, None, bool]):  Default: True.
        include_shares (Union[Unset, None, bool]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiDashboardNG, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        dashboard_id=dashboard_id,
        client=client,
        include_widgets=include_widgets,
        include_shares=include_shares,
        include_data=include_data,
    ).parsed


async def asyncio_detailed(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    include_widgets: Union[Unset, None, bool] = True,
    include_shares: Union[Unset, None, bool] = False,
    include_data: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiDashboardNG,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get dashboard

     Get dashboard with the given *dashboardId*.
    Depending on parameters the actual parts of the dashboard data can be filled or not (null).

    Args:
        dashboard_id (int):
        include_widgets (Union[Unset, None, bool]):  Default: True.
        include_shares (Union[Unset, None, bool]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiDashboardNG, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        client=client,
        include_widgets=include_widgets,
        include_shares=include_shares,
        include_data=include_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    include_widgets: Union[Unset, None, bool] = True,
    include_shares: Union[Unset, None, bool] = False,
    include_data: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiDashboardNG,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get dashboard

     Get dashboard with the given *dashboardId*.
    Depending on parameters the actual parts of the dashboard data can be filled or not (null).

    Args:
        dashboard_id (int):
        include_widgets (Union[Unset, None, bool]):  Default: True.
        include_shares (Union[Unset, None, bool]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiDashboardNG, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            client=client,
            include_widgets=include_widgets,
            include_shares=include_shares,
            include_data=include_data,
        )
    ).parsed
