from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime


class BaseSchema(BaseModel):
    model_config = {
        "extra": "forbid",
        "from_attributes": True
    }


class OutMixin(BaseSchema):
    id: Annotated[
        UUID4,
        Field(
            json_schema_extra={
                "description": "Identificador"
            }
        )
    ]
    created_at: Annotated[
        datetime,
        Field(
            json_schema_extra={
                "description": "Data de criação"
            }
        )
    ]