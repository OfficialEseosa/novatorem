"""Vercel Flask entrypoint — re-exports the app from api/orchestrator.py."""
from api.orchestrator import app

__all__ = ["app"]
