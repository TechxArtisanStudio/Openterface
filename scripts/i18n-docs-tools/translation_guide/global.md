# Global Translation Standards for Openterface

## Universal Rules

### Never Translate (Keep in English)

-   **Brand names**: Openterface, TechxArtisan, Crowd Supply, Mini-KVM, uConsole
-   **Technical terms**: KVM, USB, HDMI, VGA, Type-C, plug-and-play, headless, beta
-   **Platforms**: Windows, macOS, Linux, Android, iOS
-   **Services**: GitHub, Discord, Reddit, YouTube, Twitter/X
-   **URLs, file paths, code, commands** - NEVER translate

### Always Translate

-   User-facing text, descriptions, instructions
-   Navigation elements, buttons, CTAs
-   Product descriptions and marketing copy

## Quality Standards

-   **Accuracy**: Maintain technical meaning
-   **Consistency**: Use same terms throughout
-   **Natural flow**: Avoid literal translations
-   **Format preservation**: Keep all markdown structure, links, code blocks

## MkDocs Material Grid Cards Formatting

### CRITICAL: Grid Cards Must Follow Exact Formatting

**Required Format for Grid Cards:**

```markdown
-   :material-icon:{ .lg } **Title**

    ***

    Content text here.
    <img src="..." alt="..." style="max-width: 100%;"/>
```

**Key Requirements:**

-   **List item**: `-   ` (dash + exactly 3 spaces)
-   **Title**: `__Title__` (double underscores, NOT asterisks)
-   **Separator**: `---` (3 dashes, NOT asterisks)
-   **Content indentation**: 4 spaces
-   **Image indentation**: 4 spaces

**Why This Matters:**
MkDocs Material's grid cards renderer is extremely sensitive to formatting. Any deviation breaks the entire grid layout and causes rendering failures across all languages.

## Common Pitfalls

-   Don't translate technical acronyms (KVM, USB, HDMI)
-   Don't modify URLs or file paths
-   Don't break markdown formatting
-   **NEVER change grid card formatting** - use exact English base format
-   Use consistent terminology across all content
