import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Verifies that the /health endpoint returns a 200 OK status."""
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "app": "UNI Manager API"}

@pytest.mark.asyncio
async def test_root_endpoint(client: AsyncClient):
    """Verifies that the root endpoint is accessible."""
    response = await client.get("/")
    assert response.status_code == 200
    # We verify the welcome message contains "Jujutsu Kaisen" thematic elements if planned, 
    # but for now just status 200.
