def look_and_say(sequence, steps):
    for z in range(steps):
        i = 0
        next_sequence = []
        while i < len(sequence):
            cnt = 1
            while i + 1 < len(sequence) and sequence[i + 1] == sequence[i]:
                cnt += 1
                i += 1
            next_sequence.append(str(cnt))
            next_sequence.append(sequence[i])
            i += 1
        sequence = ''.join(next_sequence)
    return len(sequence)

ip = "3113322113"
steps = 40

result_length = look_and_say(ip, steps)
print(result_length)




ip = "3113322113"
steps = 50

result_length = look_and_say(ip, steps)
print(result_length)
