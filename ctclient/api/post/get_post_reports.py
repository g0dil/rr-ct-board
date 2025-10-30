from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_post_reports_domain_type import GetPostReportsDomainType
from ...models.get_post_reports_status import GetPostReportsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    domain_type: GetPostReportsDomainType | Unset = UNSET,
    domain_id: int | Unset = UNSET,
    status: GetPostReportsStatus | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_domain_type: str | Unset = UNSET
    if not isinstance(domain_type, Unset):
        json_domain_type = domain_type.value

    params["domain_type"] = json_domain_type

    params["domain_id"] = domain_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/post/reports",
        "params": params,
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
    *,
    client: AuthenticatedClient | Client,
    domain_type: GetPostReportsDomainType | Unset = UNSET,
    domain_id: int | Unset = UNSET,
    status: GetPostReportsStatus | Unset = UNSET,
) -> Response[Any | str]:
    """
    Args:
        domain_type (GetPostReportsDomainType | Unset):
        domain_id (int | Unset):
        status (GetPostReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    domain_type: GetPostReportsDomainType | Unset = UNSET,
    domain_id: int | Unset = UNSET,
    status: GetPostReportsStatus | Unset = UNSET,
) -> Any | str | None:
    """
    Args:
        domain_type (GetPostReportsDomainType | Unset):
        domain_id (int | Unset):
        status (GetPostReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        domain_type=domain_type,
        domain_id=domain_id,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    domain_type: GetPostReportsDomainType | Unset = UNSET,
    domain_id: int | Unset = UNSET,
    status: GetPostReportsStatus | Unset = UNSET,
) -> Response[Any | str]:
    """
    Args:
        domain_type (GetPostReportsDomainType | Unset):
        domain_id (int | Unset):
        status (GetPostReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    domain_type: GetPostReportsDomainType | Unset = UNSET,
    domain_id: int | Unset = UNSET,
    status: GetPostReportsStatus | Unset = UNSET,
) -> Any | str | None:
    """
    Args:
        domain_type (GetPostReportsDomainType | Unset):
        domain_id (int | Unset):
        status (GetPostReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            domain_type=domain_type,
            domain_id=domain_id,
            status=status,
        )
    ).parsed
