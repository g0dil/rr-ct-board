from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.issue_sign_up_token_body import IssueSignUpTokenBody
from ...models.issue_sign_up_token_response_200 import IssueSignUpTokenResponse200
from ...models.issue_sign_up_token_response_400 import IssueSignUpTokenResponse400
from ...types import Response


def _get_kwargs(
    group_id: int,
    *,
    body: IssueSignUpTokenBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/publicgroups/{group_id}/token".format(
            group_id=group_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400 | None:
    if response.status_code == 200:
        response_200 = IssueSignUpTokenResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = IssueSignUpTokenResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueSignUpTokenBody,
) -> Response[IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400]:
    """Issue new sign up token.

     The sign up token is needed to sign up to a public or open group using the form. The token can be
    issued by person id or for an email. If the person id is given, the token and the form url is
    returned. If an eMail address is given, the system checks if a user exists with that eMail, if s/he
    is already in the group or if the eMail is new to the system, hence a new user account would be
    necessary. The mail is sent with detailed information and a link to the sign up form.

    Args:
        group_id (int):
        body (IssueSignUpTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueSignUpTokenBody,
) -> IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400 | None:
    """Issue new sign up token.

     The sign up token is needed to sign up to a public or open group using the form. The token can be
    issued by person id or for an email. If the person id is given, the token and the form url is
    returned. If an eMail address is given, the system checks if a user exists with that eMail, if s/he
    is already in the group or if the eMail is new to the system, hence a new user account would be
    necessary. The mail is sent with detailed information and a link to the sign up form.

    Args:
        group_id (int):
        body (IssueSignUpTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueSignUpTokenBody,
) -> Response[IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400]:
    """Issue new sign up token.

     The sign up token is needed to sign up to a public or open group using the form. The token can be
    issued by person id or for an email. If the person id is given, the token and the form url is
    returned. If an eMail address is given, the system checks if a user exists with that eMail, if s/he
    is already in the group or if the eMail is new to the system, hence a new user account would be
    necessary. The mail is sent with detailed information and a link to the sign up form.

    Args:
        group_id (int):
        body (IssueSignUpTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueSignUpTokenBody,
) -> IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400 | None:
    """Issue new sign up token.

     The sign up token is needed to sign up to a public or open group using the form. The token can be
    issued by person id or for an email. If the person id is given, the token and the form url is
    returned. If an eMail address is given, the system checks if a user exists with that eMail, if s/he
    is already in the group or if the eMail is new to the system, hence a new user account would be
    necessary. The mail is sent with detailed information and a link to the sign up form.

    Args:
        group_id (int):
        body (IssueSignUpTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IssueSignUpTokenResponse200 | IssueSignUpTokenResponse400
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
