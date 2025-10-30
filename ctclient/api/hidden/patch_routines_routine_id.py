from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_routines_routine_id_body import PatchRoutinesRoutineIdBody
from ...models.patch_routines_routine_id_response_200 import (
    PatchRoutinesRoutineIdResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    routine_id: int,
    *,
    body: PatchRoutinesRoutineIdBody,
    dry_run: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["dry_run"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/routines/{routine_id}".format(
            routine_id=routine_id,
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchRoutinesRoutineIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PatchRoutinesRoutineIdResponse200.from_dict(response.json())

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
) -> Response[Any | PatchRoutinesRoutineIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutinesRoutineIdBody,
    dry_run: bool | Unset = UNSET,
) -> Response[Any | PatchRoutinesRoutineIdResponse200 | str]:
    """Update the specified routine.

    Args:
        routine_id (int):  Example: 9.
        dry_run (bool | Unset):
        body (PatchRoutinesRoutineIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchRoutinesRoutineIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        body=body,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutinesRoutineIdBody,
    dry_run: bool | Unset = UNSET,
) -> Any | PatchRoutinesRoutineIdResponse200 | str | None:
    """Update the specified routine.

    Args:
        routine_id (int):  Example: 9.
        dry_run (bool | Unset):
        body (PatchRoutinesRoutineIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchRoutinesRoutineIdResponse200 | str
    """

    return sync_detailed(
        routine_id=routine_id,
        client=client,
        body=body,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutinesRoutineIdBody,
    dry_run: bool | Unset = UNSET,
) -> Response[Any | PatchRoutinesRoutineIdResponse200 | str]:
    """Update the specified routine.

    Args:
        routine_id (int):  Example: 9.
        dry_run (bool | Unset):
        body (PatchRoutinesRoutineIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchRoutinesRoutineIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        body=body,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutinesRoutineIdBody,
    dry_run: bool | Unset = UNSET,
) -> Any | PatchRoutinesRoutineIdResponse200 | str | None:
    """Update the specified routine.

    Args:
        routine_id (int):  Example: 9.
        dry_run (bool | Unset):
        body (PatchRoutinesRoutineIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchRoutinesRoutineIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            routine_id=routine_id,
            client=client,
            body=body,
            dry_run=dry_run,
        )
    ).parsed
