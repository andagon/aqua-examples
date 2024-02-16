from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: int,
    step_id: int,
    attachment_script_file_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/TestCase/{id}/TestStep/{stepId}/AttachedScriptFile/{attachmentScriptFileId}/data".format(
        client.base_url, id=id, stepId=step_id, attachmentScriptFileId=attachment_script_file_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["download"] = download

    params["token"] = token

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
        File,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

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
        File,
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
    step_id: int,
    attachment_script_file_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    token: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        File,
    ]
]:
    """Get automation script

     Get the file content of the specified attached script file (used in automation).
                When possible, the content-type header will contain a fitting mime type for the returned
    content.

    Args:
        id (int):
        step_id (int):
        attachment_script_file_id (int):
        download (Union[Unset, None, bool]):
        token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    kwargs = _get_kwargs(
        id=id,
        step_id=step_id,
        attachment_script_file_id=attachment_script_file_id,
        client=client,
        download=download,
        token=token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    step_id: int,
    attachment_script_file_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    token: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        File,
    ]
]:
    """Get automation script

     Get the file content of the specified attached script file (used in automation).
                When possible, the content-type header will contain a fitting mime type for the returned
    content.

    Args:
        id (int):
        step_id (int):
        attachment_script_file_id (int):
        download (Union[Unset, None, bool]):
        token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    return sync_detailed(
        id=id,
        step_id=step_id,
        attachment_script_file_id=attachment_script_file_id,
        client=client,
        download=download,
        token=token,
    ).parsed


async def asyncio_detailed(
    id: int,
    step_id: int,
    attachment_script_file_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    token: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        File,
    ]
]:
    """Get automation script

     Get the file content of the specified attached script file (used in automation).
                When possible, the content-type header will contain a fitting mime type for the returned
    content.

    Args:
        id (int):
        step_id (int):
        attachment_script_file_id (int):
        download (Union[Unset, None, bool]):
        token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    kwargs = _get_kwargs(
        id=id,
        step_id=step_id,
        attachment_script_file_id=attachment_script_file_id,
        client=client,
        download=download,
        token=token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    step_id: int,
    attachment_script_file_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    token: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        File,
    ]
]:
    """Get automation script

     Get the file content of the specified attached script file (used in automation).
                When possible, the content-type header will contain a fitting mime type for the returned
    content.

    Args:
        id (int):
        step_id (int):
        attachment_script_file_id (int):
        download (Union[Unset, None, bool]):
        token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, File]]
    """

    return (
        await asyncio_detailed(
            id=id,
            step_id=step_id,
            attachment_script_file_id=attachment_script_file_id,
            client=client,
            download=download,
            token=token,
        )
    ).parsed
