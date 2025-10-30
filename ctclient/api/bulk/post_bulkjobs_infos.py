from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_bulkjobs_infos_body import PostBulkjobsInfosBody
from ...models.post_bulkjobs_infos_response_200 import PostBulkjobsInfosResponse200
from ...types import Response


def _get_kwargs(
    domain_type: str,
    job_key: str,
    *,
    body: PostBulkjobsInfosBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/bulkjobs/{domain_type}/{job_key}/infos".format(
            domain_type=domain_type,
            job_key=job_key,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostBulkjobsInfosResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PostBulkjobsInfosResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = response.text
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
) -> Response[Any | PostBulkjobsInfosResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_type: str,
    job_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostBulkjobsInfosBody,
) -> Response[Any | PostBulkjobsInfosResponse200 | str]:
    """Calculate infos about bulk job

     Calculate infos about bulk job

    Args:
        domain_type (str):
        job_key (str):
        body (PostBulkjobsInfosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostBulkjobsInfosResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        job_key=job_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_type: str,
    job_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostBulkjobsInfosBody,
) -> Any | PostBulkjobsInfosResponse200 | str | None:
    """Calculate infos about bulk job

     Calculate infos about bulk job

    Args:
        domain_type (str):
        job_key (str):
        body (PostBulkjobsInfosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostBulkjobsInfosResponse200 | str
    """

    return sync_detailed(
        domain_type=domain_type,
        job_key=job_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    domain_type: str,
    job_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostBulkjobsInfosBody,
) -> Response[Any | PostBulkjobsInfosResponse200 | str]:
    """Calculate infos about bulk job

     Calculate infos about bulk job

    Args:
        domain_type (str):
        job_key (str):
        body (PostBulkjobsInfosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostBulkjobsInfosResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        job_key=job_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: str,
    job_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostBulkjobsInfosBody,
) -> Any | PostBulkjobsInfosResponse200 | str | None:
    """Calculate infos about bulk job

     Calculate infos about bulk job

    Args:
        domain_type (str):
        job_key (str):
        body (PostBulkjobsInfosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostBulkjobsInfosResponse200 | str
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            job_key=job_key,
            client=client,
            body=body,
        )
    ).parsed
