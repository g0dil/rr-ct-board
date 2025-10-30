from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    request_id: int,
    *,
    comment: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["comment"] = comment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/persons/{person_id}/servicerequests/{request_id}".format(
            person_id=person_id,
            request_id=request_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    person_id: int,
    request_id: int,
    *,
    client: AuthenticatedClient | Client,
    comment: str | Unset = UNSET,
) -> Response[Any | str]:
    """Decline a service request for a person

     Use this endpoint to decline a service request.

    Args:
        person_id (int):  Example: 42.
        request_id (int):  Example: 42.
        comment (str | Unset):  Example: Holiday.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        request_id=request_id,
        comment=comment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    request_id: int,
    *,
    client: AuthenticatedClient | Client,
    comment: str | Unset = UNSET,
) -> Any | str | None:
    """Decline a service request for a person

     Use this endpoint to decline a service request.

    Args:
        person_id (int):  Example: 42.
        request_id (int):  Example: 42.
        comment (str | Unset):  Example: Holiday.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        person_id=person_id,
        request_id=request_id,
        client=client,
        comment=comment,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    request_id: int,
    *,
    client: AuthenticatedClient | Client,
    comment: str | Unset = UNSET,
) -> Response[Any | str]:
    """Decline a service request for a person

     Use this endpoint to decline a service request.

    Args:
        person_id (int):  Example: 42.
        request_id (int):  Example: 42.
        comment (str | Unset):  Example: Holiday.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        request_id=request_id,
        comment=comment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    request_id: int,
    *,
    client: AuthenticatedClient | Client,
    comment: str | Unset = UNSET,
) -> Any | str | None:
    """Decline a service request for a person

     Use this endpoint to decline a service request.

    Args:
        person_id (int):  Example: 42.
        request_id (int):  Example: 42.
        comment (str | Unset):  Example: Holiday.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            request_id=request_id,
            client=client,
            comment=comment,
        )
    ).parsed
