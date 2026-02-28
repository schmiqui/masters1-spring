def wrap(text, width):
    if width <= 0:
        return ""

    lines = []

    for paragraph in text.split("\n"):
        if paragraph.strip() == "":
            lines.append("")
            continue

        words = paragraph.split()
        actual = ""

        for word in words:
            if len(word) > width:
                if actual:
                    lines.append(actual)

                i = 0
                while i + width < len(word):
                    lines.append(word[i:i + width])
                    i += width
                actual = word[i:]
                continue

            actual_with_word = (actual + " " + word).strip()
            if len(actual_with_word) <= width:
                actual = actual_with_word
            else:
                if actual:
                    lines.append(actual)
                actual = word

        if actual:
            lines.append(actual)

    return "\n".join(lines)