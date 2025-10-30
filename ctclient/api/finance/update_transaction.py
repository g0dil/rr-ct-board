from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_transaction_body import UpdateTransactionBody
from ...models.update_transaction_include_item import UpdateTransactionIncludeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: UpdateTransactionBody,
    include: list[UpdateTransactionIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/finance/transactions/{id}".format(
            id=id,
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTransactionBody,
    include: list[UpdateTransactionIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """Update transaction

    Args:
        id (int):  Example: 1.
        include (list[UpdateTransactionIncludeItem] | Unset):
        body (UpdateTransactionBody):  Example: {'accountId': 10, 'amount': 7812,
            'contraAccountId': 11, 'costCenterId': 12, 'documentDate': '2019-01-14', 'documentNumber':
            '4/4', 'donatorId': 13, 'isImmutable': False, 'note': 'This is a transaction'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTransactionBody,
    include: list[UpdateTransactionIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """Update transaction

    Args:
        id (int):  Example: 1.
        include (list[UpdateTransactionIncludeItem] | Unset):
        body (UpdateTransactionBody):  Example: {'accountId': 10, 'amount': 7812,
            'contraAccountId': 11, 'costCenterId': 12, 'documentDate': '2019-01-14', 'documentNumber':
            '4/4', 'donatorId': 13, 'isImmutable': False, 'note': 'This is a transaction'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        include=include,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTransactionBody,
    include: list[UpdateTransactionIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """Update transaction

    Args:
        id (int):  Example: 1.
        include (list[UpdateTransactionIncludeItem] | Unset):
        body (UpdateTransactionBody):  Example: {'accountId': 10, 'amount': 7812,
            'contraAccountId': 11, 'costCenterId': 12, 'documentDate': '2019-01-14', 'documentNumber':
            '4/4', 'donatorId': 13, 'isImmutable': False, 'note': 'This is a transaction'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTransactionBody,
    include: list[UpdateTransactionIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """Update transaction

    Args:
        id (int):  Example: 1.
        include (list[UpdateTransactionIncludeItem] | Unset):
        body (UpdateTransactionBody):  Example: {'accountId': 10, 'amount': 7812,
            'contraAccountId': 11, 'costCenterId': 12, 'documentDate': '2019-01-14', 'documentNumber':
            '4/4', 'donatorId': 13, 'isImmutable': False, 'note': 'This is a transaction'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            include=include,
        )
    ).parsed
