import requests
import re

# Fetch a random quote from the Quotable API
response = requests.get("https://api.quotable.io/random")
data = response.json()
quote = f"“{data['content']}” — {data['author']}"

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Define start and end markers
start_tag = "<!-- quote-start -->"
end_tag = "<!-- quote-end -->"

# Create the new quote section to insert
new_quote = f"{start_tag}\n💬 {quote}\n{end_tag}"

# Replace the old quote section with the new one
updated_content = re.sub(f"{start_tag}.*?{end_tag}", new_quote, content, flags=re.DOTALL)

# Write the updated content back to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Quote fetched:", quote)

