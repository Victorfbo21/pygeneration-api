from pydantic import BaseModel, Field
import uuid

class Service(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(...)
    value: float = Field(...)
    description: str = Field(...)
    category: str = Field(...)
    