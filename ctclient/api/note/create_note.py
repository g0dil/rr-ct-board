from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_note_body import CreateNoteBody
from ...models.create_note_domain_type import CreateNoteDomainType
from ...types import Response


def _get_kwargs(
    domain_type: CreateNoteDomainType,
    domain_id: int,
    *,
    body: CreateNoteBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/notes/{domain_type}/{domain_id}".format(
            domain_type=domain_type,
            domain_id=domain_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
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
) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_type: CreateNoteDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateNoteBody,
) -> Response[Any | str]:
    """Create a note

    Args:
        domain_type (CreateNoteDomainType): Domain types that notes can be used with Example:
            group.
        domain_id (int):  Example: 35.
        body (CreateNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_type: CreateNoteDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateNoteBody,
) -> Any | str | None:
    """Create a note

    Args:
        domain_type (CreateNoteDomainType): Domain types that notes can be used with Example:
            group.
        domain_id (int):  Example: 35.
        body (CreateNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        domain_type=domain_type,
        domain_id=domain_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    domain_type: CreateNoteDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateNoteBody,
) -> Response[Any | str]:
    """Create a note

    Args:
        domain_type (CreateNoteDomainType): Domain types that notes can be used with Example:
            group.
        domain_id (int):  Example: 35.
        body (CreateNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: CreateNoteDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateNoteBody,
) -> Any | str | None:
    """Create a note

    Args:
        domain_type (CreateNoteDomainType): Domain types that notes can be used with Example:
            group.
        domain_id (int):  Example: 35.
        body (CreateNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            domain_id=domain_id,
            client=client,
            body=body,
        )
    ).parsed
