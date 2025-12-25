"""A client library for accessing ERCOT Public API Client/Developer Documentation"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
