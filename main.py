import random

# SETTINGS
random.seed(42)

base = [
    "admin","root","user"
]

num_variants = [
    "1","2","3","01","02","03","001","002","003","100","101","200","201","301","302","400","500","123","12345"
]

prefixes = [
    "", "x", "y", "z", "a", "b", "c", "alpha", "beta"
]

suffixes = [
    "", "a", "b", "c", "01", "02", "03", "001"
]

separators = [
    "", ".", "-", "_"
]

TARGET = 100000
results = set()
attempts = 0
max_attempts = 2000000

# MAIN CODE
while len(results) < TARGET and attempts < max_attempts:
    attempts += 1
    k = random.choices([2,2,2,3,3,4], weights=[30,30,20,10,5,5])[0]
    parts = []
    for i in range(k):
        w = random.choice(base)
        if random.random() < 0.25:
            w = random.choice(prefixes) + w
        if random.random() < 0.25:
            w = w + random.choice(suffixes)
        if random.random() < 0.20:
            parts.append(random.choice(num_variants))
        parts.append(w)
    sep = random.choice(separators)
    if random.random() < 0.12:
        if len(parts) >= 2:
            core = "".join(parts[:-1])
            candidate = core + "-" + parts[-1]
        else:
            candidate = sep.join(parts)
    else:
        candidate = sep.join(parts)
    candidate = candidate.strip("-_ .")
    while "--" in candidate:
        candidate = candidate.replace("--","-")
    if 2 <= len(candidate) <= 120:
        results.add(candidate.lower())

i = 0
while len(results) < TARGET:
    a = base[i % len(base)]
    b = base[(i+7) % len(base)]
    n = num_variants[i % len(num_variants)]
    if i % 3 == 0:
        cand = f"{a}{b}{n}"
    elif i % 3 == 1:
        cand = f"{a}-{b}-{n}"
    else:
        cand = f"{a}{b}-{n}"
    results.add(cand)
    i += 1

results_list = list(results)
random.shuffle(results_list)

out_path = r"./wordlist.txt"  # Output path
with open(out_path, "w", encoding="utf-8") as f:
    for line in results_list:
        f.write(line + "\n")

preview = "\n".join(results_list[:60])
len_results = len(results_list)
out_path, len_results, preview[:5000]
