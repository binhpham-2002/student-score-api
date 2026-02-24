from pydantic import BaseModel
from typing import Literal

class StudentInput(BaseModel):
    Hours_Studied: float
    Attendance: float
    Sleep_Hours: float
    Previous_Scores: float
    Tutoring_Sessions: float
    Physical_Activity: float

    Parental_Involvement: Literal["Low", "Medium", "High"]
    Access_to_Resources: Literal["Low", "Medium", "High"]
    Extracurricular_Activities: Literal["Yes", "No"]
    Motivation_Level: Literal["Low", "Medium", "High"]
    Internet_Access: Literal["Yes", "No"]
    Family_Income: Literal["Low", "Medium", "High"]
    School_Type: Literal["Public", "Private"]
    Peer_Influence: Literal["Negative", "Neutral", "Positive"]
    Learning_Disabilities: Literal["Yes", "No"]
    Gender: Literal["Male", "Female"]
