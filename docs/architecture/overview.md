# orbit-auth architecture

`orbit-auth` owns provider-neutral authentication and authorization capabilities. It implements
Orbit Core's stable ASGI `Authenticator` and `RouteAuthorizer` protocols while leaving request
dispatch, lifecycle, and context ownership in Core.

```text
Orbit Core: generic ASGI auth hooks and opaque request context
└── orbit-auth: authenticators, principals, token and policy contracts
    ├── orbit-auth-oauth2: OAuth 2.0 flow and PKCE
    ├── orbit-auth-jwt: PyJWT verifier
    └── orbit-auth-rbac: role-to-permission evaluator

orbit-security: cross-cutting controls, such as local HTTP rate limiting
```

The capability contains no provider SDK, network client, credential defaults, or implicit
installation hooks. Basic Auth is opt-in. Bearer authentication delegates verification to an
injected `TokenVerifier`. OAuth/OIDC models and JWKS types define boundaries; provider adapters own
network access, key retrieval, credential material, and provider-specific failures.

## Dependency direction

`orbit-auth` depends on Core's public runtime and ASGI contracts. Core does not depend on this
optional package. Provider integrations depend on `orbit-auth`; applications install only the
integrations they use. `orbit-security` remains independent because its rate limiter is not an
authentication implementation.

## SDK policy

`orbit-auth` is the Python capability API. Provider implementations use the language and SDK best
suited to the integration, while preserving the package contract. A second language implementation
is added only when it has a distinct workload need and conformance evidence.
