from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_internal_permissions_for_person_response_200 import (
    GetInternalPermissionsForPersonResponse200,
)
from ...types import Response


def _get_kwargs(
    person_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/permissions/internal/persons/{person_id}".format(
            person_id=person_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetInternalPermissionsForPersonResponse200 | None:
    if response.status_code == 200:
        response_200 = GetInternalPermissionsForPersonResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetInternalPermissionsForPersonResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetInternalPermissionsForPersonResponse200]:
    """Lookup Person-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Person`. This
    endpoint calculates the result of all group internal permissions with regard to a person. That mean,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+invite persons: true`. This means, the current user can invite the
    person with `{personId}` to ChurchTools based on this group internal permissions. That could mean,
    the user can the person are in the same group or the user is in an superior groups, which inherits
    permissions.

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInternalPermissionsForPersonResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetInternalPermissionsForPersonResponse200 | None:
    """Lookup Person-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Person`. This
    endpoint calculates the result of all group internal permissions with regard to a person. That mean,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+invite persons: true`. This means, the current user can invite the
    person with `{personId}` to ChurchTools based on this group internal permissions. That could mean,
    the user can the person are in the same group or the user is in an superior groups, which inherits
    permissions.

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInternalPermissionsForPersonResponse200
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetInternalPermissionsForPersonResponse200]:
    """Lookup Person-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Person`. This
    endpoint calculates the result of all group internal permissions with regard to a person. That mean,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+invite persons: true`. This means, the current user can invite the
    person with `{personId}` to ChurchTools based on this group internal permissions. That could mean,
    the user can the person are in the same group or the user is in an superior groups, which inherits
    permissions.

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInternalPermissionsForPersonResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetInternalPermissionsForPersonResponse200 | None:
    """Lookup Person-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Person`. This
    endpoint calculates the result of all group internal permissions with regard to a person. That mean,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+invite persons: true`. This means, the current user can invite the
    person with `{personId}` to ChurchTools based on this group internal permissions. That could mean,
    the user can the person are in the same group or the user is in an superior groups, which inherits
    permissions.

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInternalPermissionsForPersonResponse200
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
        )
    ).parsed
