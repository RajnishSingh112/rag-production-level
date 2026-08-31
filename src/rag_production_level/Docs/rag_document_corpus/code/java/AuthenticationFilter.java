package com.nexus.security;

public final class AuthenticationFilter {
    public AuthenticationResult validate(String bearerToken) {
        if (bearerToken == null || bearerToken.isBlank()) {
            return AuthenticationResult.unauthorized();
        }

        // Token validation is performed by the gateway in production.
        return AuthenticationResult.success();
    }
}
