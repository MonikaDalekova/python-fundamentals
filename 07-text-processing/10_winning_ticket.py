def valid_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_winning_symbol in winning_symbols:
        for unterapted_match_lenght in range(10, 5, -1):
            winning_symbol_repetition = current_winning_symbol*unterapted_match_lenght
            if winning_symbol_repetition in left_part and winning_symbol_repetition in right_part:
                if unterapted_match_lenght == 10:
                    return f'ticket "{ticket}" - {unterapted_match_lenght}{current_winning_symbol} Jackpot!'
            return f'ticket "{ticket}" - {unterapted_match_lenght}{current_winning_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(valid_ticket(current_ticket))