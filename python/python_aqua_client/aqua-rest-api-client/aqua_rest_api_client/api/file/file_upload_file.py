from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_file_upload_info import ApiFileUploadInfo
from ...models.api_internal_error import ApiInternalError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...models.file_upload_file_multipart_data import FileUploadFileMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: FileUploadFileMultipartData,
    file_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/File".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fileName"] = file_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiFileUploadInfo.from_dict(response.json())

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
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]
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
    multipart_data: FileUploadFileMultipartData,
    file_name: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload file

     Upload a file. The file is temporarily stored and its URL is included in the response.
    This URL can then be used to add the file as an attachment when creating or updating
    an item.

    Args:
        file_name (Union[Unset, None, str]):
        multipart_data (FileUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        file_name=file_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: FileUploadFileMultipartData,
    file_name: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload file

     Upload a file. The file is temporarily stored and its URL is included in the response.
    This URL can then be used to add the file as an attachment when creating or updating
    an item.

    Args:
        file_name (Union[Unset, None, str]):
        multipart_data (FileUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        file_name=file_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: FileUploadFileMultipartData,
    file_name: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload file

     Upload a file. The file is temporarily stored and its URL is included in the response.
    This URL can then be used to add the file as an attachment when creating or updating
    an item.

    Args:
        file_name (Union[Unset, None, str]):
        multipart_data (FileUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        file_name=file_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: FileUploadFileMultipartData,
    file_name: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload file

     Upload a file. The file is temporarily stored and its URL is included in the response.
    This URL can then be used to add the file as an attachment when creating or updating
    an item.

    Args:
        file_name (Union[Unset, None, str]):
        multipart_data (FileUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiFileUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            file_name=file_name,
        )
    ).parsed
