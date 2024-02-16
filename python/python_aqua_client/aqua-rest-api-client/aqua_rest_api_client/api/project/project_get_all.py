from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_project_info import ApiProjectInfo
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    only_shared_with_project: Union[Unset, None, int] = UNSET,
    include_permissions: Union[Unset, None, bool] = False,
    include_archived: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/Project".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["onlySharedWithProject"] = only_shared_with_project

    params["includePermissions"] = include_permissions

    params["includeArchived"] = include_archived

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
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiProjectInfo"]]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiProjectInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiProjectInfo"]]
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
    only_shared_with_project: Union[Unset, None, int] = UNSET,
    include_permissions: Union[Unset, None, bool] = False,
    include_archived: Union[Unset, None, bool] = True,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiProjectInfo"]]
]:
    """Get my projects

     Get projects the current user is assigned to.

    Args:
        only_shared_with_project (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):
        include_archived (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiProjectInfo']]]
    """

    kwargs = _get_kwargs(
        client=client,
        only_shared_with_project=only_shared_with_project,
        include_permissions=include_permissions,
        include_archived=include_archived,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    only_shared_with_project: Union[Unset, None, int] = UNSET,
    include_permissions: Union[Unset, None, bool] = False,
    include_archived: Union[Unset, None, bool] = True,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiProjectInfo"]]
]:
    """Get my projects

     Get projects the current user is assigned to.

    Args:
        only_shared_with_project (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):
        include_archived (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiProjectInfo']]]
    """

    return sync_detailed(
        client=client,
        only_shared_with_project=only_shared_with_project,
        include_permissions=include_permissions,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    only_shared_with_project: Union[Unset, None, int] = UNSET,
    include_permissions: Union[Unset, None, bool] = False,
    include_archived: Union[Unset, None, bool] = True,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiProjectInfo"]]
]:
    """Get my projects

     Get projects the current user is assigned to.

    Args:
        only_shared_with_project (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):
        include_archived (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiProjectInfo']]]
    """

    kwargs = _get_kwargs(
        client=client,
        only_shared_with_project=only_shared_with_project,
        include_permissions=include_permissions,
        include_archived=include_archived,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    only_shared_with_project: Union[Unset, None, int] = UNSET,
    include_permissions: Union[Unset, None, bool] = False,
    include_archived: Union[Unset, None, bool] = True,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiProjectInfo"]]
]:
    """Get my projects

     Get projects the current user is assigned to.

    Args:
        only_shared_with_project (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):
        include_archived (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiProjectInfo']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            only_shared_with_project=only_shared_with_project,
            include_permissions=include_permissions,
            include_archived=include_archived,
        )
    ).parsed
