from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_item_type import ApiItemType
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...models.api_user_view import ApiUserView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_view_id: int,
    *,
    client: AuthenticatedClient,
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_permissions: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/UserView/{userViewId}".format(client.base_url, userViewId=user_view_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_item_type: Union[None, Unset, str]
    if isinstance(item_type, Unset):
        json_item_type = UNSET
    elif item_type is None:
        json_item_type = None

    else:
        json_item_type = UNSET
        if not isinstance(item_type, Unset):
            json_item_type = item_type.value if item_type else None

    params["itemType"] = json_item_type

    params["includePermissions"] = include_permissions

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
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        ApiUserView,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiUserView.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
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
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        ApiUserView,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_view_id: int,
    *,
    client: AuthenticatedClient,
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_permissions: Union[Unset, None, bool] = True,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        ApiUserView,
    ]
]:
    """Get user view

     Get the user view with the given *userViewId*.

    Args:
        user_view_id (int):
        item_type (Union[ApiItemType, None, Unset]):
        include_permissions (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUserView]]
    """

    kwargs = _get_kwargs(
        user_view_id=user_view_id,
        client=client,
        item_type=item_type,
        include_permissions=include_permissions,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_view_id: int,
    *,
    client: AuthenticatedClient,
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_permissions: Union[Unset, None, bool] = True,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        ApiUserView,
    ]
]:
    """Get user view

     Get the user view with the given *userViewId*.

    Args:
        user_view_id (int):
        item_type (Union[ApiItemType, None, Unset]):
        include_permissions (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUserView]]
    """

    return sync_detailed(
        user_view_id=user_view_id,
        client=client,
        item_type=item_type,
        include_permissions=include_permissions,
    ).parsed


async def asyncio_detailed(
    user_view_id: int,
    *,
    client: AuthenticatedClient,
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_permissions: Union[Unset, None, bool] = True,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        ApiUserView,
    ]
]:
    """Get user view

     Get the user view with the given *userViewId*.

    Args:
        user_view_id (int):
        item_type (Union[ApiItemType, None, Unset]):
        include_permissions (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUserView]]
    """

    kwargs = _get_kwargs(
        user_view_id=user_view_id,
        client=client,
        item_type=item_type,
        include_permissions=include_permissions,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_view_id: int,
    *,
    client: AuthenticatedClient,
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_permissions: Union[Unset, None, bool] = True,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        ApiUserView,
    ]
]:
    """Get user view

     Get the user view with the given *userViewId*.

    Args:
        user_view_id (int):
        item_type (Union[ApiItemType, None, Unset]):
        include_permissions (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUserView]]
    """

    return (
        await asyncio_detailed(
            user_view_id=user_view_id,
            client=client,
            item_type=item_type,
            include_permissions=include_permissions,
        )
    ).parsed
