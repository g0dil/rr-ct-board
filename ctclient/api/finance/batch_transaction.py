from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_transaction_body import BatchTransactionBody
from ...models.batch_transaction_response_200 import BatchTransactionResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: BatchTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/finance/transactions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchTransactionResponse200 | None:
    if response.status_code == 200:
        response_200 = BatchTransactionResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BatchTransactionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchTransactionBody,
) -> Response[BatchTransactionResponse200]:
    """Transaction Batch Processing

     Batch API for Transactions. The batch API needs two informations sets. Firstly the `changeset`,
    which holds the information for the batch command. Either a field that needs to be updated or a
    trigger keyword to start a command. Secondly, a set of `filters`. Filters are either transaction
    filters, which resolve to a list of transaction IDs, or you can explicitly state a list of IDs to
    include or exclude from the batch command.

    Args:
        body (BatchTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchTransactionResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BatchTransactionBody,
) -> BatchTransactionResponse200 | None:
    """Transaction Batch Processing

     Batch API for Transactions. The batch API needs two informations sets. Firstly the `changeset`,
    which holds the information for the batch command. Either a field that needs to be updated or a
    trigger keyword to start a command. Secondly, a set of `filters`. Filters are either transaction
    filters, which resolve to a list of transaction IDs, or you can explicitly state a list of IDs to
    include or exclude from the batch command.

    Args:
        body (BatchTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchTransactionResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchTransactionBody,
) -> Response[BatchTransactionResponse200]:
    """Transaction Batch Processing

     Batch API for Transactions. The batch API needs two informations sets. Firstly the `changeset`,
    which holds the information for the batch command. Either a field that needs to be updated or a
    trigger keyword to start a command. Secondly, a set of `filters`. Filters are either transaction
    filters, which resolve to a list of transaction IDs, or you can explicitly state a list of IDs to
    include or exclude from the batch command.

    Args:
        body (BatchTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchTransactionResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BatchTransactionBody,
) -> BatchTransactionResponse200 | None:
    """Transaction Batch Processing

     Batch API for Transactions. The batch API needs two informations sets. Firstly the `changeset`,
    which holds the information for the batch command. Either a field that needs to be updated or a
    trigger keyword to start a command. Secondly, a set of `filters`. Filters are either transaction
    filters, which resolve to a list of transaction IDs, or you can explicitly state a list of IDs to
    include or exclude from the batch command.

    Args:
        body (BatchTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchTransactionResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
