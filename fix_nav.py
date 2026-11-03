import os

base = "/tmp/nettool_probe/feedback-repo"
os.chdir(base)

langs = [
    ("zh-CN", "简体中文", "README.md"),
    ("en", "English", "lang/README.en.md"),
    ("es", "Español", "lang/README.es.md"),
    ("fr", "Français", "lang/README.fr.md"),
    ("de", "Deutsch", "lang/README.de.md"),
    ("ru", "Русский", "lang/README.ru.md"),
    ("ja", "日本語", "lang/README.ja.md"),
    ("ko", "한국어", "lang/README.ko.md"),
    ("ar", "العربية", "lang/README.ar.md"),
    ("pt", "Português", "lang/README.pt.md"),
    ("it", "Italiano", "lang/README.it.md"),
    ("hi", "हिन्दी", "lang/README.hi.md"),
    ("th", "ไทย", "lang/README.th.md"),
    ("vi", "Tiếng Việt", "lang/README.vi.md"),
    ("id", "Bahasa Indonesia", "lang/README.id.md"),
    ("tr", "Türkçe", "lang/README.tr.md"),
    ("nl", "Nederlands", "lang/README.nl.md"),
]

for code, name, path in langs:
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    lines = [line for line in lines if not line.startswith("[English](README.md)")]

    order = [(code, name, path)] + [item for item in langs if item[0] != code]
    parts = []
    for other_code, other_name, other_path in order:
        if other_code == code:
            parts.append(other_name)
        else:
            if code == "zh-CN":
                url = other_path
            elif other_code == "zh-CN":
                url = "../README.md"
            else:
                url = os.path.basename(other_path)
            parts.append("[%s](%s)" % (other_name, url))

    nav = " · ".join(parts)
    block = ['<div align="center">', '', nav, '', '</div>', '']

    title_index = lines.index("# SilentCodeTeams Feedback")
    new_lines = lines[:title_index] + block + lines[title_index:]

    newline = chr(10)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(newline.join(new_lines).rstrip() + newline)

print("navigation rewritten")
