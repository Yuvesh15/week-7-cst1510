"""
RECORD CHECK  -  my version
===========================

Name  :Yuvesh Devason
Lane  :  AI 
Date  :07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.


def parse_line(raw_line):
    line = raw_line.strip()#strips the whole line
    hostname_part, rest = line.split(",", 1)#splitting the hostname
    hostname = hostname_part.strip().lower()
    data = {"hostname": hostname}
    for piece in rest.split(","):
        key, value = piece.split("=")
        data[key.strip()] = float(value.strip())

def status_of(used, total, warning_at=90):
    percent = (used/total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else: return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.
with open("messy_file", "w") as f:
    f.write("  Survey_2026 , rating=4 , age=23  \n")
    f.write("Survey_2025 ,Rating=10 , age=21\n")
    f.write("   Survey_2024 ,   rating=12 ,age=10    \n")
    f.write("    Survey_2023 , Rating=18 , Age=24 \n")
    f.write("Survey_2022 ,    rating=15 ,Age=14 \n")
    f.write(" Survey_2021 ,Rating=21 , Age=29\n")


raw_records = []
with open("messy_file", "r") as file:
    for line in file:
        raw_records.append(line.strip())





# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
total_records = 0 
flagged_records = 0
for raw_record in raw_records:
    total_records +=1
    try:
        data = parse_line(raw_record)
        rating = data.get('rating', 0)
        age = data.get('age', 0)
        status = status_of(rating, 3)
        if status in ("OVER LIMIT", "WARNING", "FLAGGED"):
            flagged_records +=1
            print(f"{data}, status: {status}")
    except ValueError:
        print(f"could not parse: {raw_record}")
print(f"\nSummary: Total records: {total_records}, Flagged Records: {Flagged_records}")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
