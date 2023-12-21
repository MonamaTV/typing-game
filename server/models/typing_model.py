from pydantic import BaseModel, NaiveDatetime


class Typing(BaseModel):
    t_id: str
    user_id: str
    wpm: int
    wps: float
    accuracy: float
    time_completed: NaiveDatetime
    date_played: NaiveDatetime
    avg_words_typed: int
