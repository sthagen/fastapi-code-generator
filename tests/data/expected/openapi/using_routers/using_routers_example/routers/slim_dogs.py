# generated by fastapi-codegen:
#   filename:  using_routers_example.yaml
#   timestamp: 2023-04-11T00:00:00+00:00

from __future__ import annotations

from fastapi import APIRouter

from ..dependencies import *

router = APIRouter(tags=['Slim Dogs'])


@router.get('/dogs', response_model=SlimDogs, tags=['Slim Dogs'])
def list_slim_dogs(limit: Optional[int] = None) -> SlimDogs:
    """
    List All Slim Dogs
    """
    pass


@router.post('/dogs', response_model=None, tags=['Slim Dogs'])
def create_slim_dogs() -> None:
    """
    Create a Slim Dog
    """
    pass


@router.get('/dogs/{dog_id}', response_model=Pet, tags=['Slim Dogs'])
def show_dog_by_id(dog_id: str = Path(..., alias='dogId')) -> Pet:
    """
    Info For a Specific Dog
    """
    pass
