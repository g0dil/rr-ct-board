from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200 import (
    GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200,
)
from ...types import Response


def _get_kwargs(
    external_system_id: str,
    job_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/externalsystems/{external_system_id}/jobconfigs/{job_id}/filter".format(
            external_system_id=external_system_id,
            job_id=job_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200 | None
):
    if response.status_code == 200:
        response_200 = GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
]:
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
    client: AuthenticatedClient,
) -> Response[
    Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
]:
    """Fetch all entity filters for this job

     Fetch all entity filters for this job.

    Args:
        external_system_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200 | None
):
    """Fetch all entity filters for this job

     Fetch all entity filters for this job.

    Args:
        external_system_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
    """

    return sync_detailed(
        external_system_id=external_system_id,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
]:
    """Fetch all entity filters for this job

     Fetch all entity filters for this job.

    Args:
        external_system_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_system_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200 | None
):
    """Fetch all entity filters for this job

     Fetch all entity filters for this job.

    Args:
        external_system_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
    """

    return (
        await asyncio_detailed(
            external_system_id=external_system_id,
            job_id=job_id,
            client=client,
        )
    ).parsed
