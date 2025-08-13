from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            max_length=10,
            json_schema_extra={
                "description": "Nome da categoria",
                "example": "Scale"
            }
        )
    ]


class CategoriaOut(CategoriaIn):
    id: Annotated[
        UUID4,
        Field(
            json_schema_extra={
                "description": "Identificador da Categoria"
            }
        )
    ]