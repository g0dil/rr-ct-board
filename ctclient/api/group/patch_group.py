from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_group_body import PatchGroupBody
from ...models.patch_group_response_200 import PatchGroupResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    body: PatchGroupBody,
    skip_my_posts_reducing_visibility: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["skip_my_posts_reducing_visibility"] = skip_my_posts_reducing_visibility

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/groups/{group_id}".format(
            group_id=group_id,
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchGroupResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PatchGroupResponse200.from_dict(response.json())

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
) -> Response[Any | PatchGroupResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchGroupBody,
    skip_my_posts_reducing_visibility: bool | Unset = UNSET,
) -> Response[Any | PatchGroupResponse200 | str]:
    """Update Group

     Update a group by id. All group fields can be updated here. Use the fields api to get all fields
    that can be updated here.

    Args:
        group_id (int):  Example: 42.
        skip_my_posts_reducing_visibility (bool | Unset):
        body (PatchGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchGroupResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        skip_my_posts_reducing_visibility=skip_my_posts_reducing_visibility,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchGroupBody,
    skip_my_posts_reducing_visibility: bool | Unset = UNSET,
) -> Any | PatchGroupResponse200 | str | None:
    """Update Group

     Update a group by id. All group fields can be updated here. Use the fields api to get all fields
    that can be updated here.

    Args:
        group_id (int):  Example: 42.
        skip_my_posts_reducing_visibility (bool | Unset):
        body (PatchGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchGroupResponse200 | str
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
        skip_my_posts_reducing_visibility=skip_my_posts_reducing_visibility,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchGroupBody,
    skip_my_posts_reducing_visibility: bool | Unset = UNSET,
) -> Response[Any | PatchGroupResponse200 | str]:
    """Update Group

     Update a group by id. All group fields can be updated here. Use the fields api to get all fields
    that can be updated here.

    Args:
        group_id (int):  Example: 42.
        skip_my_posts_reducing_visibility (bool | Unset):
        body (PatchGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchGroupResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        skip_my_posts_reducing_visibility=skip_my_posts_reducing_visibility,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchGroupBody,
    skip_my_posts_reducing_visibility: bool | Unset = UNSET,
) -> Any | PatchGroupResponse200 | str | None:
    """Update Group

     Update a group by id. All group fields can be updated here. Use the fields api to get all fields
    that can be updated here.

    Args:
        group_id (int):  Example: 42.
        skip_my_posts_reducing_visibility (bool | Unset):
        body (PatchGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchGroupResponse200 | str
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            skip_my_posts_reducing_visibility=skip_my_posts_reducing_visibility,
        )
    ).parsed
