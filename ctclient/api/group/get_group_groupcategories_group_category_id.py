from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_group_groupcategories_group_category_id_response_200 import (
    GetGroupGroupcategoriesGroupCategoryIdResponse200,
)
from ...types import Response


def _get_kwargs(
    group_category_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group/groupcategories/{group_category_id}".format(
            group_category_id=group_category_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetGroupGroupcategoriesGroupCategoryIdResponse200.from_dict(
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
) -> Response[Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_category_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str]:
    """Get Group Category

    Args:
        group_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_category_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str | None:
    """Get Group Category

    Args:
        group_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str
    """

    return sync_detailed(
        group_category_id=group_category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_category_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str]:
    """Get Group Category

    Args:
        group_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_category_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str | None:
    """Get Group Category

    Args:
        group_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupGroupcategoriesGroupCategoryIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            group_category_id=group_category_id,
            client=client,
        )
    ).parsed
