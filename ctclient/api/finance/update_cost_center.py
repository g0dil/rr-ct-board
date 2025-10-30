from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_cost_center_body import UpdateCostCenterBody
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: UpdateCostCenterBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/finance/costcenters/{id}".format(
            id=id,
        ),
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
    body: UpdateCostCenterBody,
) -> Response[Any | str]:
    """Update cost center

     Update cost center

    Args:
        id (int):  Example: 1.
        body (UpdateCostCenterBody):  Example: {'accountId': 4, 'accountingPeriodId': 5, 'budget':
            2300, 'groupId': 5, 'name': 'Kostenstelle Jugend', 'number': '803'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
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
    body: UpdateCostCenterBody,
) -> Any | str | None:
    """Update cost center

     Update cost center

    Args:
        id (int):  Example: 1.
        body (UpdateCostCenterBody):  Example: {'accountId': 4, 'accountingPeriodId': 5, 'budget':
            2300, 'groupId': 5, 'name': 'Kostenstelle Jugend', 'number': '803'}.

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
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCostCenterBody,
) -> Response[Any | str]:
    """Update cost center

     Update cost center

    Args:
        id (int):  Example: 1.
        body (UpdateCostCenterBody):  Example: {'accountId': 4, 'accountingPeriodId': 5, 'budget':
            2300, 'groupId': 5, 'name': 'Kostenstelle Jugend', 'number': '803'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
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
    body: UpdateCostCenterBody,
) -> Any | str | None:
    """Update cost center

     Update cost center

    Args:
        id (int):  Example: 1.
        body (UpdateCostCenterBody):  Example: {'accountId': 4, 'accountingPeriodId': 5, 'budget':
            2300, 'groupId': 5, 'name': 'Kostenstelle Jugend', 'number': '803'}.

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
        )
    ).parsed
