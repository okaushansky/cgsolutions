#!/usr/bin/env python3

from dal.jsonobject import JsonDBObject


# Baggage class
class Baggage(JsonDBObject):
    def __init__(self) -> None:
        super.__init__(self, 'Baggage', "../data/baggage.json")
