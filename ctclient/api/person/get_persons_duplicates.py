from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_persons_duplicates_response_200 import (
    GetPersonsDuplicatesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    reset_cache: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["reset_cache"] = reset_cache

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/duplicates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPersonsDuplicatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPersonsDuplicatesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPersonsDuplicatesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    reset_cache: bool | Unset = UNSET,
) -> Response[GetPersonsDuplicatesResponse200]:
    """get potential duplicates of persons

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    Provide a list of potential duplicate person records. You can suppress some duplicates

    The other parameters are used to filter duplicates.

    Returns an array of duplicates

    * `p1` - properties of Person 1
    * `p2` - properties of Person 2

    Args:
        reset_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPersonsDuplicatesResponse200]
    """

    kwargs = _get_kwargs(
        reset_cache=reset_cache,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    reset_cache: bool | Unset = UNSET,
) -> GetPersonsDuplicatesResponse200 | None:
    """get potential duplicates of persons

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    Provide a list of potential duplicate person records. You can suppress some duplicates

    The other parameters are used to filter duplicates.

    Returns an array of duplicates

    * `p1` - properties of Person 1
    * `p2` - properties of Person 2

    Args:
        reset_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPersonsDuplicatesResponse200
    """

    return sync_detailed(
        client=client,
        reset_cache=reset_cache,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    reset_cache: bool | Unset = UNSET,
) -> Response[GetPersonsDuplicatesResponse200]:
    """get potential duplicates of persons

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    Provide a list of potential duplicate person records. You can suppress some duplicates

    The other parameters are used to filter duplicates.

    Returns an array of duplicates

    * `p1` - properties of Person 1
    * `p2` - properties of Person 2

    Args:
        reset_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPersonsDuplicatesResponse200]
    """

    kwargs = _get_kwargs(
        reset_cache=reset_cache,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    reset_cache: bool | Unset = UNSET,
) -> GetPersonsDuplicatesResponse200 | None:
    """get potential duplicates of persons

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    Provide a list of potential duplicate person records. You can suppress some duplicates

    The other parameters are used to filter duplicates.

    Returns an array of duplicates

    * `p1` - properties of Person 1
    * `p2` - properties of Person 2

    Args:
        reset_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPersonsDuplicatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            reset_cache=reset_cache,
        )
    ).parsed
