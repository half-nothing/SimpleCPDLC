from dataclasses import dataclass
from typing import Optional


@dataclass
class FlightPlan:
    callsign: str
    dep: str
    arr: str
    aircraft: str
    route: str


class FlightPlanManager:
    _flight_plan: Optional[FlightPlan] = None

    def set_flight_plan(self, flight_plan: FlightPlan):
        self._flight_plan = flight_plan

    @property
    def flight_plan(self) -> Optional[FlightPlan]:
        return self._flight_plan


