from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_queue_job_groups_status_response_200 import (
    GetQueueJobGroupsStatusResponse200,
)
from ...types import Response


def _get_kwargs(
    queue: str,
    job_group: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/queues/{queue}/jobgroups/{job_group}".format(
            queue=queue,
            job_group=job_group,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetQueueJobGroupsStatusResponse200 | None:
    if response.status_code == 200:
        response_200 = GetQueueJobGroupsStatusResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetQueueJobGroupsStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue: str,
    job_group: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetQueueJobGroupsStatusResponse200]:
    """Status Information About Job Groups in Queue

     Job in a queue can belong to a job group to categorize a job. This endpoint counts jobs in queue and
    groups them by they status.

    Use this endpoint to check if all jobs are processed or if still jobs are pending and wait to be
    processed.

    Args:
        queue (str):
        job_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueueJobGroupsStatusResponse200]
    """

    kwargs = _get_kwargs(
        queue=queue,
        job_group=job_group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue: str,
    job_group: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetQueueJobGroupsStatusResponse200 | None:
    """Status Information About Job Groups in Queue

     Job in a queue can belong to a job group to categorize a job. This endpoint counts jobs in queue and
    groups them by they status.

    Use this endpoint to check if all jobs are processed or if still jobs are pending and wait to be
    processed.

    Args:
        queue (str):
        job_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueueJobGroupsStatusResponse200
    """

    return sync_detailed(
        queue=queue,
        job_group=job_group,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue: str,
    job_group: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetQueueJobGroupsStatusResponse200]:
    """Status Information About Job Groups in Queue

     Job in a queue can belong to a job group to categorize a job. This endpoint counts jobs in queue and
    groups them by they status.

    Use this endpoint to check if all jobs are processed or if still jobs are pending and wait to be
    processed.

    Args:
        queue (str):
        job_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueueJobGroupsStatusResponse200]
    """

    kwargs = _get_kwargs(
        queue=queue,
        job_group=job_group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue: str,
    job_group: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetQueueJobGroupsStatusResponse200 | None:
    """Status Information About Job Groups in Queue

     Job in a queue can belong to a job group to categorize a job. This endpoint counts jobs in queue and
    groups them by they status.

    Use this endpoint to check if all jobs are processed or if still jobs are pending and wait to be
    processed.

    Args:
        queue (str):
        job_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueueJobGroupsStatusResponse200
    """

    return (
        await asyncio_detailed(
            queue=queue,
            job_group=job_group,
            client=client,
        )
    ).parsed
