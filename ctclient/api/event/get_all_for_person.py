from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_for_person_response_200_item import (
    GetAllForPersonResponse200Item,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    *,
    person_is_requester: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["personIsRequester"] = person_is_requester

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/exchangerequests".format(
            person_id=person_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[GetAllForPersonResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAllForPersonResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[GetAllForPersonResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    person_is_requester: bool | Unset = UNSET,
) -> Response[list[GetAllForPersonResponse200Item]]:
    """Get all service exchange requests for a user

     Returns all exchange requests for a certain user

    Args:
        person_id (int):  Example: 42.
        person_is_requester (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[GetAllForPersonResponse200Item]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        person_is_requester=person_is_requester,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    person_is_requester: bool | Unset = UNSET,
) -> list[GetAllForPersonResponse200Item] | None:
    """Get all service exchange requests for a user

     Returns all exchange requests for a certain user

    Args:
        person_id (int):  Example: 42.
        person_is_requester (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[GetAllForPersonResponse200Item]
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        person_is_requester=person_is_requester,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    person_is_requester: bool | Unset = UNSET,
) -> Response[list[GetAllForPersonResponse200Item]]:
    """Get all service exchange requests for a user

     Returns all exchange requests for a certain user

    Args:
        person_id (int):  Example: 42.
        person_is_requester (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[GetAllForPersonResponse200Item]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        person_is_requester=person_is_requester,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    person_is_requester: bool | Unset = UNSET,
) -> list[GetAllForPersonResponse200Item] | None:
    """Get all service exchange requests for a user

     Returns all exchange requests for a certain user

    Args:
        person_id (int):  Example: 42.
        person_is_requester (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[GetAllForPersonResponse200Item]
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            person_is_requester=person_is_requester,
        )
    ).parsed
