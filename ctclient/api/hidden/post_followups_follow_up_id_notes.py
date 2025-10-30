from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_followups_follow_up_id_notes_body import (
    PostFollowupsFollowUpIdNotesBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    follow_up_id: int,
    *,
    body: PostFollowupsFollowUpIdNotesBody,
    also_apply_to_person: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["also_apply_to_person"] = also_apply_to_person

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/followups/{follow_up_id}/notes".format(
            follow_up_id=follow_up_id,
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    follow_up_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFollowupsFollowUpIdNotesBody,
    also_apply_to_person: bool | Unset = UNSET,
) -> Response[Any | str]:
    """Add Note to follow-up

     Add note to follow up

    Args:
        follow_up_id (int):  Example: 2.
        also_apply_to_person (bool | Unset):  Example: True.
        body (PostFollowupsFollowUpIdNotesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        follow_up_id=follow_up_id,
        body=body,
        also_apply_to_person=also_apply_to_person,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    follow_up_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFollowupsFollowUpIdNotesBody,
    also_apply_to_person: bool | Unset = UNSET,
) -> Any | str | None:
    """Add Note to follow-up

     Add note to follow up

    Args:
        follow_up_id (int):  Example: 2.
        also_apply_to_person (bool | Unset):  Example: True.
        body (PostFollowupsFollowUpIdNotesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        follow_up_id=follow_up_id,
        client=client,
        body=body,
        also_apply_to_person=also_apply_to_person,
    ).parsed


async def asyncio_detailed(
    follow_up_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFollowupsFollowUpIdNotesBody,
    also_apply_to_person: bool | Unset = UNSET,
) -> Response[Any | str]:
    """Add Note to follow-up

     Add note to follow up

    Args:
        follow_up_id (int):  Example: 2.
        also_apply_to_person (bool | Unset):  Example: True.
        body (PostFollowupsFollowUpIdNotesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        follow_up_id=follow_up_id,
        body=body,
        also_apply_to_person=also_apply_to_person,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    follow_up_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFollowupsFollowUpIdNotesBody,
    also_apply_to_person: bool | Unset = UNSET,
) -> Any | str | None:
    """Add Note to follow-up

     Add note to follow up

    Args:
        follow_up_id (int):  Example: 2.
        also_apply_to_person (bool | Unset):  Example: True.
        body (PostFollowupsFollowUpIdNotesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            follow_up_id=follow_up_id,
            client=client,
            body=body,
            also_apply_to_person=also_apply_to_person,
        )
    ).parsed
