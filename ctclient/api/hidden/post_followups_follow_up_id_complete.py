from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_followups_follow_up_id_complete_body import (
    PostFollowupsFollowUpIdCompleteBody,
)
from ...models.post_followups_follow_up_id_complete_response_200 import (
    PostFollowupsFollowUpIdCompleteResponse200,
)
from ...types import Response


def _get_kwargs(
    follow_up_id: int,
    *,
    body: PostFollowupsFollowUpIdCompleteBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/followups/{follow_up_id}/complete".format(
            follow_up_id=follow_up_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFollowupsFollowUpIdCompleteResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PostFollowupsFollowUpIdCompleteResponse200.from_dict(
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
) -> Response[Any | PostFollowupsFollowUpIdCompleteResponse200 | str]:
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
    body: PostFollowupsFollowUpIdCompleteBody,
) -> Response[Any | PostFollowupsFollowUpIdCompleteResponse200 | str]:
    """Complete follow-up

     Completes the specified follow-up.

    Args:
        follow_up_id (int):  Example: 2.
        body (PostFollowupsFollowUpIdCompleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFollowupsFollowUpIdCompleteResponse200 | str]
    """

    kwargs = _get_kwargs(
        follow_up_id=follow_up_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    follow_up_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFollowupsFollowUpIdCompleteBody,
) -> Any | PostFollowupsFollowUpIdCompleteResponse200 | str | None:
    """Complete follow-up

     Completes the specified follow-up.

    Args:
        follow_up_id (int):  Example: 2.
        body (PostFollowupsFollowUpIdCompleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFollowupsFollowUpIdCompleteResponse200 | str
    """

    return sync_detailed(
        follow_up_id=follow_up_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    follow_up_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFollowupsFollowUpIdCompleteBody,
) -> Response[Any | PostFollowupsFollowUpIdCompleteResponse200 | str]:
    """Complete follow-up

     Completes the specified follow-up.

    Args:
        follow_up_id (int):  Example: 2.
        body (PostFollowupsFollowUpIdCompleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFollowupsFollowUpIdCompleteResponse200 | str]
    """

    kwargs = _get_kwargs(
        follow_up_id=follow_up_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    follow_up_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFollowupsFollowUpIdCompleteBody,
) -> Any | PostFollowupsFollowUpIdCompleteResponse200 | str | None:
    """Complete follow-up

     Completes the specified follow-up.

    Args:
        follow_up_id (int):  Example: 2.
        body (PostFollowupsFollowUpIdCompleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFollowupsFollowUpIdCompleteResponse200 | str
    """

    return (
        await asyncio_detailed(
            follow_up_id=follow_up_id,
            client=client,
            body=body,
        )
    ).parsed
