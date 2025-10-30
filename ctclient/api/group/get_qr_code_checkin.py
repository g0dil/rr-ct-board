from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_qr_code_checkin_response_200 import GetQRCodeCheckinResponse200
from ...types import Response


def _get_kwargs(
    group_id: int,
    person_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/qrcodecheckin/{person_id}/pdf".format(
            group_id=group_id,
            person_id=person_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetQRCodeCheckinResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetQRCodeCheckinResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Any | GetQRCodeCheckinResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetQRCodeCheckinResponse200 | str]:
    """Get link to QR-Code for CheckIn PDF

     Get link to QR-Code for CheckIn PDF

    Args:
        group_id (int):  Example: 42.
        person_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetQRCodeCheckinResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        person_id=person_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetQRCodeCheckinResponse200 | str | None:
    """Get link to QR-Code for CheckIn PDF

     Get link to QR-Code for CheckIn PDF

    Args:
        group_id (int):  Example: 42.
        person_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetQRCodeCheckinResponse200 | str
    """

    return sync_detailed(
        group_id=group_id,
        person_id=person_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetQRCodeCheckinResponse200 | str]:
    """Get link to QR-Code for CheckIn PDF

     Get link to QR-Code for CheckIn PDF

    Args:
        group_id (int):  Example: 42.
        person_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetQRCodeCheckinResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        person_id=person_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetQRCodeCheckinResponse200 | str | None:
    """Get link to QR-Code for CheckIn PDF

     Get link to QR-Code for CheckIn PDF

    Args:
        group_id (int):  Example: 42.
        person_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetQRCodeCheckinResponse200 | str
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            person_id=person_id,
            client=client,
        )
    ).parsed
