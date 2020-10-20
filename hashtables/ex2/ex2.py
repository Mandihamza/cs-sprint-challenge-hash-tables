class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    itinerary = [None] * length
    ticket_cache = {}

    for ticket in tickets:
        ticket_cache[ticket.source] = ticket.destination
    next = ticket_cache["NONE"]

    for current in range(0, length):
        itinerary[current] = next
        next = ticket_cache[next]
    return itinerary