# orbit-auth operations

## Configure authentication explicitly

Basic authentication is disabled unless `BasicAuthenticator` is passed to the ASGI application.
Supply only salted password hashes created by `BasicCredential.from_password`, and load the
password input from protected configuration at startup. The implementation never has default
credentials or persists plaintext passwords.

Use HTTPS end to end or a trusted TLS terminator. Configure Core's trusted forwarded-header policy
before using proxy-provided client information. Do not trust arbitrary forwarding headers.

## Token and provider behavior

Bearer authentication requires a verifier implementation. Use `orbit-auth-jwt` only with explicit
algorithm, issuer, audience, and key configuration. Use `orbit-auth-oauth2` with a shared,
short-lived transaction store and a trusted session binding. Do not log tokens, authorization
codes, state values, PKCE verifiers, credentials, or raw provider responses.

The built-in token revocation store is process-local and is lost on restart. Multi-worker or
distributed deployments need a separately implemented shared store. This repository does not claim
to provide provider discovery transport, JWKS fetching, account recovery, MFA, or identity lifecycle.
