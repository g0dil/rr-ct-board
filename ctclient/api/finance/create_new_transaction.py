from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_new_transaction_body import CreateNewTransactionBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateNewTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/finance/transactions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewTransactionBody,
) -> Response[Any]:
    """Create new transaction

    Args:
        body (CreateNewTransactionBody):  Example: {'accountId': 10, 'amount': 7812,
            'contraAccountId': 11, 'costCenterId': 12, 'documentDate': '2019-01-14', 'documentNumber':
            '4/4', 'donatorId': 13, 'donatorSpouseId': 14, 'note': 'This is a transaction'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewTransactionBody,
) -> Response[Any]:
    """Create new transaction

    Args:
        body (CreateNewTransactionBody):  Example: {'accountId': 10, 'amount': 7812,
            'contraAccountId': 11, 'costCenterId': 12, 'documentDate': '2019-01-14', 'documentNumber':
            '4/4', 'donatorId': 13, 'donatorSpouseId': 14, 'note': 'This is a transaction'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
