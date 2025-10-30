from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_routines_routine_id_runs_run_id_run_action_run_action import (
    GetRoutinesRoutineIdRunsRunIdRunActionRunAction,
)
from ...types import Response


def _get_kwargs(
    routine_id: int,
    run_id: int,
    run_action: GetRoutinesRoutineIdRunsRunIdRunActionRunAction,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/routines/{routine_id}/runs/{run_id}/{run_action}".format(
            routine_id=routine_id,
            run_id=run_id,
            run_action=run_action,
        ),
    }

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
    routine_id: int,
    run_id: int,
    run_action: GetRoutinesRoutineIdRunsRunIdRunActionRunAction,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get all available runs for the specified routine.

    Args:
        routine_id (int):  Example: 9.
        run_id (int):  Example: 16.
        run_action (GetRoutinesRoutineIdRunsRunIdRunActionRunAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        run_id=run_id,
        run_action=run_action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routine_id: int,
    run_id: int,
    run_action: GetRoutinesRoutineIdRunsRunIdRunActionRunAction,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get all available runs for the specified routine.

    Args:
        routine_id (int):  Example: 9.
        run_id (int):  Example: 16.
        run_action (GetRoutinesRoutineIdRunsRunIdRunActionRunAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        routine_id=routine_id,
        run_id=run_id,
        run_action=run_action,
        client=client,
    ).parsed


async def asyncio_detailed(
    routine_id: int,
    run_id: int,
    run_action: GetRoutinesRoutineIdRunsRunIdRunActionRunAction,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get all available runs for the specified routine.

    Args:
        routine_id (int):  Example: 9.
        run_id (int):  Example: 16.
        run_action (GetRoutinesRoutineIdRunsRunIdRunActionRunAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        run_id=run_id,
        run_action=run_action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routine_id: int,
    run_id: int,
    run_action: GetRoutinesRoutineIdRunsRunIdRunActionRunAction,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get all available runs for the specified routine.

    Args:
        routine_id (int):  Example: 9.
        run_id (int):  Example: 16.
        run_action (GetRoutinesRoutineIdRunsRunIdRunActionRunAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            routine_id=routine_id,
            run_id=run_id,
            run_action=run_action,
            client=client,
        )
    ).parsed
