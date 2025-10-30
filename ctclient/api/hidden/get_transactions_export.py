from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_transactions_export_target import GetTransactionsExportTarget
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 10,
    order_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    accounting_period_id: str | Unset = UNSET,
    target: GetTransactionsExportTarget | Unset = UNSET,
    page: int | Unset = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["order_by"] = order_by

    params["direction"] = direction

    params["accounting_period_id"] = accounting_period_id

    json_target: str | Unset = UNSET
    if not isinstance(target, Unset):
        json_target = target.value

    params["target"] = json_target

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/transactions/export",
        "params": params,
    }

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
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    order_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    accounting_period_id: str | Unset = UNSET,
    target: GetTransactionsExportTarget | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[Any | str]:
    """TODO 200

    Args:
        limit (int | Unset):  Default: 10. Example: 10.
        order_by (str | Unset):
        direction (str | Unset):
        accounting_period_id (str | Unset):
        target (GetTransactionsExportTarget | Unset):
        page (int | Unset):  Default: 1. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        order_by=order_by,
        direction=direction,
        accounting_period_id=accounting_period_id,
        target=target,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    order_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    accounting_period_id: str | Unset = UNSET,
    target: GetTransactionsExportTarget | Unset = UNSET,
    page: int | Unset = 1,
) -> Any | str | None:
    """TODO 200

    Args:
        limit (int | Unset):  Default: 10. Example: 10.
        order_by (str | Unset):
        direction (str | Unset):
        accounting_period_id (str | Unset):
        target (GetTransactionsExportTarget | Unset):
        page (int | Unset):  Default: 1. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        limit=limit,
        order_by=order_by,
        direction=direction,
        accounting_period_id=accounting_period_id,
        target=target,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    order_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    accounting_period_id: str | Unset = UNSET,
    target: GetTransactionsExportTarget | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[Any | str]:
    """TODO 200

    Args:
        limit (int | Unset):  Default: 10. Example: 10.
        order_by (str | Unset):
        direction (str | Unset):
        accounting_period_id (str | Unset):
        target (GetTransactionsExportTarget | Unset):
        page (int | Unset):  Default: 1. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        order_by=order_by,
        direction=direction,
        accounting_period_id=accounting_period_id,
        target=target,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    order_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    accounting_period_id: str | Unset = UNSET,
    target: GetTransactionsExportTarget | Unset = UNSET,
    page: int | Unset = 1,
) -> Any | str | None:
    """TODO 200

    Args:
        limit (int | Unset):  Default: 10. Example: 10.
        order_by (str | Unset):
        direction (str | Unset):
        accounting_period_id (str | Unset):
        target (GetTransactionsExportTarget | Unset):
        page (int | Unset):  Default: 1. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            order_by=order_by,
            direction=direction,
            accounting_period_id=accounting_period_id,
            target=target,
            page=page,
        )
    ).parsed
