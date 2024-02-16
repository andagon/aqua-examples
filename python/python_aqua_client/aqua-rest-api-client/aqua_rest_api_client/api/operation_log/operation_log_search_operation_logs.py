import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_search_operation_log_result import ApiSearchOperationLogResult
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    first_results: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    folder_id: Union[Unset, None, int] = UNSET,
    folder_path: Union[Unset, None, str] = UNSET,
    operation_user_id: Union[Unset, None, int] = UNSET,
    date_from_utc: Union[Unset, None, datetime.datetime] = UNSET,
    date_to_utc: Union[Unset, None, datetime.datetime] = UNSET,
    category: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/OperationLog/Search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["firstResults"] = first_results

    params["maxResults"] = max_results

    params["projectId"] = project_id

    params["folderId"] = folder_id

    params["folderPath"] = folder_path

    params["operationUserId"] = operation_user_id

    json_date_from_utc: Union[Unset, None, str] = UNSET
    if not isinstance(date_from_utc, Unset):
        json_date_from_utc = date_from_utc.isoformat() if date_from_utc else None

    params["dateFromUTC"] = json_date_from_utc

    json_date_to_utc: Union[Unset, None, str] = UNSET
    if not isinstance(date_to_utc, Unset):
        json_date_to_utc = date_to_utc.isoformat() if date_to_utc else None

    params["dateToUTC"] = json_date_to_utc

    params["category"] = category

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
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSearchOperationLogResult,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSearchOperationLogResult.from_dict(response.json())

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
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSearchOperationLogResult,
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
    first_results: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    folder_id: Union[Unset, None, int] = UNSET,
    folder_path: Union[Unset, None, str] = UNSET,
    operation_user_id: Union[Unset, None, int] = UNSET,
    date_from_utc: Union[Unset, None, datetime.datetime] = UNSET,
    date_to_utc: Union[Unset, None, datetime.datetime] = UNSET,
    category: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSearchOperationLogResult,
        ApiUnauthorizedError,
    ]
]:
    """Search log

     Performs search of operation logs i.e. log entries that represent e.g. history of administrative
                changes in the system. There are several search parameters available. Lack of parameter
    means no
                filtering on given field.

    Args:
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        folder_id (Union[Unset, None, int]):
        folder_path (Union[Unset, None, str]):
        operation_user_id (Union[Unset, None, int]):
        date_from_utc (Union[Unset, None, datetime.datetime]):
        date_to_utc (Union[Unset, None, datetime.datetime]):
        category (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSearchOperationLogResult, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        first_results=first_results,
        max_results=max_results,
        project_id=project_id,
        folder_id=folder_id,
        folder_path=folder_path,
        operation_user_id=operation_user_id,
        date_from_utc=date_from_utc,
        date_to_utc=date_to_utc,
        category=category,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    first_results: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    folder_id: Union[Unset, None, int] = UNSET,
    folder_path: Union[Unset, None, str] = UNSET,
    operation_user_id: Union[Unset, None, int] = UNSET,
    date_from_utc: Union[Unset, None, datetime.datetime] = UNSET,
    date_to_utc: Union[Unset, None, datetime.datetime] = UNSET,
    category: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSearchOperationLogResult,
        ApiUnauthorizedError,
    ]
]:
    """Search log

     Performs search of operation logs i.e. log entries that represent e.g. history of administrative
                changes in the system. There are several search parameters available. Lack of parameter
    means no
                filtering on given field.

    Args:
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        folder_id (Union[Unset, None, int]):
        folder_path (Union[Unset, None, str]):
        operation_user_id (Union[Unset, None, int]):
        date_from_utc (Union[Unset, None, datetime.datetime]):
        date_to_utc (Union[Unset, None, datetime.datetime]):
        category (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSearchOperationLogResult, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        first_results=first_results,
        max_results=max_results,
        project_id=project_id,
        folder_id=folder_id,
        folder_path=folder_path,
        operation_user_id=operation_user_id,
        date_from_utc=date_from_utc,
        date_to_utc=date_to_utc,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    first_results: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    folder_id: Union[Unset, None, int] = UNSET,
    folder_path: Union[Unset, None, str] = UNSET,
    operation_user_id: Union[Unset, None, int] = UNSET,
    date_from_utc: Union[Unset, None, datetime.datetime] = UNSET,
    date_to_utc: Union[Unset, None, datetime.datetime] = UNSET,
    category: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSearchOperationLogResult,
        ApiUnauthorizedError,
    ]
]:
    """Search log

     Performs search of operation logs i.e. log entries that represent e.g. history of administrative
                changes in the system. There are several search parameters available. Lack of parameter
    means no
                filtering on given field.

    Args:
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        folder_id (Union[Unset, None, int]):
        folder_path (Union[Unset, None, str]):
        operation_user_id (Union[Unset, None, int]):
        date_from_utc (Union[Unset, None, datetime.datetime]):
        date_to_utc (Union[Unset, None, datetime.datetime]):
        category (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSearchOperationLogResult, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        first_results=first_results,
        max_results=max_results,
        project_id=project_id,
        folder_id=folder_id,
        folder_path=folder_path,
        operation_user_id=operation_user_id,
        date_from_utc=date_from_utc,
        date_to_utc=date_to_utc,
        category=category,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    first_results: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    folder_id: Union[Unset, None, int] = UNSET,
    folder_path: Union[Unset, None, str] = UNSET,
    operation_user_id: Union[Unset, None, int] = UNSET,
    date_from_utc: Union[Unset, None, datetime.datetime] = UNSET,
    date_to_utc: Union[Unset, None, datetime.datetime] = UNSET,
    category: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSearchOperationLogResult,
        ApiUnauthorizedError,
    ]
]:
    """Search log

     Performs search of operation logs i.e. log entries that represent e.g. history of administrative
                changes in the system. There are several search parameters available. Lack of parameter
    means no
                filtering on given field.

    Args:
        first_results (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        folder_id (Union[Unset, None, int]):
        folder_path (Union[Unset, None, str]):
        operation_user_id (Union[Unset, None, int]):
        date_from_utc (Union[Unset, None, datetime.datetime]):
        date_to_utc (Union[Unset, None, datetime.datetime]):
        category (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSearchOperationLogResult, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            first_results=first_results,
            max_results=max_results,
            project_id=project_id,
            folder_id=folder_id,
            folder_path=folder_path,
            operation_user_id=operation_user_id,
            date_from_utc=date_from_utc,
            date_to_utc=date_to_utc,
            category=category,
        )
    ).parsed
