import re
import sys
from pathlib import Path


ATTRIBUTION = re.compile(
    r"\b(?:AI|LLM|Claude|Codex|Copilot|ChatGPT|Gemini|OpenAI|Anthropic)\b"
    r"|generated[- ]by",
    re.IGNORECASE,
)


def main():
    message = Path(sys.argv[1]).read_text(encoding="utf-8")
    if ATTRIBUTION.search(message):
        print("Commit rejected: omit AI attribution and branding from the message.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())