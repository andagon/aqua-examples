from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_redirect_result import ApiRedirectResult
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    access_token: Union[Unset, None, str] = UNSET,
    tenant_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Defect/{id}/Attachment/{attachmentId}/data".format(client.base_url, id=id, attachmentId=attachment_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["download"] = download

    params["access_token"] = access_token

    params["tenantId"] = tenant_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ApiRedirectResult, File, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == HTTPStatus.TEMPORARY_REDIRECT:
        response_307 = ApiRedirectResult.from_dict(response.json())

        return response_307
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.text)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(str, response.text)
        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(str, response.text)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(str, response.text)
        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = cast(str, response.text)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ApiRedirectResult, File, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    access_token: Union[Unset, None, str] = UNSET,
    tenant_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[ApiRedirectResult, File, str]]:
    """Get attachment

     Get the file content of the specified attachment. When possible, the content-type
                header will contain a fitting mime type for the returned content. The response might
                redirect to the actual download URL.


    Args:
        id (int):
        attachment_id (int):
        download (Union[Unset, None, bool]):
        access_token (Union[Unset, None, str]):
        tenant_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiRedirectResult, File, str]]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        client=client,
        download=download,
        access_token=access_token,
        tenant_id=tenant_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    access_token: Union[Unset, None, str] = UNSET,
    tenant_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ApiRedirectResult, File, str]]:
    """Get attachment

     Get the file content of the specified attachment. When possible, the content-type
                header will contain a fitting mime type for the returned content. The response might
                redirect to the actual download URL.


    Args:
        id (int):
        attachment_id (int):
        download (Union[Unset, None, bool]):
        access_token (Union[Unset, None, str]):
        tenant_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiRedirectResult, File, str]]
    """

    return sync_detailed(
        id=id,
        attachment_id=attachment_id,
        client=client,
        download=download,
        access_token=access_token,
        tenant_id=tenant_id,
    ).parsed


async def asyncio_detailed(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    access_token: Union[Unset, None, str] = UNSET,
    tenant_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[ApiRedirectResult, File, str]]:
    """Get attachment

     Get the file content of the specified attachment. When possible, the content-type
                header will contain a fitting mime type for the returned content. The response might
                redirect to the actual download URL.


    Args:
        id (int):
        attachment_id (int):
        download (Union[Unset, None, bool]):
        access_token (Union[Unset, None, str]):
        tenant_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiRedirectResult, File, str]]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        client=client,
        download=download,
        access_token=access_token,
        tenant_id=tenant_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    download: Union[Unset, None, bool] = False,
    access_token: Union[Unset, None, str] = UNSET,
    tenant_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ApiRedirectResult, File, str]]:
    """Get attachment

     Get the file content of the specified attachment. When possible, the content-type
                header will contain a fitting mime type for the returned content. The response might
                redirect to the actual download URL.


    Args:
        id (int):
        attachment_id (int):
        download (Union[Unset, None, bool]):
        access_token (Union[Unset, None, str]):
        tenant_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiRedirectResult, File, str]]
    """

    return (
        await asyncio_detailed(
            id=id,
            attachment_id=attachment_id,
            client=client,
            download=download,
            access_token=access_token,
            tenant_id=tenant_id,
        )
    ).parsed
