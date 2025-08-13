from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            max_length=50,
            json_schema_extra={"description": "Nome do atleta", "example": "Joao"}
        )
    ]
    cpf: Annotated[
        str,
        Field(
            max_length=11,
            json_schema_extra={"description": "CPF do atleta", "example": "12345678900"}
        )
    ]
    idade: Annotated[
        int,
        Field(
            json_schema_extra={"description": "Idade do atleta", "example": 25}
        )
    ]
    peso: Annotated[
        PositiveFloat,
        Field(
            json_schema_extra={"description": "Peso do atleta", "example": 75.5}
        )
    ]
    altura: Annotated[
        PositiveFloat,
        Field(
            json_schema_extra={"description": "Altura do atleta", "example": 1.70}
        )
    ]
    sexo: Annotated[
        str,
        Field(
            max_length=1,
            json_schema_extra={"description": "Sexo do atleta", "example": "M"}
        )
    ]
    categoria: Annotated[
        CategoriaIn,
        Field(
            json_schema_extra={"description": "Categoria do atleta"}
        )
    ]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta,
        Field(
            json_schema_extra={"description": "Centro de treinamento do atleta"}
        )
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


class AtletaUpdate(BaseSchema):
    nome: Annotated[
        Optional[str],
        Field(
            None,
            max_length=50,
            json_schema_extra={"description": "Nome do atleta", "example": "Joao"}
        )
    ]
    idade: Annotated[
        Optional[int],
        Field(
            None,
            json_schema_extra={"description": "Idade do atleta", "example": 25}
        )
    ]