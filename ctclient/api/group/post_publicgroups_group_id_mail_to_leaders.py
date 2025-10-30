from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_publicgroups_group_id_mail_to_leaders_body import (
    PostPublicgroupsGroupIdMailToLeadersBody,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    body: PostPublicgroupsGroupIdMailToLeadersBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/publicgroups/{group_id}/mailToLeaders".format(
            group_id=group_id,
        ),
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

    if response.status_code == 400:
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
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostPublicgroupsGroupIdMailToLeadersBody,
) -> Response[Any]:
    """Send a Mail to Public Group Leaders

     Sends a mail to each group leader of the public group who has an email address set.

    Args:
        group_id (str):
        body (PostPublicgroupsGroupIdMailToLeadersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostPublicgroupsGroupIdMailToLeadersBody,
) -> Response[Any]:
    """Send a Mail to Public Group Leaders

     Sends a mail to each group leader of the public group who has an email address set.

    Args:
        group_id (str):
        body (PostPublicgroupsGroupIdMailToLeadersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
