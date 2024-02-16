from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_image_upload_info import ApiImageUploadInfo
from ...models.api_internal_error import ApiInternalError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...models.image_upload_image_multipart_data import ImageUploadImageMultipartData
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: ImageUploadImageMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/Image".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiImageUploadInfo.from_dict(response.json())

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
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]
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
    multipart_data: ImageUploadImageMultipartData,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload image

     Upload an image. The image is temporarily stored and its URL is included in the response.
    This URL can then be used to include images into rich text, e.g. in a description.

    Args:
        multipart_data (ImageUploadImageMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: ImageUploadImageMultipartData,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload image

     Upload an image. The image is temporarily stored and its URL is included in the response.
    This URL can then be used to include images into rich text, e.g. in a description.

    Args:
        multipart_data (ImageUploadImageMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: ImageUploadImageMultipartData,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload image

     Upload an image. The image is temporarily stored and its URL is included in the response.
    This URL can then be used to include images into rich text, e.g. in a description.

    Args:
        multipart_data (ImageUploadImageMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: ImageUploadImageMultipartData,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]
]:
    """Upload image

     Upload an image. The image is temporarily stored and its URL is included in the response.
    This URL can then be used to include images into rich text, e.g. in a description.

    Args:
        multipart_data (ImageUploadImageMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiImageUploadInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
