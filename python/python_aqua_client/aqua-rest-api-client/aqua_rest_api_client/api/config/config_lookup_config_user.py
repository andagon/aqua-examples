from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_config_element import ApiConfigElement
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    data_path: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/ConfigData/User".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["dataPath"] = data_path

    params["projectId"] = project_id

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
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiConfigElement,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiConfigElement.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
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
        ApiConfigElement,
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
    *,
    client: AuthenticatedClient,
    data_path: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiConfigElement,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get my config elements

     Performs lookup of config elements from \"user\" point of view i.e. taking into consideration the
    following fallback rules:

    a) When looking up for project-related entries (projectId is not null) then:
      a1) at first try to find config element defined in the scope of current user and project
      a2) if nothing found then try to find project-default config element
      a3) if nothing found then try to find global config element defined in the scope of current user
      a4) finally, if nothing found, then try to find global-default config element
    b) When looking up for global entries (projectId is null) then:
      b1) at first try to find global config element defined in the scope of current user
      b2) if nothing found then try to find global-default config element


    Args:
        data_path (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiConfigElement, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        data_path=data_path,
        project_id=project_id,
        include_data=include_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    data_path: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiConfigElement,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get my config elements

     Performs lookup of config elements from \"user\" point of view i.e. taking into consideration the
    following fallback rules:

    a) When looking up for project-related entries (projectId is not null) then:
      a1) at first try to find config element defined in the scope of current user and project
      a2) if nothing found then try to find project-default config element
      a3) if nothing found then try to find global config element defined in the scope of current user
      a4) finally, if nothing found, then try to find global-default config element
    b) When looking up for global entries (projectId is null) then:
      b1) at first try to find global config element defined in the scope of current user
      b2) if nothing found then try to find global-default config element


    Args:
        data_path (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiConfigElement, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        data_path=data_path,
        project_id=project_id,
        include_data=include_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    data_path: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiConfigElement,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get my config elements

     Performs lookup of config elements from \"user\" point of view i.e. taking into consideration the
    following fallback rules:

    a) When looking up for project-related entries (projectId is not null) then:
      a1) at first try to find config element defined in the scope of current user and project
      a2) if nothing found then try to find project-default config element
      a3) if nothing found then try to find global config element defined in the scope of current user
      a4) finally, if nothing found, then try to find global-default config element
    b) When looking up for global entries (projectId is null) then:
      b1) at first try to find global config element defined in the scope of current user
      b2) if nothing found then try to find global-default config element


    Args:
        data_path (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiConfigElement, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        data_path=data_path,
        project_id=project_id,
        include_data=include_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    data_path: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiConfigElement,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Get my config elements

     Performs lookup of config elements from \"user\" point of view i.e. taking into consideration the
    following fallback rules:

    a) When looking up for project-related entries (projectId is not null) then:
      a1) at first try to find config element defined in the scope of current user and project
      a2) if nothing found then try to find project-default config element
      a3) if nothing found then try to find global config element defined in the scope of current user
      a4) finally, if nothing found, then try to find global-default config element
    b) When looking up for global entries (projectId is null) then:
      b1) at first try to find global config element defined in the scope of current user
      b2) if nothing found then try to find global-default config element


    Args:
        data_path (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        include_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiConfigElement, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            data_path=data_path,
            project_id=project_id,
            include_data=include_data,
        )
    ).parsed
