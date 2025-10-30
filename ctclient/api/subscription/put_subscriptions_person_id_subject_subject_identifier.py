from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_subscriptions_person_id_subject_subject_identifier_response_200 import (
    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200,
)
from ...models.put_subscriptions_person_id_subject_subject_identifier_subject import (
    PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject,
)
from ...types import Response


def _get_kwargs(
    person_id: int,
    subject: PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject,
    subject_identifier: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/subscriptions/{person_id}/{subject}/{subject_identifier}".format(
            person_id=person_id,
            subject=subject,
            subject_identifier=subject_identifier,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str | None:
    if response.status_code == 200:
        response_200 = (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200.from_dict(
                response.json()
            )
        )

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
) -> Response[Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    subject: PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject,
    subject_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str]:
    """Create a new subscription

    Args:
        person_id (int):  Example: 42.
        subject (PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject):  Example: group.
        subject_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        subject=subject,
        subject_identifier=subject_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    subject: PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject,
    subject_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str | None:
    """Create a new subscription

    Args:
        person_id (int):  Example: 42.
        subject (PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject):  Example: group.
        subject_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str
    """

    return sync_detailed(
        person_id=person_id,
        subject=subject,
        subject_identifier=subject_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    subject: PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject,
    subject_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str]:
    """Create a new subscription

    Args:
        person_id (int):  Example: 42.
        subject (PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject):  Example: group.
        subject_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        subject=subject,
        subject_identifier=subject_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    subject: PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject,
    subject_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str | None:
    """Create a new subscription

    Args:
        person_id (int):  Example: 42.
        subject (PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject):  Example: group.
        subject_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200 | str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            subject=subject,
            subject_identifier=subject_identifier,
            client=client,
        )
    ).parsed
