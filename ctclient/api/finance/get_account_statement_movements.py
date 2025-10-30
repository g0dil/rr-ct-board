from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_account_statement_movements_include_item import (
    GetAccountStatementMovementsIncludeItem,
)
from ...models.get_account_statement_movements_state import (
    GetAccountStatementMovementsState,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    account_id: str,
    statement_id: str,
    *,
    state: GetAccountStatementMovementsState | Unset = UNSET,
    include: list[GetAccountStatementMovementsIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

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
        "url": "/finance/accountingperiods/{id}/accounts/{account_id}/statements/{statement_id}/movements".format(
            id=id,
            account_id=account_id,
            statement_id=statement_id,
        ),
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
    id: int,
    account_id: str,
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: GetAccountStatementMovementsState | Unset = UNSET,
    include: list[GetAccountStatementMovementsIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """
    Args:
        id (int):  Example: 1.
        account_id (str):
        statement_id (str):
        state (GetAccountStatementMovementsState | Unset):
        include (list[GetAccountStatementMovementsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        id=id,
        account_id=account_id,
        statement_id=statement_id,
        state=state,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    account_id: str,
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: GetAccountStatementMovementsState | Unset = UNSET,
    include: list[GetAccountStatementMovementsIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """
    Args:
        id (int):  Example: 1.
        account_id (str):
        statement_id (str):
        state (GetAccountStatementMovementsState | Unset):
        include (list[GetAccountStatementMovementsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        id=id,
        account_id=account_id,
        statement_id=statement_id,
        client=client,
        state=state,
        include=include,
    ).parsed


async def asyncio_detailed(
    id: int,
    account_id: str,
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: GetAccountStatementMovementsState | Unset = UNSET,
    include: list[GetAccountStatementMovementsIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """
    Args:
        id (int):  Example: 1.
        account_id (str):
        statement_id (str):
        state (GetAccountStatementMovementsState | Unset):
        include (list[GetAccountStatementMovementsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        id=id,
        account_id=account_id,
        statement_id=statement_id,
        state=state,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    account_id: str,
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: GetAccountStatementMovementsState | Unset = UNSET,
    include: list[GetAccountStatementMovementsIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """
    Args:
        id (int):  Example: 1.
        account_id (str):
        statement_id (str):
        state (GetAccountStatementMovementsState | Unset):
        include (list[GetAccountStatementMovementsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            id=id,
            account_id=account_id,
            statement_id=statement_id,
            client=client,
            state=state,
            include=include,
        )
    ).parsed
