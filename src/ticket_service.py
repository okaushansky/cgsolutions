#!/usr/bin/env python3

from ticket import Ticket
from destination import Destination
from baggage import Baggage
from ticket_api import TicketAPI

# Baggage class
class TicketService(TicketAPI):
    def __init__(self, ticket_id) -> None:
        super.__init(ticket_id)

    def getTicket(self):
        return Ticket().getById(self.ticket_id)
        
    def isTicketAvailable(self) -> bool:
        ticket = self.getTicket()
        if ticket is None:
            return False
        else:
            self.logger.error(f'Tiket {id} is not available')
            return False
        
    def checkDestination(self, destination_id) -> bool:
        destination = Destination().getById(destination_id)
        if not destination:
            self.logger.error(f'Destination {destination_id} is not available')
            return False
        ticket = self.getTicket()
        if destination_id in ticket["destination_ids"]:
            return True
        else:
            self.logger.error(f'Destination is not assigned for ticket {self.ticket_id}')
            return False
            
    def checkInBaggage(self, destination_id, baggage_id) -> bool:
        ticket = self.getTicket()
        if not ticket:
            self.logger.error(f'Tiket {self.ticket_id} is not available')
            return False
        destination = Destination().getById(destination_id)
        if self.checkDestination(destination_id):
            self.logger.error(f'Destination {destination_id} is not available or wrong')
            return False
        
        baggage_dal = Baggage() 
        baggage = baggage_dal.getById(baggage_id)
        if baggage:
            # Baggage already checked in - validate destination and ticket
            if baggage["destination_id"] == destination_id and baggage["ticket_id"] == self.ticket_id and baggage_id in ticket["baggage_ids"]:
                self.logger.info(f'Baggage {baggage_id} already checked in for ticket {self.ticket_id} and destination {destination_id}')
                return True
            else:
                self.logger.error(f'Baggage {baggage_id} is already checked for other ticket/destination ({baggage["ticket_id"]}, {baggage["destination_id"]})')
                return False
        else:
            # Should add here more validations ans add buggage to Buggage table and Tickets table
