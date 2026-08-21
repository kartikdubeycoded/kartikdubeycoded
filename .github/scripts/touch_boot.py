import re
from datetime import datetime, timezone

IST = datetime.now(timezone.utc).astimezone()
stamp = f"{IST.strftime('%d %b %Y, %H:%M')} ist"

with open("README.md", encoding="utf-8") as f:
    text = f.read()

pattern = re.compile(r"<!--BOOT:START-->.*?<!--BOOT:END-->", re.DOTALL)
text, n = pattern.subn(f"<!--BOOT:START-->{stamp}<!--BOOT:END-->", text)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(text)

print(f"boot stamp updated ({n} replaced): {stamp}")
