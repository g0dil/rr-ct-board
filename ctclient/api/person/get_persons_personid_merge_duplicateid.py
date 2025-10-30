from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    person_id: str,
    duplicate_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/merge/{duplicate_id}".format(
            person_id=person_id,
            duplicate_id=duplicate_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
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
    person_id: str,
    duplicate_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get information to compare two person records in order to prepare a merge

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    This retrieves the basis for a merge of two person records You will receive person data,
    relationships, groups etc. for both persons.

    Args:
        person_id (str):
        duplicate_id (str):  Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        duplicate_id=duplicate_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: str,
    duplicate_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get information to compare two person records in order to prepare a merge

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    This retrieves the basis for a merge of two person records You will receive person data,
    relationships, groups etc. for both persons.

    Args:
        person_id (str):
        duplicate_id (str):  Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        duplicate_id=duplicate_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
