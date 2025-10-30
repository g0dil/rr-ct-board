from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_queue_worker_queue import StartQueueWorkerQueue
from ...models.start_queue_worker_response_200 import StartQueueWorkerResponse200
from ...types import Response


def _get_kwargs(
    queue: StartQueueWorkerQueue,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/queues/{queue}".format(
            queue=queue,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StartQueueWorkerResponse200 | None:
    if response.status_code == 200:
        response_200 = StartQueueWorkerResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StartQueueWorkerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue: StartQueueWorkerQueue,
    *,
    client: AuthenticatedClient | Client,
) -> Response[StartQueueWorkerResponse200]:
    """Start Worker For Queue

     ChurchTools utilizes a queueing system to offload time-intensive or processing-intensive work.
    Calling this endpoint will start a worker, which grabs pending jobs and processing them. If the
    queue has still jobs pending the worker starts a new worker to continue the work.

    Args:
        queue (StartQueueWorkerQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartQueueWorkerResponse200]
    """

    kwargs = _get_kwargs(
        queue=queue,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue: StartQueueWorkerQueue,
    *,
    client: AuthenticatedClient | Client,
) -> StartQueueWorkerResponse200 | None:
    """Start Worker For Queue

     ChurchTools utilizes a queueing system to offload time-intensive or processing-intensive work.
    Calling this endpoint will start a worker, which grabs pending jobs and processing them. If the
    queue has still jobs pending the worker starts a new worker to continue the work.

    Args:
        queue (StartQueueWorkerQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartQueueWorkerResponse200
    """

    return sync_detailed(
        queue=queue,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue: StartQueueWorkerQueue,
    *,
    client: AuthenticatedClient | Client,
) -> Response[StartQueueWorkerResponse200]:
    """Start Worker For Queue

     ChurchTools utilizes a queueing system to offload time-intensive or processing-intensive work.
    Calling this endpoint will start a worker, which grabs pending jobs and processing them. If the
    queue has still jobs pending the worker starts a new worker to continue the work.

    Args:
        queue (StartQueueWorkerQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartQueueWorkerResponse200]
    """

    kwargs = _get_kwargs(
        queue=queue,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue: StartQueueWorkerQueue,
    *,
    client: AuthenticatedClient | Client,
) -> StartQueueWorkerResponse200 | None:
    """Start Worker For Queue

     ChurchTools utilizes a queueing system to offload time-intensive or processing-intensive work.
    Calling this endpoint will start a worker, which grabs pending jobs and processing them. If the
    queue has still jobs pending the worker starts a new worker to continue the work.

    Args:
        queue (StartQueueWorkerQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartQueueWorkerResponse200
    """

    return (
        await asyncio_detailed(
            queue=queue,
            client=client,
        )
    ).parsed
