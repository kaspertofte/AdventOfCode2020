def get_rules(data, with_quantifier):
    rules = {}
    for rule in data:
        rule_buffer = rule.split('contain')
        outer_bag = rule_buffer[0][0:len(rule_buffer[0])-6]
        inner_bags = (rule_buffer[1].strip()[0:len(rule_buffer[1])-2]).split(',')
        rules[outer_bag] = []
        if inner_bags[0] == 'no other bags':
            continue
        else:
            for bag in inner_bags:
                stripped_bag = bag.strip()
                quantifier = int(stripped_bag[0])
                color = stripped_bag[1:len(stripped_bag)].split('bag')[0].strip()
                if with_quantifier:
                    rules[outer_bag].append([quantifier, color])
                else:
                    rules[outer_bag].append(color)
    return rules


def get_outer_bags(rules, result, inner_bag):
    for rule in rules:
        if (inner_bag in rules[rule]) and (rule not in result):
            result.append(rule)
            result = get_outer_bags(rules, result, rule)
    return result


def get_total_number_of_bags(rules, outer_bag):
    result = 1
    for bag in rules[outer_bag]:
        result += bag[0] * get_total_number_of_bags(rules, bag[1])
    return result


def challenge1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    rules = get_rules(data, False)

    result = len(get_outer_bags(rules, [], 'shiny gold'))
    return result


def challenge2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    rules = get_rules(data, True)

    # the result includes the outer bag as well.
    # that is subtracted to get the total number of contained bags.
    result = get_total_number_of_bags(rules, 'shiny gold') - 1
    return result
