from pydantic import BaseModel
from typing import Optional


class JobData(BaseModel):
    apply_before: str
    company_name: str
    job_type: Optional[str] = None
    level: Optional[str] = None
    location: Optional[str] = None
    no_of_vacancy: Optional[str] = None
    offered_salary: Optional[str] = None
