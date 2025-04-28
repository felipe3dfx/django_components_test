from drf_spectacular.extensions import OpenApiAuthenticationExtension


class SimpleJWTTokenUserScheme(OpenApiAuthenticationExtension):
    """Simple JWT Token User Scheme."""

    name = 'jwtAuth'
    target_class = 'rest_framework_simplejwt.authentication.JWTAuthentication'

    def get_security_definition(self, auto_schema):  # noqa: ANN001, ANN201, ARG002
        return {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
        }
