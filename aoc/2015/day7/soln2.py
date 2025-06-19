def parse_instruction(instruction):
    parts = instruction.split(" -> ")
    expr, wire = parts[0], parts[1]
    return wire, expr.split()

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def evaluate(wire, wires, cache):
    if is_integer(wire):
        return int(wire)

    if wire in cache:
        return cache[wire]

    expr = wires[wire]
    if len(expr) == 1:
        val = evaluate(expr[0], wires, cache)
    elif len(expr) == 2:
        val = ~evaluate(expr[1], wires, cache) & 0xFFFF
    elif len(expr) == 3:
        a, op, b = expr
        if op == "AND":
            val = evaluate(a, wires, cache) & evaluate(b, wires, cache)
        elif op == "OR":
            val = evaluate(a, wires, cache) | evaluate(b, wires, cache)
        elif op == "LSHIFT":
            val = (evaluate(a, wires, cache) << int(b)) & 0xFFFF
        elif op == "RSHIFT":
            val = evaluate(a, wires, cache) >> int(b)
    else:
        raise Exception(f"Unexpected instruction format: {expr}")

    cache[wire] = val
    return val

def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    wires = {}
    for line in lines:
        wire, expr = parse_instruction(line)
        wires[wire] = expr

    cache = {}
    part1_result = evaluate("a", wires, cache)
    print(f"Part 1: Signal provided to wire a: {part1_result}")

    wires["b"] = [str(part1_result)]
    cache = {}
    part2_result = evaluate("a", wires, cache)
    print(f"Part 2: New signal provided to wire a: {part2_result}")

if __name__ == "__main__":
    main()

