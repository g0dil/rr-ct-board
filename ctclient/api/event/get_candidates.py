from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_candidates_response_200 import GetCandidatesResponse200
from ...types import Response


def _get_kwargs(
    person_id: int,
    event_id: int,
    service_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/events/{event_id}/services/{service_id}/exchangerequests/candidates".format(
            person_id=person_id,
            event_id=event_id,
            service_id=service_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCandidatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCandidatesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCandidatesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCandidatesResponse200]:
    """Get candidates for service exchange request

     Returns all possible candidates for an exchange of a service

    Args:
        person_id (int):  Example: 42.
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCandidatesResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        event_id=event_id,
        service_id=service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetCandidatesResponse200 | None:
    """Get candidates for service exchange request

     Returns all possible candidates for an exchange of a service

    Args:
        person_id (int):  Example: 42.
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCandidatesResponse200
    """

    return sync_detailed(
        person_id=person_id,
        event_id=event_id,
        service_id=service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCandidatesResponse200]:
    """Get candidates for service exchange request

     Returns all possible candidates for an exchange of a service

    Args:
        person_id (int):  Example: 42.
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCandidatesResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        event_id=event_id,
        service_id=service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetCandidatesResponse200 | None:
    """Get candidates for service exchange request

     Returns all possible candidates for an exchange of a service

    Args:
        person_id (int):  Example: 42.
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCandidatesResponse200
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            event_id=event_id,
            service_id=service_id,
            client=client,
        )
    ).parsed
