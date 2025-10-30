from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wiki_categories_wiki_category_id_search_response_200 import (
    GetWikiCategoriesWikiCategoryIdSearchResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    wiki_category_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    json_wiki_category_ids: list[int] | Unset = UNSET
    if not isinstance(wiki_category_ids, Unset):
        json_wiki_category_ids = wiki_category_ids

    params["wiki_category_ids[]"] = json_wiki_category_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/wiki/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWikiCategoriesWikiCategoryIdSearchResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWikiCategoriesWikiCategoryIdSearchResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWikiCategoriesWikiCategoryIdSearchResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    wiki_category_ids: list[int] | Unset = UNSET,
) -> Response[GetWikiCategoriesWikiCategoryIdSearchResponse200]:
    """Your GET endpoint

     Full text search in all wiki pages

    Args:
        query (str | Unset):
        wiki_category_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWikiCategoriesWikiCategoryIdSearchResponse200]
    """

    kwargs = _get_kwargs(
        query=query,
        wiki_category_ids=wiki_category_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    wiki_category_ids: list[int] | Unset = UNSET,
) -> GetWikiCategoriesWikiCategoryIdSearchResponse200 | None:
    """Your GET endpoint

     Full text search in all wiki pages

    Args:
        query (str | Unset):
        wiki_category_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWikiCategoriesWikiCategoryIdSearchResponse200
    """

    return sync_detailed(
        client=client,
        query=query,
        wiki_category_ids=wiki_category_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    wiki_category_ids: list[int] | Unset = UNSET,
) -> Response[GetWikiCategoriesWikiCategoryIdSearchResponse200]:
    """Your GET endpoint

     Full text search in all wiki pages

    Args:
        query (str | Unset):
        wiki_category_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWikiCategoriesWikiCategoryIdSearchResponse200]
    """

    kwargs = _get_kwargs(
        query=query,
        wiki_category_ids=wiki_category_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    wiki_category_ids: list[int] | Unset = UNSET,
) -> GetWikiCategoriesWikiCategoryIdSearchResponse200 | None:
    """Your GET endpoint

     Full text search in all wiki pages

    Args:
        query (str | Unset):
        wiki_category_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWikiCategoriesWikiCategoryIdSearchResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            wiki_category_ids=wiki_category_ids,
        )
    ).parsed
