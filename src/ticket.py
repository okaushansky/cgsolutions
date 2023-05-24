#!/usr/bin/env python3

from dal.jsonobject import JsonDBObject


# Ticket class
class Ticket(JsonDBObject):
    def __init__(self) -> None:
        super.__init__(self, 'Ticket', "../data/ticket.json")
        
    def check_ticket(self, id) -> bool:
        ticket = self.getById(id)
        if ticket:
            return True
        else:
            self.logger.error(f'Tiket {id} is not available')
