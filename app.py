"""Hello-world entry point for the AI engineering journey.

Loads the OpenAI API key from a local `.env` file and runs a single
chat completion as a smoke test for your environment.
"""

from __future__ import annotations

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError


def main() -> int:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "sk-replace-me":
        print(
            "ERROR: OPENAI_API_KEY is not set. "
            "Copy .env.example to .env and add your key.",
            file=sys.stderr,
        )
        return 1

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a concise assistant. Reply in one sentence.",
                },
                {
                    "role": "user",
                    "content": "Say hello to someone starting their AI engineering journey.",
                },
            ],
        )
    except OpenAIError as exc:
        print(f"ERROR calling OpenAI: {exc}", file=sys.stderr)
        return 2

    message = response.choices[0].message.content
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
