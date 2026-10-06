# ADR 0001: Authentication capability ownership

- Status: Accepted
- Date: 2026-10-06

## Context

Authentication and authorization implementations had accumulated in `orbit-security`, combining
identity capabilities with unrelated cross-cutting security controls. Provider integrations need a
focused, reusable parent contract.

## Decision

Create `orbit-auth` as the capability package for authentication and authorization, including
Basic/bearer mechanisms and provider-neutral identity, token, OAuth/OIDC, JWKS, role, and policy
contracts. Name integrations `orbit-auth-*`. Keep `orbit-security` for cross-cutting controls such
as local HTTP rate limiting. Core retains only generic runtime extension protocols and opaque
request context.

## Consequences

- Applications install authentication capabilities explicitly.
- OAuth2, JWT, and RBAC integrations depend on `orbit-auth`.
- Core remains usable without installing an auth implementation.
- The old pre-alpha imports from `orbit_security` are replaced by `orbit_auth`.
