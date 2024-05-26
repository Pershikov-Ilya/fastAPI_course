from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskADD(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskADD):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int