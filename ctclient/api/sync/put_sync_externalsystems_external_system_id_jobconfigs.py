from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_sync_externalsystems_external_system_id_jobconfigs_job_configuration import (
    PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration,
)
from ...models.put_sync_externalsystems_external_system_id_jobconfigs_response_200 import (
    PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200,
)
from ...types import Response


def _get_kwargs(
    external_system_id: str,
    job_id: str,
    *,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/sync/externalsystems/{external_system_id}/jobconfigs/{job_id}".format(
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
) -> PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200]:
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
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration,
) -> Response[PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200]:
    """Update job configuration

     Update job configuration

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200]
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


def sync(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration,
) -> PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200 | None:
    """Update job configuration

     Update job configuration

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200
    """

    return sync_detailed(
        external_system_id=external_system_id,
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration,
) -> Response[PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200]:
    """Update job configuration

     Update job configuration

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration,
) -> PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200 | None:
    """Update job configuration

     Update job configuration

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSyncExternalsystemsExternalSystemIdJobconfigsResponse200
    """

    return (
        await asyncio_detailed(
            external_system_id=external_system_id,
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
