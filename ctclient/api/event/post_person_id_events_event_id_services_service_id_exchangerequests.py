from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_person_id_events_event_id_services_service_id_exchangerequests_body import (
    PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    event_id: int,
    service_id: str,
    *,
    body: PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBody,
    incoming: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["incoming"] = incoming

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/persons/{person_id}/events/{event_id}/services/{service_id}/exchangerequests".format(
            person_id=person_id,
            event_id=event_id,
            service_id=service_id,
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
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
    body: PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBody,
    incoming: bool | Unset = UNSET,
) -> Response[Any]:
    """Create a new service exchange request

     Creates a new service exchange request

    Args:
        person_id (int):  Example: 42.
        event_id (int):  Example: 42.
        service_id (str):
        incoming (bool | Unset):
        body (PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        event_id=event_id,
        service_id=service_id,
        body=body,
        incoming=incoming,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: int,
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBody,
    incoming: bool | Unset = UNSET,
) -> Response[Any]:
    """Create a new service exchange request

     Creates a new service exchange request

    Args:
        person_id (int):  Example: 42.
        event_id (int):  Example: 42.
        service_id (str):
        incoming (bool | Unset):
        body (PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        event_id=event_id,
        service_id=service_id,
        body=body,
        incoming=incoming,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
