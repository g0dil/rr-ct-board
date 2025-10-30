from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_account_body import UpdateAccountBody
from ...models.update_account_response_200 import UpdateAccountResponse200
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: UpdateAccountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/finance/accounts/{id}".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateAccountResponse200 | str | None:
    if response.status_code == 200:
        response_200 = UpdateAccountResponse200.from_dict(response.json())

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
) -> Response[Any | UpdateAccountResponse200 | str]:
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
    body: UpdateAccountBody,
) -> Response[Any | UpdateAccountResponse200 | str]:
    """Update account

    Args:
        id (int):  Example: 1.
        body (UpdateAccountBody):  Example: {'accountGroupId': 4, 'budget': 100000, 'example':
            'Donations', 'identifier': 'DE12345678901234567890', 'isDonationAccount': False,
            'isOpeningBalanceAccount': False, 'name': 'the new donations account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateAccountResponse200 | str]
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
    body: UpdateAccountBody,
) -> Any | UpdateAccountResponse200 | str | None:
    """Update account

    Args:
        id (int):  Example: 1.
        body (UpdateAccountBody):  Example: {'accountGroupId': 4, 'budget': 100000, 'example':
            'Donations', 'identifier': 'DE12345678901234567890', 'isDonationAccount': False,
            'isOpeningBalanceAccount': False, 'name': 'the new donations account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateAccountResponse200 | str
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
    body: UpdateAccountBody,
) -> Response[Any | UpdateAccountResponse200 | str]:
    """Update account

    Args:
        id (int):  Example: 1.
        body (UpdateAccountBody):  Example: {'accountGroupId': 4, 'budget': 100000, 'example':
            'Donations', 'identifier': 'DE12345678901234567890', 'isDonationAccount': False,
            'isOpeningBalanceAccount': False, 'name': 'the new donations account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateAccountResponse200 | str]
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
    body: UpdateAccountBody,
) -> Any | UpdateAccountResponse200 | str | None:
    """Update account

    Args:
        id (int):  Example: 1.
        body (UpdateAccountBody):  Example: {'accountGroupId': 4, 'budget': 100000, 'example':
            'Donations', 'identifier': 'DE12345678901234567890', 'isDonationAccount': False,
            'isOpeningBalanceAccount': False, 'name': 'the new donations account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateAccountResponse200 | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
