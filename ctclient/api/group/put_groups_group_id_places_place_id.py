from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_groups_group_id_places_place_id_body import (
    PutGroupsGroupIdPlacesPlaceIdBody,
)
from ...models.put_groups_group_id_places_place_id_response_200 import (
    PutGroupsGroupIdPlacesPlaceIdResponse200,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
    place_id: int,
    *,
    body: PutGroupsGroupIdPlacesPlaceIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/groups/{group_id}/places/{place_id}".format(
            group_id=group_id,
            place_id=place_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PutGroupsGroupIdPlacesPlaceIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = response.text
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
) -> Response[Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupsGroupIdPlacesPlaceIdBody,
) -> Response[Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str]:
    """
    Args:
        group_id (int):  Example: 42.
        place_id (int):
        body (PutGroupsGroupIdPlacesPlaceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        place_id=place_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupsGroupIdPlacesPlaceIdBody,
) -> Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str | None:
    """
    Args:
        group_id (int):  Example: 42.
        place_id (int):
        body (PutGroupsGroupIdPlacesPlaceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str
    """

    return sync_detailed(
        group_id=group_id,
        place_id=place_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupsGroupIdPlacesPlaceIdBody,
) -> Response[Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str]:
    """
    Args:
        group_id (int):  Example: 42.
        place_id (int):
        body (PutGroupsGroupIdPlacesPlaceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        place_id=place_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupsGroupIdPlacesPlaceIdBody,
) -> Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str | None:
    """
    Args:
        group_id (int):  Example: 42.
        place_id (int):
        body (PutGroupsGroupIdPlacesPlaceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutGroupsGroupIdPlacesPlaceIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            place_id=place_id,
            client=client,
            body=body,
        )
    ).parsed
