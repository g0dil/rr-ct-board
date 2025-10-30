from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_group_groupcategories_group_category_id_response_409 import (
    DeleteGroupGroupcategoriesGroupCategoryIdResponse409,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_category_id: str,
    *,
    dry_run: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/group/groupcategories/{group_category_id}".format(
            group_category_id=group_category_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = DeleteGroupGroupcategoriesGroupCategoryIdResponse409.from_dict(
            response.json()
        )

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str]:
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
    dry_run: bool | Unset = UNSET,
) -> Response[Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str]:
    """
    Args:
        group_category_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    dry_run: bool | Unset = UNSET,
) -> Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str | None:
    """
    Args:
        group_category_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str
    """

    return sync_detailed(
        group_category_id=group_category_id,
        client=client,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    group_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    dry_run: bool | Unset = UNSET,
) -> Response[Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str]:
    """
    Args:
        group_category_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    dry_run: bool | Unset = UNSET,
) -> Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str | None:
    """
    Args:
        group_category_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGroupGroupcategoriesGroupCategoryIdResponse409 | str
    """

    return (
        await asyncio_detailed(
            group_category_id=group_category_id,
            client=client,
            dry_run=dry_run,
        )
    ).parsed
