import re


def challenge1(file_path):
    fields, my_ticket, nearby_tickets = read_data(file_path)
    flattend_nearby_tickets = [i for ticket in nearby_tickets for i in ticket]
    result = 0
    for i in flattend_nearby_tickets:
        found = False
        for field in fields.values():
            # print(i, field[0], field[1], i in field[0] or i in field[1])
            if i in field[0] or i in field[1]:
                found = True
                break
        if not found:
            result += i

    return result


def challenge2(file_path):
    fields, my_ticket, nearby_tickets = read_data(file_path)
    valid_tickets = [ticket for ticket in nearby_tickets if is_valid(ticket, fields)]
    valid_field_map = {i: list(fields.keys()) for i in range(len(fields))}
    for ticket in valid_tickets:
        for idx, entry in enumerate(ticket):
            for key in valid_field_map[idx]:
                field = fields[key]
                if (entry not in field[0]) and (entry not in field[1]):
                    valid_field_map[idx].remove(key)
    print([(key, len(valid_field_map[key])) for key in valid_field_map])

    match = [''] * len(fields)
    for idx in range(len(fields)):
        seen = []
        bipartite_matching(idx, match, seen, valid_field_map)

    print(match)
    result = 0
    return result


def bipartite_matching(idx, match, seen, allowed_matchings):
    for field in allowed_matchings[idx]:
        if field not in seen:
            seen.append(field)

            '''If job 'v' is not assigned to 
               an applicant OR previously assigned  
               applicant for job v (which is matchR[v])  
               has an alternate job available.  
               Since v is marked as visited in the  
               above line, matchR[v]  in the following 
               recursive call will not get job 'v' again'''
            if match[idx] == '' or bipartite_matching(match[idx], match, seen):
                match[idx] = field
                return True
    return False


def is_valid(ticket, fields):
    for i in ticket:
        i_found = False
        for field in fields.values():
            if (i in field[0]) or (i in field[1]):
                i_found = True
                break
        if not i_found:
            return False
    return True


def read_data(file_path):
    with open(file_path, "r") as file:
        data = [line.strip() for line in file.read().strip().split("\n")]

    my_ticket_idx = data.index('your ticket:')
    my_ticket = [int(idx) for idx in data[my_ticket_idx + 1].split(",")]

    nearby_ticket_idx = data.index('nearby tickets:')
    nearby_tickets = [[int(idx) for idx in line.split(',')] for line in data[nearby_ticket_idx + 1:]]

    field_pattern = re.compile(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)")
    fields = {match.group(1):
                  (range(int(match.group(2)), int(match.group(3)) + 1),
                   range(int(match.group(4)), int(match.group(5)) + 1))
              for match in map(field_pattern.match, data[0:my_ticket_idx - 1])}

    return fields, my_ticket, nearby_tickets
