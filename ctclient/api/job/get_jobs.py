from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_jobs_response_200 import GetJobsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: list[str] | Unset = UNSET,
    identifier: str | Unset = UNSET,
    name: str | Unset = UNSET,
    domain_ids: list[int] | Unset = UNSET,
    created_start_date: str | Unset = UNSET,
    created_end_date: str | Unset = UNSET,
    modified_start_date: str | Unset = UNSET,
    modified_end_date: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["identifier"] = identifier

    params["name"] = name

    json_domain_ids: list[int] | Unset = UNSET
    if not isinstance(domain_ids, Unset):
        json_domain_ids = domain_ids

    params["domain_ids[]"] = json_domain_ids

    params["created_start_date"] = created_start_date

    params["created_end_date"] = created_end_date

    params["modified_start_date"] = modified_start_date

    params["modified_end_date"] = modified_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetJobsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetJobsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetJobsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: list[str] | Unset = UNSET,
    identifier: str | Unset = UNSET,
    name: str | Unset = UNSET,
    domain_ids: list[int] | Unset = UNSET,
    created_start_date: str | Unset = UNSET,
    created_end_date: str | Unset = UNSET,
    modified_start_date: str | Unset = UNSET,
    modified_end_date: str | Unset = UNSET,
) -> Response[GetJobsResponse200]:
    """Your GET endpoint

    Args:
        status (list[str] | Unset):
        identifier (str | Unset):
        name (str | Unset):
        domain_ids (list[int] | Unset):
        created_start_date (str | Unset):
        created_end_date (str | Unset):
        modified_start_date (str | Unset):
        modified_end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        identifier=identifier,
        name=name,
        domain_ids=domain_ids,
        created_start_date=created_start_date,
        created_end_date=created_end_date,
        modified_start_date=modified_start_date,
        modified_end_date=modified_end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: list[str] | Unset = UNSET,
    identifier: str | Unset = UNSET,
    name: str | Unset = UNSET,
    domain_ids: list[int] | Unset = UNSET,
    created_start_date: str | Unset = UNSET,
    created_end_date: str | Unset = UNSET,
    modified_start_date: str | Unset = UNSET,
    modified_end_date: str | Unset = UNSET,
) -> GetJobsResponse200 | None:
    """Your GET endpoint

    Args:
        status (list[str] | Unset):
        identifier (str | Unset):
        name (str | Unset):
        domain_ids (list[int] | Unset):
        created_start_date (str | Unset):
        created_end_date (str | Unset):
        modified_start_date (str | Unset):
        modified_end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobsResponse200
    """

    return sync_detailed(
        client=client,
        status=status,
        identifier=identifier,
        name=name,
        domain_ids=domain_ids,
        created_start_date=created_start_date,
        created_end_date=created_end_date,
        modified_start_date=modified_start_date,
        modified_end_date=modified_end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: list[str] | Unset = UNSET,
    identifier: str | Unset = UNSET,
    name: str | Unset = UNSET,
    domain_ids: list[int] | Unset = UNSET,
    created_start_date: str | Unset = UNSET,
    created_end_date: str | Unset = UNSET,
    modified_start_date: str | Unset = UNSET,
    modified_end_date: str | Unset = UNSET,
) -> Response[GetJobsResponse200]:
    """Your GET endpoint

    Args:
        status (list[str] | Unset):
        identifier (str | Unset):
        name (str | Unset):
        domain_ids (list[int] | Unset):
        created_start_date (str | Unset):
        created_end_date (str | Unset):
        modified_start_date (str | Unset):
        modified_end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        identifier=identifier,
        name=name,
        domain_ids=domain_ids,
        created_start_date=created_start_date,
        created_end_date=created_end_date,
        modified_start_date=modified_start_date,
        modified_end_date=modified_end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: list[str] | Unset = UNSET,
    identifier: str | Unset = UNSET,
    name: str | Unset = UNSET,
    domain_ids: list[int] | Unset = UNSET,
    created_start_date: str | Unset = UNSET,
    created_end_date: str | Unset = UNSET,
    modified_start_date: str | Unset = UNSET,
    modified_end_date: str | Unset = UNSET,
) -> GetJobsResponse200 | None:
    """Your GET endpoint

    Args:
        status (list[str] | Unset):
        identifier (str | Unset):
        name (str | Unset):
        domain_ids (list[int] | Unset):
        created_start_date (str | Unset):
        created_end_date (str | Unset):
        modified_start_date (str | Unset):
        modified_end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            identifier=identifier,
            name=name,
            domain_ids=domain_ids,
            created_start_date=created_start_date,
            created_end_date=created_end_date,
            modified_start_date=modified_start_date,
            modified_end_date=modified_end_date,
        )
    ).parsed
