from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_finance_turnover_report_body import PostFinanceTurnoverReportBody
from ...models.post_finance_turnover_report_response_200 import (
    PostFinanceTurnoverReportResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostFinanceTurnoverReportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/finance/reports/turnover",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostFinanceTurnoverReportResponse200 | None:
    if response.status_code == 200:
        response_200 = PostFinanceTurnoverReportResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostFinanceTurnoverReportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFinanceTurnoverReportBody,
) -> Response[PostFinanceTurnoverReportResponse200]:
    """Issue new Turnover Report

     Issue new turnover report. _Monthly_ and _Quarterly_ reports are available. The result provides the
    URI to the generated PDF file.

    Args:
        body (PostFinanceTurnoverReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFinanceTurnoverReportResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostFinanceTurnoverReportBody,
) -> PostFinanceTurnoverReportResponse200 | None:
    """Issue new Turnover Report

     Issue new turnover report. _Monthly_ and _Quarterly_ reports are available. The result provides the
    URI to the generated PDF file.

    Args:
        body (PostFinanceTurnoverReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFinanceTurnoverReportResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFinanceTurnoverReportBody,
) -> Response[PostFinanceTurnoverReportResponse200]:
    """Issue new Turnover Report

     Issue new turnover report. _Monthly_ and _Quarterly_ reports are available. The result provides the
    URI to the generated PDF file.

    Args:
        body (PostFinanceTurnoverReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFinanceTurnoverReportResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFinanceTurnoverReportBody,
) -> PostFinanceTurnoverReportResponse200 | None:
    """Issue new Turnover Report

     Issue new turnover report. _Monthly_ and _Quarterly_ reports are available. The result provides the
    URI to the generated PDF file.

    Args:
        body (PostFinanceTurnoverReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFinanceTurnoverReportResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
