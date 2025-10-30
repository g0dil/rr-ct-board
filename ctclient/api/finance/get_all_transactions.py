import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_transactions_include_item import GetAllTransactionsIncludeItem
from ...models.get_all_transactions_order_by import GetAllTransactionsOrderBy
from ...models.get_all_transactions_order_direction import (
    GetAllTransactionsOrderDirection,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accounting_period_id: int,
    created_pid: int | Unset = UNSET,
    cost_center_ids: list[int] | Unset = UNSET,
    donator_ids: list[int] | Unset = UNSET,
    include_ids: list[int] | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
    account_ids: list[int] | Unset = UNSET,
    is_donation: bool | Unset = UNSET,
    is_income: bool | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    is_immutable: bool | Unset = UNSET,
    order_by: GetAllTransactionsOrderBy | Unset = UNSET,
    order_direction: GetAllTransactionsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllTransactionsIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accounting_period_id"] = accounting_period_id

    params["created_pid"] = created_pid

    json_cost_center_ids: list[int] | Unset = UNSET
    if not isinstance(cost_center_ids, Unset):
        json_cost_center_ids = cost_center_ids

    params["cost_center_ids"] = json_cost_center_ids

    json_donator_ids: list[int] | Unset = UNSET
    if not isinstance(donator_ids, Unset):
        json_donator_ids = donator_ids

    params["donator_ids"] = json_donator_ids

    json_include_ids: list[int] | Unset = UNSET
    if not isinstance(include_ids, Unset):
        json_include_ids = include_ids

    params["include_ids"] = json_include_ids

    json_exclude_ids: list[int] | Unset = UNSET
    if not isinstance(exclude_ids, Unset):
        json_exclude_ids = exclude_ids

    params["exclude_ids"] = json_exclude_ids

    json_account_ids: list[int] | Unset = UNSET
    if not isinstance(account_ids, Unset):
        json_account_ids = account_ids

    params["account_ids"] = json_account_ids

    params["is_donation"] = is_donation

    params["is_income"] = is_income

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["is_immutable"] = is_immutable

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

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/transactions",
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
    created_pid: int | Unset = UNSET,
    cost_center_ids: list[int] | Unset = UNSET,
    donator_ids: list[int] | Unset = UNSET,
    include_ids: list[int] | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
    account_ids: list[int] | Unset = UNSET,
    is_donation: bool | Unset = UNSET,
    is_income: bool | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    is_immutable: bool | Unset = UNSET,
    order_by: GetAllTransactionsOrderBy | Unset = UNSET,
    order_direction: GetAllTransactionsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllTransactionsIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """Get all transaction

    Args:
        accounting_period_id (int):  Example: 1.
        created_pid (int | Unset):
        cost_center_ids (list[int] | Unset):
        donator_ids (list[int] | Unset):
        include_ids (list[int] | Unset):
        exclude_ids (list[int] | Unset):
        account_ids (list[int] | Unset):
        is_donation (bool | Unset):
        is_income (bool | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        is_immutable (bool | Unset):
        order_by (GetAllTransactionsOrderBy | Unset):
        order_direction (GetAllTransactionsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllTransactionsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        created_pid=created_pid,
        cost_center_ids=cost_center_ids,
        donator_ids=donator_ids,
        include_ids=include_ids,
        exclude_ids=exclude_ids,
        account_ids=account_ids,
        is_donation=is_donation,
        is_income=is_income,
        start_date=start_date,
        end_date=end_date,
        is_immutable=is_immutable,
        order_by=order_by,
        order_direction=order_direction,
        page=page,
        limit=limit,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    created_pid: int | Unset = UNSET,
    cost_center_ids: list[int] | Unset = UNSET,
    donator_ids: list[int] | Unset = UNSET,
    include_ids: list[int] | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
    account_ids: list[int] | Unset = UNSET,
    is_donation: bool | Unset = UNSET,
    is_income: bool | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    is_immutable: bool | Unset = UNSET,
    order_by: GetAllTransactionsOrderBy | Unset = UNSET,
    order_direction: GetAllTransactionsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllTransactionsIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """Get all transaction

    Args:
        accounting_period_id (int):  Example: 1.
        created_pid (int | Unset):
        cost_center_ids (list[int] | Unset):
        donator_ids (list[int] | Unset):
        include_ids (list[int] | Unset):
        exclude_ids (list[int] | Unset):
        account_ids (list[int] | Unset):
        is_donation (bool | Unset):
        is_income (bool | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        is_immutable (bool | Unset):
        order_by (GetAllTransactionsOrderBy | Unset):
        order_direction (GetAllTransactionsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllTransactionsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        accounting_period_id=accounting_period_id,
        created_pid=created_pid,
        cost_center_ids=cost_center_ids,
        donator_ids=donator_ids,
        include_ids=include_ids,
        exclude_ids=exclude_ids,
        account_ids=account_ids,
        is_donation=is_donation,
        is_income=is_income,
        start_date=start_date,
        end_date=end_date,
        is_immutable=is_immutable,
        order_by=order_by,
        order_direction=order_direction,
        page=page,
        limit=limit,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    created_pid: int | Unset = UNSET,
    cost_center_ids: list[int] | Unset = UNSET,
    donator_ids: list[int] | Unset = UNSET,
    include_ids: list[int] | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
    account_ids: list[int] | Unset = UNSET,
    is_donation: bool | Unset = UNSET,
    is_income: bool | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    is_immutable: bool | Unset = UNSET,
    order_by: GetAllTransactionsOrderBy | Unset = UNSET,
    order_direction: GetAllTransactionsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllTransactionsIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """Get all transaction

    Args:
        accounting_period_id (int):  Example: 1.
        created_pid (int | Unset):
        cost_center_ids (list[int] | Unset):
        donator_ids (list[int] | Unset):
        include_ids (list[int] | Unset):
        exclude_ids (list[int] | Unset):
        account_ids (list[int] | Unset):
        is_donation (bool | Unset):
        is_income (bool | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        is_immutable (bool | Unset):
        order_by (GetAllTransactionsOrderBy | Unset):
        order_direction (GetAllTransactionsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllTransactionsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        created_pid=created_pid,
        cost_center_ids=cost_center_ids,
        donator_ids=donator_ids,
        include_ids=include_ids,
        exclude_ids=exclude_ids,
        account_ids=account_ids,
        is_donation=is_donation,
        is_income=is_income,
        start_date=start_date,
        end_date=end_date,
        is_immutable=is_immutable,
        order_by=order_by,
        order_direction=order_direction,
        page=page,
        limit=limit,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    created_pid: int | Unset = UNSET,
    cost_center_ids: list[int] | Unset = UNSET,
    donator_ids: list[int] | Unset = UNSET,
    include_ids: list[int] | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
    account_ids: list[int] | Unset = UNSET,
    is_donation: bool | Unset = UNSET,
    is_income: bool | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    is_immutable: bool | Unset = UNSET,
    order_by: GetAllTransactionsOrderBy | Unset = UNSET,
    order_direction: GetAllTransactionsOrderDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllTransactionsIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """Get all transaction

    Args:
        accounting_period_id (int):  Example: 1.
        created_pid (int | Unset):
        cost_center_ids (list[int] | Unset):
        donator_ids (list[int] | Unset):
        include_ids (list[int] | Unset):
        exclude_ids (list[int] | Unset):
        account_ids (list[int] | Unset):
        is_donation (bool | Unset):
        is_income (bool | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        is_immutable (bool | Unset):
        order_by (GetAllTransactionsOrderBy | Unset):
        order_direction (GetAllTransactionsOrderDirection | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllTransactionsIncludeItem] | Unset):

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
            created_pid=created_pid,
            cost_center_ids=cost_center_ids,
            donator_ids=donator_ids,
            include_ids=include_ids,
            exclude_ids=exclude_ids,
            account_ids=account_ids,
            is_donation=is_donation,
            is_income=is_income,
            start_date=start_date,
            end_date=end_date,
            is_immutable=is_immutable,
            order_by=order_by,
            order_direction=order_direction,
            page=page,
            limit=limit,
            include=include,
        )
    ).parsed
