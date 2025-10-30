from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_tax_rates_response_200 import GetAllTaxRatesResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    accounting_period_id: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accounting_period_id"] = accounting_period_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/taxrates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAllTaxRatesResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetAllTaxRatesResponse200.from_dict(response.json())

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
) -> Response[Any | GetAllTaxRatesResponse200 | str]:
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
) -> Response[Any | GetAllTaxRatesResponse200 | str]:
    """Get all tax rates ordered by id

    Args:
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllTaxRatesResponse200 | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
) -> Any | GetAllTaxRatesResponse200 | str | None:
    """Get all tax rates ordered by id

    Args:
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllTaxRatesResponse200 | str
    """

    return sync_detailed(
        client=client,
        accounting_period_id=accounting_period_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
) -> Response[Any | GetAllTaxRatesResponse200 | str]:
    """Get all tax rates ordered by id

    Args:
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllTaxRatesResponse200 | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
) -> Any | GetAllTaxRatesResponse200 | str | None:
    """Get all tax rates ordered by id

    Args:
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllTaxRatesResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            accounting_period_id=accounting_period_id,
        )
    ).parsed
