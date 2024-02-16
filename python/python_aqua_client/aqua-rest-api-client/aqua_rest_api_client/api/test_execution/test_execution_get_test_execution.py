from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_rich_text_include_type import ApiRichTextIncludeType
from ...models.api_test_execution import ApiTestExecution
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    rich_text_format_to_include: Union[Unset, None, ApiRichTextIncludeType] = ApiRichTextIncludeType.ALL,
) -> Dict[str, Any]:
    url = "{}/api/TestExecution/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_rich_text_format_to_include: Union[Unset, None, str] = UNSET
    if not isinstance(rich_text_format_to_include, Unset):
        json_rich_text_format_to_include = rich_text_format_to_include.value if rich_text_format_to_include else None

    params["richTextFormatToInclude"] = json_rich_text_format_to_include

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
        ApiTestExecution,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiTestExecution.from_dict(response.json())

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
        ApiTestExecution,
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
    id: int,
    *,
    client: AuthenticatedClient,
    rich_text_format_to_include: Union[Unset, None, ApiRichTextIncludeType] = ApiRichTextIncludeType.ALL,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiTestExecution,
        ApiUnauthorizedError,
    ]
]:
    """Get test execution

     Get test execution with given *testExecutionId*.

    Args:
        id (int):
        rich_text_format_to_include (Union[Unset, None, ApiRichTextIncludeType]): This enum
            determinates wich information should be included in the richtext.
            This enum has the following values:
              - `All` All, this means Html and plain text are included.
              - `HTML` Html is included.
              - `PlainText` Plain text is included.
             Default: ApiRichTextIncludeType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiTestExecution, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        rich_text_format_to_include=rich_text_format_to_include,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    rich_text_format_to_include: Union[Unset, None, ApiRichTextIncludeType] = ApiRichTextIncludeType.ALL,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiTestExecution,
        ApiUnauthorizedError,
    ]
]:
    """Get test execution

     Get test execution with given *testExecutionId*.

    Args:
        id (int):
        rich_text_format_to_include (Union[Unset, None, ApiRichTextIncludeType]): This enum
            determinates wich information should be included in the richtext.
            This enum has the following values:
              - `All` All, this means Html and plain text are included.
              - `HTML` Html is included.
              - `PlainText` Plain text is included.
             Default: ApiRichTextIncludeType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiTestExecution, ApiUnauthorizedError]]
    """

    return sync_detailed(
        id=id,
        client=client,
        rich_text_format_to_include=rich_text_format_to_include,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    rich_text_format_to_include: Union[Unset, None, ApiRichTextIncludeType] = ApiRichTextIncludeType.ALL,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiTestExecution,
        ApiUnauthorizedError,
    ]
]:
    """Get test execution

     Get test execution with given *testExecutionId*.

    Args:
        id (int):
        rich_text_format_to_include (Union[Unset, None, ApiRichTextIncludeType]): This enum
            determinates wich information should be included in the richtext.
            This enum has the following values:
              - `All` All, this means Html and plain text are included.
              - `HTML` Html is included.
              - `PlainText` Plain text is included.
             Default: ApiRichTextIncludeType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiTestExecution, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        rich_text_format_to_include=rich_text_format_to_include,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    rich_text_format_to_include: Union[Unset, None, ApiRichTextIncludeType] = ApiRichTextIncludeType.ALL,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiTestExecution,
        ApiUnauthorizedError,
    ]
]:
    """Get test execution

     Get test execution with given *testExecutionId*.

    Args:
        id (int):
        rich_text_format_to_include (Union[Unset, None, ApiRichTextIncludeType]): This enum
            determinates wich information should be included in the richtext.
            This enum has the following values:
              - `All` All, this means Html and plain text are included.
              - `HTML` Html is included.
              - `PlainText` Plain text is included.
             Default: ApiRichTextIncludeType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiTestExecution, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            rich_text_format_to_include=rich_text_format_to_include,
        )
    ).parsed
