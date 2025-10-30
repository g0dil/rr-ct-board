from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_donators_order_by import GetAllDonatorsOrderBy
from ...models.get_all_donators_order_direction import GetAllDonatorsOrderDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accounting_period_id: int,
    order_by: GetAllDonatorsOrderBy | Unset = UNSET,
    order_direction: GetAllDonatorsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    query: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accounting_period_id"] = accounting_period_id

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_order_direction: str | Unset = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["order_direction"] = json_order_direction

    params["page"] = page

    params["limit"] = limit

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/donators",
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
    accounting_period_id: int,
    order_by: GetAllDonatorsOrderBy | Unset = UNSET,
    order_direction: GetAllDonatorsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    query: str | Unset = UNSET,
) -> Response[Any | str]:
    """Get all donators including their donation information (e.g. donation amount)

    Args:
        accounting_period_id (int):  Example: 1.
        order_by (GetAllDonatorsOrderBy | Unset):
        order_direction (GetAllDonatorsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        order_by=order_by,
        order_direction=order_direction,
        page=page,
        limit=limit,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    order_by: GetAllDonatorsOrderBy | Unset = UNSET,
    order_direction: GetAllDonatorsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    query: str | Unset = UNSET,
) -> Any | str | None:
    """Get all donators including their donation information (e.g. donation amount)

    Args:
        accounting_period_id (int):  Example: 1.
        order_by (GetAllDonatorsOrderBy | Unset):
        order_direction (GetAllDonatorsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        accounting_period_id=accounting_period_id,
        order_by=order_by,
        order_direction=order_direction,
        page=page,
        limit=limit,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    order_by: GetAllDonatorsOrderBy | Unset = UNSET,
    order_direction: GetAllDonatorsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    query: str | Unset = UNSET,
) -> Response[Any | str]:
    """Get all donators including their donation information (e.g. donation amount)

    Args:
        accounting_period_id (int):  Example: 1.
        order_by (GetAllDonatorsOrderBy | Unset):
        order_direction (GetAllDonatorsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        order_by=order_by,
        order_direction=order_direction,
        page=page,
        limit=limit,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    order_by: GetAllDonatorsOrderBy | Unset = UNSET,
    order_direction: GetAllDonatorsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    query: str | Unset = UNSET,
) -> Any | str | None:
    """Get all donators including their donation information (e.g. donation amount)

    Args:
        accounting_period_id (int):  Example: 1.
        order_by (GetAllDonatorsOrderBy | Unset):
        order_direction (GetAllDonatorsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            accounting_period_id=accounting_period_id,
            order_by=order_by,
            order_direction=order_direction,
            page=page,
            limit=limit,
            query=query,
        )
    ).parsed
