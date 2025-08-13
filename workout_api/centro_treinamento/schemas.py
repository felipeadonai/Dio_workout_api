from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            max_length=20,
            json_schema_extra={
                "description": "Nome do centro de treinamento",
                "example": "CT King"
            }
        )
    ]
    endereco: Annotated[
        str,
        Field(
            max_length=60,
            json_schema_extra={
                "description": "Endereço do centro de treinamento",
                "example": "Rua X, Q02"
            }
        )
    ]
    proprietario: Annotated[
        str,
        Field(
            max_length=30,
            json_schema_extra={
                "description": "Proprietário do centro de treinamento",
                "example": "Marcos"
            }
        )
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            max_length=20,
            json_schema_extra={
                "description": "Nome do centro de treinamento",
                "example": "CT King"
            }
        )
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[
        UUID4,
        Field(
            json_schema_extra={
                "description": "Identificador do centro de treinamento"
            }
        )
    ]