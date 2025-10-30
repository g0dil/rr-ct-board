from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body import (
    PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody,
)
from ...models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200 import (
    PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200,
)
from ...types import Response


def _get_kwargs(
    external_system_id: str,
    job_id: str,
    *,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/sync/externalsystems/{external_system_id}/jobconfigs/{job_id}/filter".format(
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
) -> (
    Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200 | None
):
    if response.status_code == 200:
        response_200 = PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200.from_dict(
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
    Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
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
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody,
) -> Response[
    Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
]:
    """Save entity filters

     Save entity filter for this job.

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200]
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
    client: AuthenticatedClient,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody,
) -> (
    Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200 | None
):
    """Save entity filters

     Save entity filter for this job.

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
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
    client: AuthenticatedClient,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody,
) -> Response[
    Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
]:
    """Save entity filters

     Save entity filter for this job.

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200]
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
    client: AuthenticatedClient,
    body: PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody,
) -> (
    Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200 | None
):
    """Save entity filters

     Save entity filter for this job.

    Args:
        external_system_id (str):
        job_id (str):
        body (PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200
    """

    return (
        await asyncio_detailed(
            external_system_id=external_system_id,
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
