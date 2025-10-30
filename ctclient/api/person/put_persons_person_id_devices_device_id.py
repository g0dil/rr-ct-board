from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_persons_person_id_devices_device_id_body import (
    PutPersonsPersonIdDevicesDeviceIdBody,
)
from ...models.put_persons_person_id_devices_device_id_response_200 import (
    PutPersonsPersonIdDevicesDeviceIdResponse200,
)
from ...types import Response


def _get_kwargs(
    person_id: int,
    device_id: str,
    *,
    body: PutPersonsPersonIdDevicesDeviceIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/persons/{person_id}/devices/{device_id}".format(
            person_id=person_id,
            device_id=device_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PutPersonsPersonIdDevicesDeviceIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str]:
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
    body: PutPersonsPersonIdDevicesDeviceIdBody,
) -> Response[Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str]:
    """Create or update new device for person

     Create a new device or update an existing using this endpoint. This endpoint is usually used to
    update the TTL. If the TTL is reached the device will be removed from ChurchTools, cause of
    inactivity.

    Args:
        person_id (int):  Example: 42.
        device_id (str):
        body (PutPersonsPersonIdDevicesDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        device_id=device_id,
        body=body,
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
    body: PutPersonsPersonIdDevicesDeviceIdBody,
) -> Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str | None:
    """Create or update new device for person

     Create a new device or update an existing using this endpoint. This endpoint is usually used to
    update the TTL. If the TTL is reached the device will be removed from ChurchTools, cause of
    inactivity.

    Args:
        person_id (int):  Example: 42.
        device_id (str):
        body (PutPersonsPersonIdDevicesDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str
    """

    return sync_detailed(
        person_id=person_id,
        device_id=device_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutPersonsPersonIdDevicesDeviceIdBody,
) -> Response[Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str]:
    """Create or update new device for person

     Create a new device or update an existing using this endpoint. This endpoint is usually used to
    update the TTL. If the TTL is reached the device will be removed from ChurchTools, cause of
    inactivity.

    Args:
        person_id (int):  Example: 42.
        device_id (str):
        body (PutPersonsPersonIdDevicesDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        device_id=device_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutPersonsPersonIdDevicesDeviceIdBody,
) -> Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str | None:
    """Create or update new device for person

     Create a new device or update an existing using this endpoint. This endpoint is usually used to
    update the TTL. If the TTL is reached the device will be removed from ChurchTools, cause of
    inactivity.

    Args:
        person_id (int):  Example: 42.
        device_id (str):
        body (PutPersonsPersonIdDevicesDeviceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutPersonsPersonIdDevicesDeviceIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            device_id=device_id,
            client=client,
            body=body,
        )
    ).parsed
