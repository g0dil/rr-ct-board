from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_accounting_period_body import UpdateAccountingPeriodBody
from ...models.update_accounting_period_response_200 import (
    UpdateAccountingPeriodResponse200,
)
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: UpdateAccountingPeriodBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/finance/accountingperiods/{id}".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateAccountingPeriodResponse200 | str | None:
    if response.status_code == 200:
        response_200 = UpdateAccountingPeriodResponse200.from_dict(response.json())

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
) -> Response[Any | UpdateAccountingPeriodResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAccountingPeriodBody,
) -> Response[Any | UpdateAccountingPeriodResponse200 | str]:
    """Update accounting period

    Args:
        id (int):  Example: 1.
        body (UpdateAccountingPeriodBody):  Example: {'clientId': 2, 'endDate': '2019-12-31',
            'isClosed': False, 'setImmutable': False, 'startDate': '2019-01-01'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateAccountingPeriodResponse200 | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAccountingPeriodBody,
) -> Any | UpdateAccountingPeriodResponse200 | str | None:
    """Update accounting period

    Args:
        id (int):  Example: 1.
        body (UpdateAccountingPeriodBody):  Example: {'clientId': 2, 'endDate': '2019-12-31',
            'isClosed': False, 'setImmutable': False, 'startDate': '2019-01-01'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateAccountingPeriodResponse200 | str
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAccountingPeriodBody,
) -> Response[Any | UpdateAccountingPeriodResponse200 | str]:
    """Update accounting period

    Args:
        id (int):  Example: 1.
        body (UpdateAccountingPeriodBody):  Example: {'clientId': 2, 'endDate': '2019-12-31',
            'isClosed': False, 'setImmutable': False, 'startDate': '2019-01-01'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateAccountingPeriodResponse200 | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAccountingPeriodBody,
) -> Any | UpdateAccountingPeriodResponse200 | str | None:
    """Update accounting period

    Args:
        id (int):  Example: 1.
        body (UpdateAccountingPeriodBody):  Example: {'clientId': 2, 'endDate': '2019-12-31',
            'isClosed': False, 'setImmutable': False, 'startDate': '2019-01-01'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateAccountingPeriodResponse200 | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
