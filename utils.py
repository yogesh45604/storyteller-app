def create_prompt(genre: str, characters: str, sections: int) -> str:
    return (
        f"Write a {sections}-paragraph {genre} story that includes these characters: {characters}. "
        "Start with a short summary or preface, then number each paragraph in the story."
    )

def parse_story(raw_output: str):
    lines = raw_output.strip().split("\n")
    summary = []
    paragraphs = []

    for line in lines:
        if line.strip().startswith("1.") or line.strip().startswith("1 "):
            break
        summary.append(line)

    current_paragraph = []
    for line in lines[len(summary):]:
        if line.strip().startswith(tuple(str(i) for i in range(1, 21))):
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph).strip())
                current_paragraph = []
            current_paragraph.append(line)
        else:
            current_paragraph.append(line)
    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph).strip())

    return "\n".join(summary).strip(), paragraphs
