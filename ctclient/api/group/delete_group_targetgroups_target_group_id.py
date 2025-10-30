from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_group_targetgroups_target_group_id_response_409 import (
    DeleteGroupTargetgroupsTargetGroupIdResponse409,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    target_group_id: str,
    *,
    dry_run: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/group/targetgroups/{target_group_id}".format(
            target_group_id=target_group_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str | None:
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
        response_409 = DeleteGroupTargetgroupsTargetGroupIdResponse409.from_dict(
            response.json()
        )

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_group_id: str,
    *,
    client: AuthenticatedClient | Client,
    dry_run: bool | Unset = UNSET,
) -> Response[Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str]:
    """delete target group

    Args:
        target_group_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str]
    """

    kwargs = _get_kwargs(
        target_group_id=target_group_id,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_group_id: str,
    *,
    client: AuthenticatedClient | Client,
    dry_run: bool | Unset = UNSET,
) -> Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str | None:
    """delete target group

    Args:
        target_group_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str
    """

    return sync_detailed(
        target_group_id=target_group_id,
        client=client,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    target_group_id: str,
    *,
    client: AuthenticatedClient | Client,
    dry_run: bool | Unset = UNSET,
) -> Response[Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str]:
    """delete target group

    Args:
        target_group_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str]
    """

    kwargs = _get_kwargs(
        target_group_id=target_group_id,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_group_id: str,
    *,
    client: AuthenticatedClient | Client,
    dry_run: bool | Unset = UNSET,
) -> Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str | None:
    """delete target group

    Args:
        target_group_id (str):
        dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGroupTargetgroupsTargetGroupIdResponse409 | str
    """

    return (
        await asyncio_detailed(
            target_group_id=target_group_id,
            client=client,
            dry_run=dry_run,
        )
    ).parsed
