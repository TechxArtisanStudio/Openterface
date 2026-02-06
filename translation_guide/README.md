# Translation Guide System for Openterface

**Concise** translation guides automatically integrated into LLM prompts for consistent translations.

> **⚠️ CRITICAL**: Keep guides under 600 tokens for efficiency. Verbose guides increase costs and reduce quality.

## Quick Start

### File Structure

```
translation_guide/
├── global.md          # Universal rules (~400 tokens)
├── es.md             # Spanish guide (~600 tokens)
├── template.md       # Template for new languages
└── README.md         # This file
```

### How It Works

1. **Prompt Generation**: `python3 openterface-cms/scripts/i18n-docs-tools/generate_prompts.py --docs docs --overwrite`
2. **Auto-Loading**: System loads global + language-specific guides
3. **LLM Translation**: Guides embedded in prompts for consistent translations

## Creating Language Guides

### 1. Copy Template

```bash
cp template.md zh.md  # For Chinese
```

### 2. Customize (CONCISE ONLY)

**Include ONLY**:

- Essential terminology (most common terms)
- Critical style guidelines
- Key patterns (3-4 max)
- Brief checklist (4-5 items)

**AVOID**:

- Verbose explanations
- Repetitive examples
- Long tables
- Cultural discussions

### 3. Test

```bash
python3 openterface-cms/scripts/i18n-docs-tools/generate_prompts.py --docs docs --overwrite
```

## Token Limits & Benefits

| Guide       | Limit | Current | Reduction |
| ----------- | ----- | ------- | --------- |
| `global.md` | <400  | ~400    | 84%       |
| `es.md`     | <600  | ~600    | 85%       |

**Benefits**: Faster processing, lower costs, better focus

## Contributing

### Requirements

- **Understand workflow**: LLM-powered translation with embedded guides
- **Stay concise**: Focus on essential rules only
- **Monitor tokens**: Optimize if exceeding limits
- **Test integration**: Validate with prompt generation

### Do's & Don'ts

**✅ DO**: Bullet points, essential terms, minimal examples
**❌ DON'T**: Verbose text, extensive discussions, long tables

## Workflow Summary

1. Content Creation → 2. Audit → 3. Prompt Generation → 4. Translation → 5. Review → 6. Integration

**Key**: Guides are embedded in LLM prompts - must be concise!
