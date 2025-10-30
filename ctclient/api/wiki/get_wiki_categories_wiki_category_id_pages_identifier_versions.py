from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    wiki_category_id: int,
    identifier: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/wiki/categories/{wiki_category_id}/pages/{identifier}/versions".format(
            wiki_category_id=wiki_category_id,
            identifier=identifier,
        ),
    }

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
    wiki_category_id: int,
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Returns all version of the wiki page for the given

     Returns all version of the wiki page for the given identifier.

    Args:
        wiki_category_id (int):  Example: 42.
        identifier (str):  Example: main.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        wiki_category_id=wiki_category_id,
        identifier=identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    wiki_category_id: int,
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Returns all version of the wiki page for the given

     Returns all version of the wiki page for the given identifier.

    Args:
        wiki_category_id (int):  Example: 42.
        identifier (str):  Example: main.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        wiki_category_id=wiki_category_id,
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
