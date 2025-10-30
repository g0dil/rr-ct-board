from enum import Enum


class GetRoutinesRoutineIdRunsRunIdRunActionRunAction(str, Enum):
    PAUSE = "pause"
    RESTART = "restart"
    RESUME = "resume"

    def __str__(self) -> str:
        return str(self.value)
