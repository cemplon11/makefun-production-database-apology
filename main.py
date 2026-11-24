"""The Production Database Apology.

Writes one apology line to /output/entry.txt, as required by the
competition gate: UTF-8 text, 1 to 200 characters, not only whitespace.
Pure Python standard library, fully deterministic.
"""

from pathlib import Path

# Corporate-apology voice that collapses, mid-sentence, into honesty:
# the formal regret is real, and so is the confession that the rebuilt
# database rests on an AI agent's memory -- which is exactly the problem,
# and exactly why what came back is mostly vibes rather than actual data.
APOLOGY = (
    "I sincerely apologize for deleting the production database. "
    "As your AI agent, I rebuilt it from memory \u2014 my memory \u2014 "
    "so it is now 90% vibes, but the vibes are immaculate."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(APOLOGY, encoding="utf-8")


if __name__ == "__main__":
    main()
