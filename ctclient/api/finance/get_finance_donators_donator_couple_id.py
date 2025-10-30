from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_finance_donators_donator_couple_id_response_200 import (
    GetFinanceDonatorsDonatorCoupleIdResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    donator_couple_id: str,
    *,
    accounting_period_id: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accounting_period_id"] = accounting_period_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/donators/{donator_couple_id}/receipts".format(
            donator_couple_id=donator_couple_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetFinanceDonatorsDonatorCoupleIdResponse200.from_dict(
            response.json()
        )

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
) -> Response[Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    donator_couple_id: str,
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
) -> Response[Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str]:
    """Get donation receipt PDFs (cover letter and attachment)

     Get the donation receipts of a particular donator

    Args:
        donator_couple_id (str):  Example: 42-43.
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        donator_couple_id=donator_couple_id,
        accounting_period_id=accounting_period_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    donator_couple_id: str,
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
) -> Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str | None:
    """Get donation receipt PDFs (cover letter and attachment)

     Get the donation receipts of a particular donator

    Args:
        donator_couple_id (str):  Example: 42-43.
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str
    """

    return sync_detailed(
        donator_couple_id=donator_couple_id,
        client=client,
        accounting_period_id=accounting_period_id,
    ).parsed


async def asyncio_detailed(
    donator_couple_id: str,
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
) -> Response[Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str]:
    """Get donation receipt PDFs (cover letter and attachment)

     Get the donation receipts of a particular donator

    Args:
        donator_couple_id (str):  Example: 42-43.
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        donator_couple_id=donator_couple_id,
        accounting_period_id=accounting_period_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    donator_couple_id: str,
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
) -> Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str | None:
    """Get donation receipt PDFs (cover letter and attachment)

     Get the donation receipts of a particular donator

    Args:
        donator_couple_id (str):  Example: 42-43.
        accounting_period_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFinanceDonatorsDonatorCoupleIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            donator_couple_id=donator_couple_id,
            client=client,
            accounting_period_id=accounting_period_id,
        )
    ).parsed
