from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_field_meta import ApiFieldMeta
from ...models.api_field_sort_mode import ApiFieldSortMode
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_item_type import ApiItemType
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    item_type: ApiItemType,
    *,
    client: AuthenticatedClient,
    include_rich_text_fields: Union[Unset, None, bool] = False,
    sort_mode: Union[Unset, None, ApiFieldSortMode] = ApiFieldSortMode.BYTITLE,
    include_deactivated: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/Project/{projectId}/Meta/{itemType}/Fields".format(
        client.base_url, projectId=project_id, itemType=item_type
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["includeRichTextFields"] = include_rich_text_fields

    json_sort_mode: Union[Unset, None, str] = UNSET
    if not isinstance(sort_mode, Unset):
        json_sort_mode = sort_mode.value if sort_mode else None

    params["sortMode"] = json_sort_mode

    params["includeDeactivated"] = include_deactivated

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
        List["ApiFieldMeta"],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiFieldMeta.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
        List["ApiFieldMeta"],
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
    item_type: ApiItemType,
    *,
    client: AuthenticatedClient,
    include_rich_text_fields: Union[Unset, None, bool] = False,
    sort_mode: Union[Unset, None, ApiFieldSortMode] = ApiFieldSortMode.BYTITLE,
    include_deactivated: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiFieldMeta"],
    ]
]:
    """Get fields meta-data as list

     Get meta-data of fields in the project with the given *projectId* and *itemType*.
                also returns the EditMeta of each field.

    Args:
        project_id (int):
        item_type (ApiItemType): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        include_rich_text_fields (Union[Unset, None, bool]):
        sort_mode (Union[Unset, None, ApiFieldSortMode]): The different modes in which the list of
            fields can be sorted.
            This enum has the following values:
              - `ById` Sorts the fields by their Id.
              - `ByLayoutPosition` Sort the fields by the position in the edit layout. Fields which
            are not part of the edit layout are added at the end.
              - `ByTitle` Sort the fields by their title.
             Default: ApiFieldSortMode.BYTITLE.
        include_deactivated (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiFieldMeta']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_type=item_type,
        client=client,
        include_rich_text_fields=include_rich_text_fields,
        sort_mode=sort_mode,
        include_deactivated=include_deactivated,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    item_type: ApiItemType,
    *,
    client: AuthenticatedClient,
    include_rich_text_fields: Union[Unset, None, bool] = False,
    sort_mode: Union[Unset, None, ApiFieldSortMode] = ApiFieldSortMode.BYTITLE,
    include_deactivated: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiFieldMeta"],
    ]
]:
    """Get fields meta-data as list

     Get meta-data of fields in the project with the given *projectId* and *itemType*.
                also returns the EditMeta of each field.

    Args:
        project_id (int):
        item_type (ApiItemType): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        include_rich_text_fields (Union[Unset, None, bool]):
        sort_mode (Union[Unset, None, ApiFieldSortMode]): The different modes in which the list of
            fields can be sorted.
            This enum has the following values:
              - `ById` Sorts the fields by their Id.
              - `ByLayoutPosition` Sort the fields by the position in the edit layout. Fields which
            are not part of the edit layout are added at the end.
              - `ByTitle` Sort the fields by their title.
             Default: ApiFieldSortMode.BYTITLE.
        include_deactivated (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiFieldMeta']]]
    """

    return sync_detailed(
        project_id=project_id,
        item_type=item_type,
        client=client,
        include_rich_text_fields=include_rich_text_fields,
        sort_mode=sort_mode,
        include_deactivated=include_deactivated,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    item_type: ApiItemType,
    *,
    client: AuthenticatedClient,
    include_rich_text_fields: Union[Unset, None, bool] = False,
    sort_mode: Union[Unset, None, ApiFieldSortMode] = ApiFieldSortMode.BYTITLE,
    include_deactivated: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiFieldMeta"],
    ]
]:
    """Get fields meta-data as list

     Get meta-data of fields in the project with the given *projectId* and *itemType*.
                also returns the EditMeta of each field.

    Args:
        project_id (int):
        item_type (ApiItemType): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        include_rich_text_fields (Union[Unset, None, bool]):
        sort_mode (Union[Unset, None, ApiFieldSortMode]): The different modes in which the list of
            fields can be sorted.
            This enum has the following values:
              - `ById` Sorts the fields by their Id.
              - `ByLayoutPosition` Sort the fields by the position in the edit layout. Fields which
            are not part of the edit layout are added at the end.
              - `ByTitle` Sort the fields by their title.
             Default: ApiFieldSortMode.BYTITLE.
        include_deactivated (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiFieldMeta']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_type=item_type,
        client=client,
        include_rich_text_fields=include_rich_text_fields,
        sort_mode=sort_mode,
        include_deactivated=include_deactivated,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    item_type: ApiItemType,
    *,
    client: AuthenticatedClient,
    include_rich_text_fields: Union[Unset, None, bool] = False,
    sort_mode: Union[Unset, None, ApiFieldSortMode] = ApiFieldSortMode.BYTITLE,
    include_deactivated: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiFieldMeta"],
    ]
]:
    """Get fields meta-data as list

     Get meta-data of fields in the project with the given *projectId* and *itemType*.
                also returns the EditMeta of each field.

    Args:
        project_id (int):
        item_type (ApiItemType): Identifies the type of item.
            This enum has the following values:
              - `Defect`
              - `ExternalJira`
              - `ExternalOtrs`
              - `Requirement`
              - `Script`
              - `TestCase`
              - `TestExecution`
              - `TestScenario`
        include_rich_text_fields (Union[Unset, None, bool]):
        sort_mode (Union[Unset, None, ApiFieldSortMode]): The different modes in which the list of
            fields can be sorted.
            This enum has the following values:
              - `ById` Sorts the fields by their Id.
              - `ByLayoutPosition` Sort the fields by the position in the edit layout. Fields which
            are not part of the edit layout are added at the end.
              - `ByTitle` Sort the fields by their title.
             Default: ApiFieldSortMode.BYTITLE.
        include_deactivated (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiFieldMeta']]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            item_type=item_type,
            client=client,
            include_rich_text_fields=include_rich_text_fields,
            sort_mode=sort_mode,
            include_deactivated=include_deactivated,
        )
    ).parsed
