from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_agenda_email_body import SendAgendaEmailBody
from ...models.send_agenda_email_response_200 import SendAgendaEmailResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: SendAgendaEmailBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agendas/send",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SendAgendaEmailResponse200 | str | None:
    if response.status_code == 200:
        response_200 = SendAgendaEmailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | SendAgendaEmailResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendAgendaEmailBody,
) -> Response[Any | SendAgendaEmailResponse200 | str]:
    """Send agenda email to recipients

     An agenda can be sent to multiple people at once. Recipients can be participants of one of the
    events, whereby the user sending the mail MUST see the service groups, or the user can add
    additional recipients from the list of people the user can see. To send a mail the user MUST see the
    agenda.

    Args:
        body (SendAgendaEmailBody):  Example: {'body': 'I have updated the agenda for the upcoming
            service. Please review the changes.', 'eventIds': [31, 32], 'recipients': [40, 41, 116],
            'sendCopyToMe': True, 'subject': 'Agenda Updated'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SendAgendaEmailResponse200 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SendAgendaEmailBody,
) -> Any | SendAgendaEmailResponse200 | str | None:
    """Send agenda email to recipients

     An agenda can be sent to multiple people at once. Recipients can be participants of one of the
    events, whereby the user sending the mail MUST see the service groups, or the user can add
    additional recipients from the list of people the user can see. To send a mail the user MUST see the
    agenda.

    Args:
        body (SendAgendaEmailBody):  Example: {'body': 'I have updated the agenda for the upcoming
            service. Please review the changes.', 'eventIds': [31, 32], 'recipients': [40, 41, 116],
            'sendCopyToMe': True, 'subject': 'Agenda Updated'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SendAgendaEmailResponse200 | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendAgendaEmailBody,
) -> Response[Any | SendAgendaEmailResponse200 | str]:
    """Send agenda email to recipients

     An agenda can be sent to multiple people at once. Recipients can be participants of one of the
    events, whereby the user sending the mail MUST see the service groups, or the user can add
    additional recipients from the list of people the user can see. To send a mail the user MUST see the
    agenda.

    Args:
        body (SendAgendaEmailBody):  Example: {'body': 'I have updated the agenda for the upcoming
            service. Please review the changes.', 'eventIds': [31, 32], 'recipients': [40, 41, 116],
            'sendCopyToMe': True, 'subject': 'Agenda Updated'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SendAgendaEmailResponse200 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SendAgendaEmailBody,
) -> Any | SendAgendaEmailResponse200 | str | None:
    """Send agenda email to recipients

     An agenda can be sent to multiple people at once. Recipients can be participants of one of the
    events, whereby the user sending the mail MUST see the service groups, or the user can add
    additional recipients from the list of people the user can see. To send a mail the user MUST see the
    agenda.

    Args:
        body (SendAgendaEmailBody):  Example: {'body': 'I have updated the agenda for the upcoming
            service. Please review the changes.', 'eventIds': [31, 32], 'recipients': [40, 41, 116],
            'sendCopyToMe': True, 'subject': 'Agenda Updated'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SendAgendaEmailResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
