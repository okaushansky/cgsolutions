#!/usr/bin/env python3

# Baggage class
class TicketAPI():
    def __init__(self, ticket_id) -> None:
        self.ticket_id = ticket_id


    def IsTicketAvailable(self) -> bool:
        pass
    
    def CheckInBaggage(self, destination_id, baggage_id) -> bool:
        pass