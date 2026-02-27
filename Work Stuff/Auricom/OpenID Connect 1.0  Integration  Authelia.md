1.  [Home](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/)
2.  [Integration](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/)
3.  [OpenID Connect 1.0](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/)
4.  OpenID Connect 1.0

Authelia can act as an [OpenID Connect 1.0](https://openid.net/connect/) Provider as part of an open beta. This section details implementation specifics that can be used for integrating Authelia with an [OpenID Connect 1.0](https://openid.net/connect/) Relying Party, as well as specific documentation for some [OpenID Connect 1.0](https://openid.net/connect/) Relying Party implementations.

See the [OpenID Connect 1.0 Provider](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/provider/) and [OpenID Connect 1.0 Clients](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/clients/) configuration guides for information on how to configure the Authelia [OpenID Connect 1.0](https://openid.net/connect/) Provider (note the clients guide is for configuring the registered clients in the provider).

This page is intended as an integration reference point for any implementers who wish to integrate an [OpenID Connect 1.0](https://openid.net/connect/) Relying Party (client application) either as a developer or user of the third party Relying Party.

## Audiences

When it comes to [OpenID Connect 1.0](https://openid.net/connect/) there are effectively two types of audiences. There is the audience embedded in the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) which should always include the requesting clients identifier and audience of the [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4) and [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens). The intention of the audience in the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) is used to convey which Relying Party or client was the intended audience of the token. In contrast the audience of the [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4) is used by the Authorization Server or Resource Server to satisfy an internal policy. You could consider the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) and it’s audience to be a public facing audience, and the audience of other tokens to be private or have private meaning even when the [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4) is using the [JWT Profile for OAuth 2.0 Access Tokens](https://oauth.net/2/jwt-access-tokens/).

It’s also important to note that with the exception of [RFC9068](https://datatracker.ietf.org/doc/html/rfc9068) there is basically no standardized token format for a [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4) or a [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens). Therefore there is no way without the use of the [Introspection](https://datatracker.ietf.org/doc/html/rfc7662) endpoint to determine what audiences these tokens are meant for. It should also be noted that like the scope of a [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens) should effectively never change this also applies to the audience of this token.

For these reasons the audience of the [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4), [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens), and [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) are effectively completely separate and Authelia treats them in this manner. An [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) will always and only have the client identifier of the specific client that requested it per specification, the [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4) will always have the granted audience of the Authorization Flow or last successful Refresh Flow, and the [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens) will always have the granted audience of the Authorization Flow.

For more information about the opaque [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4) default see [Why isn’t the Access Token a JSON Web Token? (Frequently Asked Questions)](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/frequently-asked-questions/#why-isnt-the-access-token-a-json-web-token).

## Scope Definitions

The following scope definitions describe each scope supported and the associated effects including the individual claims returned by granting this scope. By default we do not issue any claims which reveal the users identity which allows administrators semi-granular control over which claims the client is entitled to.

### openid

This is the default scope for [OpenID Connect 1.0](https://openid.net/connect/). This field is forced on every client by the configuration validation that Authelia does.

_**Important Note:** The subject identifiers or `sub` [Claim](https://openid.net/specs/openid-connect-core-1_0.html#Claims) has been changed to a [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122) UUID V4 to identify the individual user as per the [Subject Identifier Types](https://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes) section of the [OpenID Connect 1.0](https://openid.net/connect/) specification. Please use the `preferred_username` [Claim](https://openid.net/specs/openid-connect-core-1_0.html#Claims) instead._

| [Claim](https://openid.net/specs/openid-connect-core-1_0.html#Claims) | JWT Type | Authelia Attribute | Description |
| --- | --- | --- | --- |
| iss | string | hostname | The issuer name, determined by URL |
| jti | string(uuid) | _N/A_ | A [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122) UUID V4 representing the JWT Identifier |
| rat | number | _N/A_ | The time when the token was requested |
| exp | number | _N/A_ | Expires |
| iat | number | _N/A_ | The time when the token was issued |
| auth\_time | number | _N/A_ | The time the user authenticated with Authelia |
| sub | string(uuid) | opaque id | A [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122) UUID V4 linked to the user who logged in |
| scope | string | scopes | Granted scopes (space delimited) |
| scp | array\[string\] | scopes | Granted scopes |
| aud | array\[string\] | _N/A_ | Audience |
| amr | array\[string\] | _N/A_ | An [RFC8176](https://datatracker.ietf.org/doc/html/rfc8176) list of authentication method reference values |
| azp | string | id (client) | The authorized party |
| client\_id | string | id (client) | The client id |

### offline\_access

This scope is a special scope designed to allow applications to obtain a [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens) which allows extended access to an application on behalf of a user. A [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens) is a special [Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4) that allows refreshing previously issued token credentials, effectively it allows the relying party to obtain new tokens periodically.

As per [OpenID Connect 1.0](https://openid.net/connect/) Section 11 [Offline Access](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess) can only be granted during the [Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) or a [Hybrid Flow](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth). The [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens) will only ever be returned at the \[Token Endpoint\] when the client is exchanging their [OAuth 2.0 Authorization Code](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1).

Generally unless an application supports this and actively requests this scope they should not be granted this scope via the client configuration.

It is also important to note that we treat a [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens) as single use and reissue a new [Refresh Token](https://openid.net/specs/openid-connect-core-1_0.html#RefreshTokens) during the refresh flow.

### groups

This scope includes the groups the authentication backend reports the user is a member of in the [Claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims) of the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

| [Claim](https://openid.net/specs/openid-connect-core-1_0.html#Claims) | JWT Type | Authelia Attribute | Description |
| --- | --- | --- | --- |
| groups | array\[string\] | groups | List of user’s groups discovered via [authentication](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/first-factor/introduction/) |

### email

This scope includes the email information the authentication backend reports about the user in the [Claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims) of the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

| Claim | JWT Type | Authelia Attribute | Description |
| --- | --- | --- | --- |
| email | string | email\[0\] | The first email address in the list of emails |
| email\_verified | bool | _N/A_ | If the email is verified, assumed true for the time being |
| alt\_emails | array\[string\] | email\[1:\] | All email addresses that are not in the email JWT field |

### profile

This scope includes the profile information the authentication backend reports about the user in the [Claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims) of the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

| Claim | JWT Type | Authelia Attribute | Description |
| --- | --- | --- | --- |
| preferred\_username | string | username | The username the user used to login with |
| name | string | display\_name | The users display name |

### Special Scopes

The following scopes represent special permissions granted to a specific token.

#### authelia.bearer.authz

This scope allows the granted access token to be utilized with the bearer authorization scheme on endpoints protected via Authelia.

The specifics about this scope are discussed in the [OAuth 2.0 Bearer Token Usage for Authorization Endpoints](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/oauth-2.0-bearer-token-usage/#authorization-endpoints) guide.

## Signing and Encryption Algorithms

[OpenID Connect 1.0](https://openid.net/connect/) and OAuth 2.0 support a wide variety of signature and encryption algorithms. Authelia supports a subset of these.

### Response Object

Authelia’s response objects can have the following signature algorithms:

| Algorithm | Key Type | Hashing Algorithm | Use | JWK Default Conditions | Notes |
| --- | --- | --- | --- | --- | --- |
| RS256 | RSA | SHA-256 | Signature | RSA Private Key without a specific algorithm | Requires an RSA Private Key with 2048 bits or more |
| RS384 | RSA | SHA-384 | Signature | N/A | Requires an RSA Private Key with 2048 bits or more |
| RS512 | RSA | SHA-512 | Signature | N/A | Requires an RSA Private Key with 2048 bits or more |
| ES256 | ECDSA P-256 | SHA-256 | Signature | ECDSA Private Key with the P-256 curve |  |
| ES384 | ECDSA P-384 | SHA-384 | Signature | ECDSA Private Key with the P-384 curve |  |
| ES512 | ECDSA P-521 | SHA-512 | Signature | ECDSA Private Key with the P-521 curve | Requires an ECDSA Private Key with 2048 bits or more |
| PS256 | RSA (MGF1) | SHA-256 | Signature | N/A | Requires an RSA Private Key with 2048 bits or more |
| PS384 | RSA (MGF1) | SHA-384 | Signature | N/A | Requires an RSA Private Key with 2048 bits or more |
| PS512 | RSA (MGF1) | SHA-512 | Signature | N/A | Requires an RSA Private Key with 2048 bits or more |

### Request Object

Authelia accepts a wide variety of request object types. The below table describes these request objects.

| Algorithm | Key Type | Hashing Algorithm | Use | Notes |
| --- | --- | --- | --- | --- |
| none | None | None | N/A | N/A |
| HS256 | HMAC Shared Secret | SHA-256 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `client_secret_jwt` |
| HS384 | HMAC Shared Secret | SHA-384 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `client_secret_jwt` |
| HS512 | HMAC Shared Secret | SHA-512 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `client_secret_jwt` |
| RS256 | RSA | SHA-256 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| RS384 | RSA | SHA-384 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| RS512 | RSA | SHA-512 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| ES256 | ECDSA P-256 | SHA-256 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| ES384 | ECDSA P-384 | SHA-384 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| ES512 | ECDSA P-521 | SHA-512 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| PS256 | RSA (MFG1) | SHA-256 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| PS384 | RSA (MFG1) | SHA-384 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |
| PS512 | RSA (MFG1) | SHA-512 | Signature | [Client Authentication Method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#client-authentication-method) `private_key_jwt` |

## Parameters

The following section describes advanced parameters which can be used in various endpoints as well as their related configuration options.

### Response Types

The following describes the supported response types. See the [OAuth 2.0 Multiple Response Type Encoding Practices](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html) for more technical information. The default response modes column indicates which response modes are allowed by default on clients configured with this flow type value. The value field is both the required value for the `response_type` parameter in the authorization request and the [response\_types](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/clients/#response_types) client configuration option.

| Flow Type | Value | Default [Response Modes](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#response-modes) Values |
| --- | --- | --- |
| [Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) | `code` | `form_post`, `query` |
| [Implicit Flow](https://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth) | `id_token token` | `form_post`, `fragment` |
| [Implicit Flow](https://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth) | `id_token` | `form_post`, `fragment` |
| [Implicit Flow](https://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth) | `token` | `form_post`, `fragment` |
| [Hybrid Flow](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth) | `code token` | `form_post`, `fragment` |
| [Hybrid Flow](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth) | `code id_token` | `form_post`, `fragment` |
| [Hybrid Flow](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth) | `code id_token token` | `form_post`, `fragment` |

### Response Modes

The following describes the supported response modes. See the [OAuth 2.0 Multiple Response Type Encoding Practices](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html) for more technical information. The default response modes of a client is based on the [Response Types](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#response-types) configuration. The value field is both the required value for the `response_mode` parameter in the authorization request and the [response\_modes](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/clients/#response_modes) client configuration option.

| Name | Supported | Value |
| --- | --- | --- |
| [OAuth 2.0 Form Post](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html) | Yes | `form_post` |
| Query String | Yes | `query` |
| Fragment | Yes | `fragment` |
| [JARM](https://openid.net/specs/openid-financial-api-jarm.html#response-mode-jwt) | Yes | `jwt` |
| [Form Post (JARM)](https://openid.net/specs/openid-financial-api-jarm.html#response-mode-form_post.jwt) | Yes | `form_post.jwt` |
| [Query String (JARM)](https://openid.net/specs/openid-financial-api-jarm.html#response-mode-query.jwt) | Yes | `query.jwt` |
| [Fragment (JARM)](https://openid.net/specs/openid-financial-api-jarm.html#response-mode-fragment.jwt) | Yes | `fragment.jwt` |

### Grant Types

The following describes the various [OAuth 2.0](https://oauth.net/2/) and [OpenID Connect 1.0](https://openid.net/connect/) grant types and their support level. The value field is both the required value for the `grant_type` parameter in the access / token request and the [grant\_types](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/clients/#grant_types) client configuration option.

| Grant Type | Supported | Value | Notes |
| --- | --- | --- | --- |
| [OAuth 2.0 Authorization Code](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1) | Yes | `authorization_code` |  |
| [OAuth 2.0 Resource Owner Password Credentials](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.3) | No | `password` | This Grant Type has been deprecated as it’s highly insecure and should not normally be used |
| [OAuth 2.0 Client Credentials](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.4) | Yes | `client_credentials` | If this is the only grant type for a client then the `openid`, `offline`, and `offline_access` scopes are not allowed |
| [OAuth 2.0 Implicit](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.2) | Yes | `implicit` | This Grant Type has been deprecated and should not normally be used |
| [OAuth 2.0 Refresh Token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.5) | Yes | `refresh_token` | This Grant Type should only be used for clients which have the `offline_access` scope |
| [OAuth 2.0 Device Code](https://datatracker.ietf.org/doc/html/rfc8628#section-3.4) | No | `urn:ietf:params:oauth:grant-type:device_code` |  |

### Client Authentication Method

The following describes the supported client authentication methods. See the [OpenID Connect 1.0 Client Authentication](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication) specification and the [OAuth 2.0 - Client Types](https://datatracker.ietf.org/doc/html/rfc8705#section-2.1) specification for more information. The value field is the valid values for the [token\_endpoint\_auth\_method](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/clients/#token_endpoint_auth_method) client configuration option.

| Description | Value | Credential Type | Supported Client Types | Default for Client Type | Assertion Type |
| --- | --- | --- | --- | --- | --- |
| Secret via HTTP Basic Auth Scheme | `client_secret_basic` | Secret | `confidential` | N/A | N/A |
| Secret via HTTP POST Body | `client_secret_post` | Secret | `confidential` | N/A | N/A |
| [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) (signed by secret) | `client_secret_jwt` | Secret | `confidential` | N/A | `urn:ietf:params:oauth:client-assertion-type:jwt-bearer` |
| [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) (signed by private key) | `private_key_jwt` | Private Key | `confidential` | N/A | `urn:ietf:params:oauth:client-assertion-type:jwt-bearer` |
| [OAuth 2.0 Mutual-TLS](https://datatracker.ietf.org/doc/html/rfc8705) | `tls_client_auth` | Private Key | Not Supported | N/A | N/A |
| [OAuth 2.0 Mutual-TLS](https://datatracker.ietf.org/doc/html/rfc8705) (Self Signed) | `self_signed_tls_client_auth` | Private Key | Not Supported | N/A | N/A |
| No Authentication | `none` | N/A | `public` | `public` | N/A |

#### Client Assertion Audience

The client authentication methods which use the JWT Bearer Client Assertions such as `client_secret_jwt` and `private_key_jwt` **require** that the JWT contains an audience (i.e. the `aud` claim) which exactly matches the full URL for the [token endpoint](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#endpoint-implementations) and it **must** be lowercase.

Per the [RFC7523 Section 3: JWT Format and Processing Requirements](https://datatracker.ietf.org/doc/html/rfc7523#section-3) this claim must be compared using [RFC3987 Section 6.2.1: Simple String Comparison](https://datatracker.ietf.org/doc/html/rfc3986#section-6.2.1) and to assist with making this predictable for implementers we ensure the comparison is done against the lowercase form of this URL.

## Authentication Method References

Authelia currently supports adding the `amr` [Claim](https://openid.net/specs/openid-connect-core-1_0.html#Claims) to the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) utilizing the [RFC8176](https://datatracker.ietf.org/doc/html/rfc8176) Authentication Method Reference values.

The values this [Claim](https://openid.net/specs/openid-connect-core-1_0.html#Claims) has are not strictly defined by the [OpenID Connect 1.0](https://openid.net/connect/) specification. As such, some backends may expect a specification other than [RFC8176](https://datatracker.ietf.org/doc/html/rfc8176) for this purpose. If you have such an application and wish for us to support it then you’re encouraged to create a [feature request](https://www.authelia.com/l/fr).

Below is a list of the potential values we place in the [Claim](https://openid.net/specs/openid-connect-core-1_0.html#Claims) and their meaning:

| Value | Description | Factor | Channel |
| --- | --- | --- | --- |
| mfa | User used multiple factors to login (see factor column) | N/A | N/A |
| mca | User used multiple channels to login (see channel column) | N/A | N/A |
| user | User confirmed they were present when using their hardware key | N/A | N/A |
| pin | User confirmed they are the owner of the hardware key with a pin | N/A | N/A |
| pwd | User used a username and password to login | Know | Browser |
| otp | User used TOTP to login | Have | Browser |
| hwk | User used a hardware key to login | Have | Browser |
| sms | User used Duo to login | Have | External |

## Introspection Signing Algorithm

The following table describes the response from the [Introspection](https://datatracker.ietf.org/doc/html/rfc7662) endpoint depending on the [introspection\_signing\_alg](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/clients/#introspection_signed_response_alg).

When responding with the Signed [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) the [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) `typ` header has the value of `token-introspection+jwt`.

| Signing Algorithm | Encoding | Content Type |
| --- | --- | --- |
| `none` | [JSON](https://datatracker.ietf.org/doc/html/rfc8259) | `application/json; charset=utf-8` |
| `RS256` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `RS384` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `RS512` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `PS256` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `PS384` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `PS512` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `ES256` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `ES384` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |
| `ES512` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/token-introspection+jwt; charset=utf-8` |

## User Information Signing Algorithm

The following table describes the response from the [UserInfo](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo) endpoint depending on the [userinfo\_signed\_response\_alg](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/configuration/identity-providers/openid-connect/clients/#userinfo_signed_response_alg).

| Signing Algorithm | Encoding | Content Type |
| --- | --- | --- |
| `none` | [JSON](https://datatracker.ietf.org/doc/html/rfc8259) | `application/json; charset=utf-8` |
| `RS256` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `RS384` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `RS512` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `PS256` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `PS384` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `PS512` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `ES256` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `ES384` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |
| `ES512` | [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) | `application/jwt; charset=utf-8` |

## Endpoint Implementations

The following section documents the endpoints we implement and their respective paths. This information can traditionally be discovered by relying parties that utilize [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html), however this information may be useful for clients which do not implement this.

The endpoints can be discovered easily by visiting the Discovery and Metadata endpoints. It is recommended regardless of your version of Authelia that you utilize this version as it will always produce the correct endpoint URLs. The paths for the Discovery/Metadata endpoints are part of IANA’s well known registration but are also documented in a table below.

These tables document the endpoints we currently support and their paths in the most recent version of Authelia. The paths are appended to the end of the primary URL used to access Authelia. The tables use the url [https://auth.example.com](https://auth.example.com/) as an example of the Authelia root URL which is also the OpenID Connect 1.0 Issuer.

### Well Known Discovery Endpoints

These endpoints can be utilized to discover other endpoints and metadata about the Authelia OP.

| Endpoint | Path |
| --- | --- |
| [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) | [https://auth.example.com/.well-known/openid-configuration](https://auth.example.com/.well-known/openid-configuration) |
| [OAuth 2.0 Authorization Server Metadata](https://datatracker.ietf.org/doc/html/rfc8414) | [https://auth.example.com/.well-known/oauth-authorization-server](https://auth.example.com/.well-known/oauth-authorization-server) |

### Discoverable Endpoints

These endpoints implement OpenID Connect 1.0 Provider specifications.

| Endpoint | Path | Discovery Attribute |
| --- | --- | --- |
| [JSON Web Key Set](https://datatracker.ietf.org/doc/html/rfc7517#section-5) | [https://auth.example.com/jwks.json](https://auth.example.com/jwks.json) | jwks\_uri |
| [Authorization](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint) | [https://auth.example.com/api/oidc/authorization](https://auth.example.com/api/oidc/authorization) | authorization\_endpoint |
| [Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) | [https://auth.example.com/api/oidc/pushed-authorization-request](https://auth.example.com/api/oidc/pushed-authorization-request) | pushed\_authorization\_request\_endpoint |
| [Token](https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint) | [https://auth.example.com/api/oidc/token](https://auth.example.com/api/oidc/token) | token\_endpoint |
| [UserInfo](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo) | [https://auth.example.com/api/oidc/userinfo](https://auth.example.com/api/oidc/userinfo) | userinfo\_endpoint |
| [Introspection](https://datatracker.ietf.org/doc/html/rfc7662) | [https://auth.example.com/api/oidc/introspection](https://auth.example.com/api/oidc/introspection) | introspection\_endpoint |
| [Revocation](https://datatracker.ietf.org/doc/html/rfc7009) | [https://auth.example.com/api/oidc/revocation](https://auth.example.com/api/oidc/revocation) | revocation\_endpoint |

## Security

The following information covers some security topics some users may wish to be familiar with. All of these elements offer hardening to the flows in differing ways (i.e. some validate the authorization server and some validate the client / relying party) which are not essential but recommended.

The [Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) endpoint is discussed in depth in [RFC9126](https://datatracker.ietf.org/doc/html/rfc9126) as well as in the [OAuth 2.0 Pushed Authorization Requests](https://oauth.net/2/pushed-authorization-requests/) documentation.

Essentially it’s a special endpoint that takes the same parameters as the [Authorization](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint) endpoint (including [Proof Key Code Exchange](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#proof-key-code-exchange)) with a few caveats:

1.  The same [Client Authentication](https://datatracker.ietf.org/doc/html/rfc6749#section-2.3) mechanism required by the [Token](https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint) endpoint **MUST** be used.
2.  The request **MUST** use the [HTTP POST method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST).
3.  The request **MUST** use the `application/x-www-form-urlencoded` content type (i.e. the parameters **MUST** be in the body, not the URI).
4.  The request **MUST** occur over the back-channel.

The response of this endpoint is [JSON](https://datatracker.ietf.org/doc/html/rfc8259) encoded with two key-value pairs:

-   `request_uri`
-   `expires_in`

The `expires_in` indicates how long the `request_uri` is valid for. The `request_uri` is used as a parameter to the [Authorization](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint) endpoint instead of the standard parameters (as the `request_uri` parameter).

The advantages of this approach are as follows:

1.  [Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) cannot be created or influenced by any party other than the Relying Party (client).
2.  Since you can force all [Authorization](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint) requests to be initiated via [Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) you drastically improve the authorization flows resistance to phishing attacks (this can be done globally or on a per-client basis).
3.  Since the [Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) endpoint requires all of the same [Client Authentication](https://datatracker.ietf.org/doc/html/rfc6749#section-2.3) mechanisms as the [Token](https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint) endpoint:
    1.  Clients using the confidential [Client Type](https://oauth.net/2/client-types/) can’t have [Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) generated by parties who do not have the credentials.
    2.  Clients using the public [Client Type](https://oauth.net/2/client-types/) and utilizing [Proof Key Code Exchange](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#proof-key-code-exchange) never transmit the verifier over any front-channel making even the `plain` challenge method relatively secure.

#### OAuth 2.0 Authorization Server Issuer Identification

The [RFC9207: OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207) implementation allows relying parties to validate the Authorization Response was returned by the expected issuer by ensuring the response includes the exact issuer in the response. This is an additional check in addition to the `state` parameter.

This validation is not supported by many clients but it should be utilized if it is supported.

#### JWT Secured Authorization Response Mode (JARM)

The [JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)](https://openid.net/specs/oauth-v2-jarm.html) implementation similar to [OAuth 2.0 Authorization Server Issuer Identification](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/integration/openid-connect/introduction/#oauth-20-authorization-server-issuer-identification) allows a relying party to ensure the Authorization Response was returned by the expected issuer and also ensures the response was not tampered with or forged as it is cryptographically signed.

This response mode is not supported by many clients but we recommend it is used if it’s supported.

#### Proof Key Code Exchange

The [Proof Key Code Exchange](https://www.rfc-editor.org/rfc/rfc7636.html) mechanism is discussed in depth in [RFC7636](https://datatracker.ietf.org/doc/html/rfc7636) as well as in the [OAuth 2.0 Proof Key Code Exchange](https://oauth.net/2/pkce/) documentation.

Essentially a random opaque value is generated by the Relying Party and optionally (but recommended) passed through a SHA256 hash. The original value is saved by the Relying Party, and the hashed value is sent in the [Authorization](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint) request in the `code_verifier` parameter with the `code_challenge_method` set to `S256` (or `plain` using a bad practice of not hashing the opaque value).

When the Relying Party requests the token from the [Token](https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint) endpoint, they must include the `code_verifier` parameter again (in the body), but this time they send the value without it being hashed.

The advantages of this approach are as follows:

1.  Provided the value was hashed it’s certain that the Relying Party which generated the authorization request is the same party as the one requesting the token or is permitted by the Relying Party to make this request.
2.  Even when using the public [Client Type](https://oauth.net/2/client-types/) there is a form of authentication on the [Token](https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint) endpoint.