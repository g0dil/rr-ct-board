from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_device_for_person_response_200 import GetDeviceForPersonResponse200
from ...types import Response


def _get_kwargs(
    person_id: int,
    device_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/devices/{device_id}".format(
            person_id=person_id,
            device_id=device_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDeviceForPersonResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDeviceForPersonResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetDeviceForPersonResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetDeviceForPersonResponse200]:
    """Get specified device

     If person ID and device ID are know you can fetch all information about one device using this
    endpoint.

    Args:
        person_id (int):  Example: 42.
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDeviceForPersonResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        device_id=device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetDeviceForPersonResponse200 | None:
    """Get specified device

     If person ID and device ID are know you can fetch all information about one device using this
    endpoint.

    Args:
        person_id (int):  Example: 42.
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDeviceForPersonResponse200
    """

    return sync_detailed(
        person_id=person_id,
        device_id=device_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetDeviceForPersonResponse200]:
    """Get specified device

     If person ID and device ID are know you can fetch all information about one device using this
    endpoint.

    Args:
        person_id (int):  Example: 42.
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDeviceForPersonResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        device_id=device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetDeviceForPersonResponse200 | None:
    """Get specified device

     If person ID and device ID are know you can fetch all information about one device using this
    endpoint.

    Args:
        person_id (int):  Example: 42.
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDeviceForPersonResponse200
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            device_id=device_id,
            client=client,
        )
    ).parsed
