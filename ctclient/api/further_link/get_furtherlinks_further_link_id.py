from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_furtherlinks_further_link_id_response_200 import (
    GetFurtherlinksFurtherLinkIdResponse200,
)
from ...types import Response


def _get_kwargs(
    further_link_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/furtherlinks/{further_link_id}".format(
            further_link_id=further_link_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetFurtherlinksFurtherLinkIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetFurtherlinksFurtherLinkIdResponse200.from_dict(
            response.json()
        )

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
) -> Response[Any | GetFurtherlinksFurtherLinkIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    further_link_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetFurtherlinksFurtherLinkIdResponse200 | str]:
    """Get further link.

     Get the specified further link.

    Args:
        further_link_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFurtherlinksFurtherLinkIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        further_link_id=further_link_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    further_link_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetFurtherlinksFurtherLinkIdResponse200 | str | None:
    """Get further link.

     Get the specified further link.

    Args:
        further_link_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFurtherlinksFurtherLinkIdResponse200 | str
    """

    return sync_detailed(
        further_link_id=further_link_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    further_link_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetFurtherlinksFurtherLinkIdResponse200 | str]:
    """Get further link.

     Get the specified further link.

    Args:
        further_link_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFurtherlinksFurtherLinkIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        further_link_id=further_link_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    further_link_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetFurtherlinksFurtherLinkIdResponse200 | str | None:
    """Get further link.

     Get the specified further link.

    Args:
        further_link_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFurtherlinksFurtherLinkIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            further_link_id=further_link_id,
            client=client,
        )
    ).parsed
