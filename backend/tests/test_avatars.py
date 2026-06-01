import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_avatars(client: AsyncClient):
    """Test listing avatars endpoint."""
    response = await client.get("/api/v1/avatars/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_avatar_not_found(client: AsyncClient):
    """Test getting a non-existent avatar."""
    import uuid
    response = await client.get(f"/api/v1/avatars/{uuid.uuid4()}")
    assert response.status_code == 404
