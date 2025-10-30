from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_accounts_response_200 import GetAllAccountsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accounting_period_id: list[int],
    calculate_balance: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_accounting_period_id = accounting_period_id

    params["accounting_period_id"] = json_accounting_period_id

    params["calculate_balance"] = calculate_balance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAllAccountsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetAllAccountsResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Any | GetAllAccountsResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: list[int],
    calculate_balance: bool | Unset = UNSET,
) -> Response[Any | GetAllAccountsResponse200 | str]:
    """Get all accounts ordered by accounting period and number

    Args:
        accounting_period_id (list[int]):
        calculate_balance (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllAccountsResponse200 | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        calculate_balance=calculate_balance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: list[int],
    calculate_balance: bool | Unset = UNSET,
) -> Any | GetAllAccountsResponse200 | str | None:
    """Get all accounts ordered by accounting period and number

    Args:
        accounting_period_id (list[int]):
        calculate_balance (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllAccountsResponse200 | str
    """

    return sync_detailed(
        client=client,
        accounting_period_id=accounting_period_id,
        calculate_balance=calculate_balance,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: list[int],
    calculate_balance: bool | Unset = UNSET,
) -> Response[Any | GetAllAccountsResponse200 | str]:
    """Get all accounts ordered by accounting period and number

    Args:
        accounting_period_id (list[int]):
        calculate_balance (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllAccountsResponse200 | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        calculate_balance=calculate_balance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: list[int],
    calculate_balance: bool | Unset = UNSET,
) -> Any | GetAllAccountsResponse200 | str | None:
    """Get all accounts ordered by accounting period and number

    Args:
        accounting_period_id (list[int]):
        calculate_balance (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllAccountsResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            accounting_period_id=accounting_period_id,
            calculate_balance=calculate_balance,
        )
    ).parsed
