from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_group_meetingtemplates_meeting_template_id_body import (
    PutGroupMeetingtemplatesMeetingTemplateIdBody,
)
from ...types import Response


def _get_kwargs(
    meeting_template_id: str,
    *,
    body: PutGroupMeetingtemplatesMeetingTemplateIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/group/meetingtemplates/{meeting_template_id}".format(
            meeting_template_id=meeting_template_id,
        ),
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
    meeting_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupMeetingtemplatesMeetingTemplateIdBody,
) -> Response[Any | str]:
    """Update group meeting template

    Args:
        meeting_template_id (str):
        body (PutGroupMeetingtemplatesMeetingTemplateIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        meeting_template_id=meeting_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    meeting_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupMeetingtemplatesMeetingTemplateIdBody,
) -> Any | str | None:
    """Update group meeting template

    Args:
        meeting_template_id (str):
        body (PutGroupMeetingtemplatesMeetingTemplateIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        meeting_template_id=meeting_template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    meeting_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupMeetingtemplatesMeetingTemplateIdBody,
) -> Response[Any | str]:
    """Update group meeting template

    Args:
        meeting_template_id (str):
        body (PutGroupMeetingtemplatesMeetingTemplateIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        meeting_template_id=meeting_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    meeting_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutGroupMeetingtemplatesMeetingTemplateIdBody,
) -> Any | str | None:
    """Update group meeting template

    Args:
        meeting_template_id (str):
        body (PutGroupMeetingtemplatesMeetingTemplateIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            meeting_template_id=meeting_template_id,
            client=client,
            body=body,
        )
    ).parsed
