from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_item_search_result import ApiItemSearchResult
from ...models.api_item_type import ApiItemType
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, int] = 0,
    search_term: Union[Unset, None, str] = "",
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_archived: Union[Unset, None, bool] = False,
    first_results: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 0,
    include_permissions: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/Project/{projectId}/Item".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["folderId"] = folder_id

    params["searchTerm"] = search_term

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

    params["includeArchived"] = include_archived

    params["firstResults"] = first_results

    params["maxResults"] = max_results

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
        ApiItemSearchResult,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiItemSearchResult.from_dict(response.json())

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
        ApiItemSearchResult,
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
    project_id: int,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, int] = 0,
    search_term: Union[Unset, None, str] = "",
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_archived: Union[Unset, None, bool] = False,
    first_results: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 0,
    include_permissions: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemSearchResult,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Search items

     Search for items in the project which contain the searchTerm in their id or name.
                Note: although this method supports searching for items of any type (see itemType
    parameter)
                the result of such a call is the aggregation of results retrived per each item type
    (what is specially important in regard to
                firstResults/maxResults parameters). Please refer to description of
    firstResults/maxResults for details.

    Args:
        project_id (int):
        folder_id (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):  Default: ''.
        item_type (Union[ApiItemType, None, Unset]):
        include_archived (Union[Unset, None, bool]):
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemSearchResult, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        folder_id=folder_id,
        search_term=search_term,
        item_type=item_type,
        include_archived=include_archived,
        first_results=first_results,
        max_results=max_results,
        include_permissions=include_permissions,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, int] = 0,
    search_term: Union[Unset, None, str] = "",
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_archived: Union[Unset, None, bool] = False,
    first_results: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 0,
    include_permissions: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemSearchResult,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Search items

     Search for items in the project which contain the searchTerm in their id or name.
                Note: although this method supports searching for items of any type (see itemType
    parameter)
                the result of such a call is the aggregation of results retrived per each item type
    (what is specially important in regard to
                firstResults/maxResults parameters). Please refer to description of
    firstResults/maxResults for details.

    Args:
        project_id (int):
        folder_id (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):  Default: ''.
        item_type (Union[ApiItemType, None, Unset]):
        include_archived (Union[Unset, None, bool]):
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemSearchResult, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        folder_id=folder_id,
        search_term=search_term,
        item_type=item_type,
        include_archived=include_archived,
        first_results=first_results,
        max_results=max_results,
        include_permissions=include_permissions,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, int] = 0,
    search_term: Union[Unset, None, str] = "",
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_archived: Union[Unset, None, bool] = False,
    first_results: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 0,
    include_permissions: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemSearchResult,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Search items

     Search for items in the project which contain the searchTerm in their id or name.
                Note: although this method supports searching for items of any type (see itemType
    parameter)
                the result of such a call is the aggregation of results retrived per each item type
    (what is specially important in regard to
                firstResults/maxResults parameters). Please refer to description of
    firstResults/maxResults for details.

    Args:
        project_id (int):
        folder_id (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):  Default: ''.
        item_type (Union[ApiItemType, None, Unset]):
        include_archived (Union[Unset, None, bool]):
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemSearchResult, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        folder_id=folder_id,
        search_term=search_term,
        item_type=item_type,
        include_archived=include_archived,
        first_results=first_results,
        max_results=max_results,
        include_permissions=include_permissions,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, int] = 0,
    search_term: Union[Unset, None, str] = "",
    item_type: Union[ApiItemType, None, Unset] = UNSET,
    include_archived: Union[Unset, None, bool] = False,
    first_results: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 0,
    include_permissions: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemSearchResult,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Search items

     Search for items in the project which contain the searchTerm in their id or name.
                Note: although this method supports searching for items of any type (see itemType
    parameter)
                the result of such a call is the aggregation of results retrived per each item type
    (what is specially important in regard to
                firstResults/maxResults parameters). Please refer to description of
    firstResults/maxResults for details.

    Args:
        project_id (int):
        folder_id (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):  Default: ''.
        item_type (Union[ApiItemType, None, Unset]):
        include_archived (Union[Unset, None, bool]):
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        include_permissions (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemSearchResult, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            folder_id=folder_id,
            search_term=search_term,
            item_type=item_type,
            include_archived=include_archived,
            first_results=first_results,
            max_results=max_results,
            include_permissions=include_permissions,
        )
    ).parsed
