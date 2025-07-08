import json

# Debug JSON loading issue
filename = 'scores_hard.json'

print("🔍 DEBUGGING JSON LOADING ISSUE")
print("=" * 40)

# Method 1: Check raw file content
print("1. RAW FILE ANALYSIS:")
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"File size: {len(content)} characters")
    print(f"Number of '{{' characters: {content.count('{')}")
    print(f"Number of '}}' characters: {content.count('}')}")

# Method 2: Try to load and catch errors
print("\n2. JSON LOADING TEST:")
try:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"✅ JSON loaded successfully")
        print(f"📊 Records loaded: {len(data)}")
        print(f"📊 Type: {type(data)}")
except json.JSONDecodeError as e:
    print(f"❌ JSON Error: {e}")
    print(f"Error at line {e.lineno}, column {e.colno}")

# Method 3: Load line by line to find the issue
print("\n3. LINE-BY-LINE ANALYSIS:")
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"Total lines in file: {len(lines)}")
    
    # Count lines with opening braces
    brace_lines = [i for i, line in enumerate(lines, 1) if '{' in line]
    print(f"Lines with '{{': {len(brace_lines)}")
    print(f"Brace line numbers: {brace_lines[:10]}...")  # Show first 10

# Method 4: Try manual parsing
print("\n4. MANUAL PARSING TEST:")
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()
    
    # Check if it's valid JSON
    try:
        parsed = json.loads(content)
        print(f"✅ Manual parsing successful: {len(parsed)} records")
        
        # Show first and last records
        print(f"First record: {parsed[0]}")
        print(f"Last record: {parsed[-1]}")
        
    except Exception as e:
        print(f"❌ Manual parsing failed: {e}")

print("\n5. DETAILED INVESTIGATION:")
# Let's see what's actually being loaded
with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f"Loaded {len(data)} records:")
    for i, record in enumerate(data):
        print(f"  {i+1}: Score {record['score']} on {record['date']}")