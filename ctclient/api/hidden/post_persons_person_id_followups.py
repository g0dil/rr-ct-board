from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_persons_person_id_followups_body import (
    PostPersonsPersonIdFollowupsBody,
)
from ...models.post_persons_person_id_followups_response_201 import (
    PostPersonsPersonIdFollowupsResponse201,
)
from ...types import Response


def _get_kwargs(
    person_id: int,
    *,
    body: PostPersonsPersonIdFollowupsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/persons/{person_id}/followups".format(
            person_id=person_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostPersonsPersonIdFollowupsResponse201 | str | None:
    if response.status_code == 201:
        response_201 = PostPersonsPersonIdFollowupsResponse201.from_dict(
            response.json()
        )

        return response_201

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
) -> Response[Any | PostPersonsPersonIdFollowupsResponse201 | str]:
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
    body: PostPersonsPersonIdFollowupsBody,
) -> Response[Any | PostPersonsPersonIdFollowupsResponse201 | str]:
    """Create follow-up

     Create a follow-up for the specified person.

    Args:
        person_id (int):  Example: 42.
        body (PostPersonsPersonIdFollowupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPersonsPersonIdFollowupsResponse201 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostPersonsPersonIdFollowupsBody,
) -> Any | PostPersonsPersonIdFollowupsResponse201 | str | None:
    """Create follow-up

     Create a follow-up for the specified person.

    Args:
        person_id (int):  Example: 42.
        body (PostPersonsPersonIdFollowupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPersonsPersonIdFollowupsResponse201 | str
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostPersonsPersonIdFollowupsBody,
) -> Response[Any | PostPersonsPersonIdFollowupsResponse201 | str]:
    """Create follow-up

     Create a follow-up for the specified person.

    Args:
        person_id (int):  Example: 42.
        body (PostPersonsPersonIdFollowupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPersonsPersonIdFollowupsResponse201 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostPersonsPersonIdFollowupsBody,
) -> Any | PostPersonsPersonIdFollowupsResponse201 | str | None:
    """Create follow-up

     Create a follow-up for the specified person.

    Args:
        person_id (int):  Example: 42.
        body (PostPersonsPersonIdFollowupsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPersonsPersonIdFollowupsResponse201 | str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed
