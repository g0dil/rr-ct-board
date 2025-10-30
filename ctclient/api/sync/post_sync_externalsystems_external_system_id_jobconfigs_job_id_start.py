from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_sync_externalsystems_external_system_id_jobconfigs_job_id_start_body import (
    PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody,
)
from ...types import Response


def _get_kwargs(
    external_system_id: str,
    job_id: str,
    *,
    body: PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sync/externalsystems/{external_system_id}/jobconfigs/{job_id}/start".format(
            external_system_id=external_system_id,
            job_id=job_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody,
) -> Response[Any]:
    """Start Execution

     Start Execution of specific Job Configuration.

    Args:
        external_system_id (str):
        job_id (str):
        body (PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody,
) -> Response[Any]:
    """Start Execution

     Start Execution of specific Job Configuration.

    Args:
        external_system_id (str):
        job_id (str):
        body (PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
