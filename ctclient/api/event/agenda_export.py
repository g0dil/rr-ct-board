from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agenda_export_body import AgendaExportBody
from ...models.agenda_export_response_200 import AgendaExportResponse200
from ...models.agenda_export_target import AgendaExportTarget
from ...types import UNSET, Response


def _get_kwargs(
    agenda_id: str,
    *,
    body: AgendaExportBody,
    target: AgendaExportTarget,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_target = target.value
    params["target"] = json_target

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agendas/{agenda_id}/export".format(
            agenda_id=agenda_id,
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgendaExportResponse200 | Any | str | None:
    if response.status_code == 200:
        response_200 = AgendaExportResponse200.from_dict(response.json())

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
) -> Response[AgendaExportResponse200 | Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agenda_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgendaExportBody,
    target: AgendaExportTarget,
) -> Response[AgendaExportResponse200 | Any | str]:
    """Exports the agenda

     Exports the agenda as zip file for imports in presenter-programs

    Args:
        agenda_id (str):
        target (AgendaExportTarget):
        body (AgendaExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgendaExportResponse200 | Any | str]
    """

    kwargs = _get_kwargs(
        agenda_id=agenda_id,
        body=body,
        target=target,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agenda_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgendaExportBody,
    target: AgendaExportTarget,
) -> AgendaExportResponse200 | Any | str | None:
    """Exports the agenda

     Exports the agenda as zip file for imports in presenter-programs

    Args:
        agenda_id (str):
        target (AgendaExportTarget):
        body (AgendaExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgendaExportResponse200 | Any | str
    """

    return sync_detailed(
        agenda_id=agenda_id,
        client=client,
        body=body,
        target=target,
    ).parsed


async def asyncio_detailed(
    agenda_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgendaExportBody,
    target: AgendaExportTarget,
) -> Response[AgendaExportResponse200 | Any | str]:
    """Exports the agenda

     Exports the agenda as zip file for imports in presenter-programs

    Args:
        agenda_id (str):
        target (AgendaExportTarget):
        body (AgendaExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgendaExportResponse200 | Any | str]
    """

    kwargs = _get_kwargs(
        agenda_id=agenda_id,
        body=body,
        target=target,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agenda_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgendaExportBody,
    target: AgendaExportTarget,
) -> AgendaExportResponse200 | Any | str | None:
    """Exports the agenda

     Exports the agenda as zip file for imports in presenter-programs

    Args:
        agenda_id (str):
        target (AgendaExportTarget):
        body (AgendaExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgendaExportResponse200 | Any | str
    """

    return (
        await asyncio_detailed(
            agenda_id=agenda_id,
            client=client,
            body=body,
            target=target,
        )
    ).parsed
