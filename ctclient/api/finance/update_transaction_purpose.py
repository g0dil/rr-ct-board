from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_transaction_purpose_body import UpdateTransactionPurposeBody
from ...models.update_transaction_purpose_response_200 import (
    UpdateTransactionPurposeResponse200,
)
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: UpdateTransactionPurposeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/finance/transactionpurposes/{id}".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateTransactionPurposeResponse200 | str | None:
    if response.status_code == 200:
        response_200 = UpdateTransactionPurposeResponse200.from_dict(response.json())

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
) -> Response[Any | UpdateTransactionPurposeResponse200 | str]:
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
    body: UpdateTransactionPurposeBody,
) -> Response[Any | UpdateTransactionPurposeResponse200 | str]:
    """Update transaction purpose

    Args:
        id (int):  Example: 1.
        body (UpdateTransactionPurposeBody):  Example: {'accountIds': [4, 5, 6], 'costCenterId':
            5, 'isIncome': True, 'name': 'Für was steht der Zweck nochmal?', 'purposeAccountId': 6,
            'sortKey': 7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateTransactionPurposeResponse200 | str]
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
    body: UpdateTransactionPurposeBody,
) -> Any | UpdateTransactionPurposeResponse200 | str | None:
    """Update transaction purpose

    Args:
        id (int):  Example: 1.
        body (UpdateTransactionPurposeBody):  Example: {'accountIds': [4, 5, 6], 'costCenterId':
            5, 'isIncome': True, 'name': 'Für was steht der Zweck nochmal?', 'purposeAccountId': 6,
            'sortKey': 7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateTransactionPurposeResponse200 | str
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
    body: UpdateTransactionPurposeBody,
) -> Response[Any | UpdateTransactionPurposeResponse200 | str]:
    """Update transaction purpose

    Args:
        id (int):  Example: 1.
        body (UpdateTransactionPurposeBody):  Example: {'accountIds': [4, 5, 6], 'costCenterId':
            5, 'isIncome': True, 'name': 'Für was steht der Zweck nochmal?', 'purposeAccountId': 6,
            'sortKey': 7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateTransactionPurposeResponse200 | str]
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
    body: UpdateTransactionPurposeBody,
) -> Any | UpdateTransactionPurposeResponse200 | str | None:
    """Update transaction purpose

    Args:
        id (int):  Example: 1.
        body (UpdateTransactionPurposeBody):  Example: {'accountIds': [4, 5, 6], 'costCenterId':
            5, 'isIncome': True, 'name': 'Für was steht der Zweck nochmal?', 'purposeAccountId': 6,
            'sortKey': 7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateTransactionPurposeResponse200 | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
