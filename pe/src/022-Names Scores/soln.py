def name_score(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

def compute_total_name_scores(filename):
    with open(filename, 'r') as file:
        names = file.read().replace('"', '').split(',')
        
    names.sort()
    
    total_score = sum((i + 1) * name_score(name) for i, name in enumerate(names))
    return total_score
filename = '0022_names.txt'
print(f"Total of all name scores: {compute_total_name_scores(filename)}")

