from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_new_account_body import CreateNewAccountBody
from ...models.create_new_account_response_200 import CreateNewAccountResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: CreateNewAccountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/finance/accounts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateNewAccountResponse200 | str | None:
    if response.status_code == 200:
        response_200 = CreateNewAccountResponse200.from_dict(response.json())

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
) -> Response[Any | CreateNewAccountResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewAccountBody,
) -> Response[Any | CreateNewAccountResponse200 | str]:
    """Create new account

    Args:
        body (CreateNewAccountBody):  Example: {'accountGroupId': 4, 'accountingPeriodId': 5,
            'budget': 1000000, 'example': 'Donations', 'identifier': 'DE12345678901234567890',
            'isDonationAccount': False, 'isOpeningBalanceAccount': False, 'name': 'the new donations
            account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewAccountResponse200 | str]
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
    body: CreateNewAccountBody,
) -> Any | CreateNewAccountResponse200 | str | None:
    """Create new account

    Args:
        body (CreateNewAccountBody):  Example: {'accountGroupId': 4, 'accountingPeriodId': 5,
            'budget': 1000000, 'example': 'Donations', 'identifier': 'DE12345678901234567890',
            'isDonationAccount': False, 'isOpeningBalanceAccount': False, 'name': 'the new donations
            account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewAccountResponse200 | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewAccountBody,
) -> Response[Any | CreateNewAccountResponse200 | str]:
    """Create new account

    Args:
        body (CreateNewAccountBody):  Example: {'accountGroupId': 4, 'accountingPeriodId': 5,
            'budget': 1000000, 'example': 'Donations', 'identifier': 'DE12345678901234567890',
            'isDonationAccount': False, 'isOpeningBalanceAccount': False, 'name': 'the new donations
            account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewAccountResponse200 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewAccountBody,
) -> Any | CreateNewAccountResponse200 | str | None:
    """Create new account

    Args:
        body (CreateNewAccountBody):  Example: {'accountGroupId': 4, 'accountingPeriodId': 5,
            'budget': 1000000, 'example': 'Donations', 'identifier': 'DE12345678901234567890',
            'isDonationAccount': False, 'isOpeningBalanceAccount': False, 'name': 'the new donations
            account', 'number': '8200'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewAccountResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
