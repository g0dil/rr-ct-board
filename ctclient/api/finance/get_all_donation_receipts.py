from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_donation_receipts_cleardoublepage import (
    GetAllDonationReceiptsCleardoublepage,
)
from ...models.get_all_donation_receipts_mode import GetAllDonationReceiptsMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accounting_period_id: int,
    mode: GetAllDonationReceiptsMode | Unset = GetAllDonationReceiptsMode.TWOFILES,
    cleardoublepage: GetAllDonationReceiptsCleardoublepage
    | Unset = GetAllDonationReceiptsCleardoublepage.NONE,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accounting_period_id"] = accounting_period_id

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    json_cleardoublepage: str | Unset = UNSET
    if not isinstance(cleardoublepage, Unset):
        json_cleardoublepage = cleardoublepage.value

    params["cleardoublepage"] = json_cleardoublepage

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/donators/receipts",
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
    mode: GetAllDonationReceiptsMode | Unset = GetAllDonationReceiptsMode.TWOFILES,
    cleardoublepage: GetAllDonationReceiptsCleardoublepage
    | Unset = GetAllDonationReceiptsCleardoublepage.NONE,
) -> Response[Any | str]:
    """Get all donators including their donation information (e.g. donation amount)

     Download all donation receipts.

    Args:
        accounting_period_id (int):  Example: 1.
        mode (GetAllDonationReceiptsMode | Unset):  Default: GetAllDonationReceiptsMode.TWOFILES.
        cleardoublepage (GetAllDonationReceiptsCleardoublepage | Unset):  Default:
            GetAllDonationReceiptsCleardoublepage.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        mode=mode,
        cleardoublepage=cleardoublepage,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    mode: GetAllDonationReceiptsMode | Unset = GetAllDonationReceiptsMode.TWOFILES,
    cleardoublepage: GetAllDonationReceiptsCleardoublepage
    | Unset = GetAllDonationReceiptsCleardoublepage.NONE,
) -> Any | str | None:
    """Get all donators including their donation information (e.g. donation amount)

     Download all donation receipts.

    Args:
        accounting_period_id (int):  Example: 1.
        mode (GetAllDonationReceiptsMode | Unset):  Default: GetAllDonationReceiptsMode.TWOFILES.
        cleardoublepage (GetAllDonationReceiptsCleardoublepage | Unset):  Default:
            GetAllDonationReceiptsCleardoublepage.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        accounting_period_id=accounting_period_id,
        mode=mode,
        cleardoublepage=cleardoublepage,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    mode: GetAllDonationReceiptsMode | Unset = GetAllDonationReceiptsMode.TWOFILES,
    cleardoublepage: GetAllDonationReceiptsCleardoublepage
    | Unset = GetAllDonationReceiptsCleardoublepage.NONE,
) -> Response[Any | str]:
    """Get all donators including their donation information (e.g. donation amount)

     Download all donation receipts.

    Args:
        accounting_period_id (int):  Example: 1.
        mode (GetAllDonationReceiptsMode | Unset):  Default: GetAllDonationReceiptsMode.TWOFILES.
        cleardoublepage (GetAllDonationReceiptsCleardoublepage | Unset):  Default:
            GetAllDonationReceiptsCleardoublepage.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        accounting_period_id=accounting_period_id,
        mode=mode,
        cleardoublepage=cleardoublepage,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accounting_period_id: int,
    mode: GetAllDonationReceiptsMode | Unset = GetAllDonationReceiptsMode.TWOFILES,
    cleardoublepage: GetAllDonationReceiptsCleardoublepage
    | Unset = GetAllDonationReceiptsCleardoublepage.NONE,
) -> Any | str | None:
    """Get all donators including their donation information (e.g. donation amount)

     Download all donation receipts.

    Args:
        accounting_period_id (int):  Example: 1.
        mode (GetAllDonationReceiptsMode | Unset):  Default: GetAllDonationReceiptsMode.TWOFILES.
        cleardoublepage (GetAllDonationReceiptsCleardoublepage | Unset):  Default:
            GetAllDonationReceiptsCleardoublepage.NONE.

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
            mode=mode,
            cleardoublepage=cleardoublepage,
        )
    ).parsed
