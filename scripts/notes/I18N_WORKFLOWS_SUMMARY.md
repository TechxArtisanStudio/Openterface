# i18n Workflows Summary

This document provides visual summaries of the key internationalization workflows using Mermaid diagrams.

## Table of Contents

1. [Configuration Flow](#configuration-flow)
2. [Static Page Generation Flow](#static-page-generation-flow)
3. [Documentation Translation Flow](#documentation-translation-flow)
4. [Complete i18n Workflow Overview](#complete-i18n-workflow-overview)
5. [File Hierarchy](#file-hierarchy)

---

## Configuration Flow

How `lang.yml` (Single Source of Truth) flows to all tools and configurations.

```mermaid
flowchart TD
    A[lang.yml<br/>Single Source of Truth] --> B[manage_i18n.py]
    A --> C[i18n-shared/lang_loader.py<br/>I18nConfig Class]
    
    B --> D[mkdocs.yml<br/>i18n plugin config]
    
    C --> E[i18n-site-tools<br/>Static page generation]
    C --> F[i18n-docs-tools<br/>Translation management]
    C --> G[url-audit-tool<br/>Language validation]
    C --> H[update-post-tool<br/>Language config]
    C --> I[youtube-tools<br/>Language config]
    
    style A fill:#ffd700,stroke:#333,stroke-width:3px
    style C fill:#90EE90,stroke:#333,stroke-width:2px
    style D fill:#87CEEB,stroke:#333,stroke-width:2px
```

---

## Static Page Generation Flow

Process of generating multilingual static HTML pages from templates.

```mermaid
flowchart LR
    A[HTML Templates<br/>with data-i18n-key] --> D[generate_static_pages.py]
    B[Translation JSON<br/>home.json, videos.json, forms.json] --> D
    C[lang.yml<br/>via I18nConfig] --> D
    
    D --> E[Validate Languages]
    E --> F[Replace data-i18n-key]
    F --> G[Generate HTML per language]
    
    G --> H[docs/overrides/<br/>home.html, home.zh.html, ...]
    G --> I[docs/partials/<br/>videos.html, videos.zh.html, ...]
    G --> J[docs/overrides/partials/<br/>hreflang.html]
    
    style A fill:#FFE4B5,stroke:#333,stroke-width:2px
    style B fill:#E6E6FA,stroke:#333,stroke-width:2px
    style C fill:#FFD700,stroke:#333,stroke-width:2px
    style D fill:#90EE90,stroke:#333,stroke-width:3px
```

---

## Documentation Translation Flow

Workflow for managing and auditing Markdown file translations.

```mermaid
flowchart TD
    A[Markdown Files<br/>docs/**/*.md] --> B[audit_translations.py]
    
    B --> C[i18n_audit.csv<br/>Coverage Matrix]
    
    C --> D[generate_prompts.py]
    C --> E[cleanup_translations.py]
    
    D --> F[prompts/*.llm-task.txt<br/>Translation Tasks]
    
    E --> G[Removes Orphaned<br/>Translations]
    
    H[workflow.py<br/>Unified Manager] --> B
    H --> D
    H --> E
    
    style A fill:#FFE4B5,stroke:#333,stroke-width:2px
    style B fill:#90EE90,stroke:#333,stroke-width:2px
    style C fill:#87CEEB,stroke:#333,stroke-width:2px
    style H fill:#FFD700,stroke:#333,stroke-width:3px
```

---

## Complete i18n Workflow Overview

High-level view of the entire i18n system architecture.

```mermaid
flowchart TB
    subgraph SSOT["Single Source of Truth"]
        A[lang.yml<br/>Language definitions<br/>Navigation translations<br/>Site names]
    end
    
    subgraph Config["Configuration Layer"]
        B[manage_i18n.py]
        C[I18nConfig Class<br/>i18n-shared/lang_loader.py]
    end
    
    subgraph StaticGen["Static Page Generation"]
        D[Templates + JSON]
        E[generate_static_pages.py]
        F[HTML Output<br/>home.*.html<br/>videos.*.html<br/>hreflang.html]
    end
    
    subgraph DocsMgmt["Documentation Management"]
        G[Markdown Files]
        H[audit_translations.py]
        I[generate_prompts.py]
        J[cleanup_translations.py]
        K[Coverage Reports<br/>Translation Tasks]
    end
    
    subgraph OtherTools["Supporting Tools"]
        L[url-audit-tool]
        M[update-post-tool]
        N[youtube-tools]
    end
    
    A --> B
    A --> C
    B --> O[mkdocs.yml]
    
    C --> D
    C --> G
    C --> L
    C --> M
    C --> N
    
    D --> E
    E --> F
    
    G --> H
    H --> I
    H --> J
    I --> K
    J --> K
    
    style A fill:#ffd700,stroke:#333,stroke-width:4px
    style C fill:#90EE90,stroke:#333,stroke-width:3px
    style E fill:#87CEEB,stroke:#333,stroke-width:2px
    style H fill:#87CEEB,stroke:#333,stroke-width:2px
```

---

## File Hierarchy

Visual representation of the key file structure.

```mermaid
graph TD
    A[Project Root] --> B[docs/assets/i18n-sites/]
    A --> C[scripts/]
    A --> D[mkdocs.yml]
    
    B --> E[lang.yml<br/>⭐ Single Source of Truth]
    B --> F[home.json]
    B --> G[videos.json]
    B --> H[forms.json]
    
    C --> I[i18n-shared/]
    C --> J[i18n-site-tools/]
    C --> K[i18n-docs-tools/]
    C --> L[manage_i18n.py]
    
    I --> M[lang_loader.py<br/>I18nConfig]
    
    J --> N[generate_static_pages.py]
    J --> O[templates/]
    
    K --> P[audit_translations.py]
    K --> Q[generate_prompts.py]
    K --> R[cleanup_translations.py]
    K --> S[workflow.py]
    
    E -.->|read by| M
    E -.->|synced to| D
    E -.->|validated by| N
    E -.->|validated by| P
    
    style E fill:#ffd700,stroke:#333,stroke-width:3px
    style M fill:#90EE90,stroke:#333,stroke-width:2px
    style D fill:#87CEEB,stroke:#333,stroke-width:2px
```

---

## Quick Reference: Adding a New Language

Step-by-step workflow for adding support for a new language.

```mermaid
flowchart TD
    A[1. Edit lang.yml<br/>Add language entry] --> B[2. Run manage_i18n.py add<br/>Sync to mkdocs.yml]
    B --> C[3. Add translations to JSON<br/>home.json, videos.json, forms.json]
    C --> D[4. Update language-select.js<br/>Frontend switcher]
    D --> E[5. Run generate_all_i18n.py<br/>Regenerate static pages]
    
    style A fill:#FFE4B5,stroke:#333,stroke-width:2px
    style B fill:#90EE90,stroke:#333,stroke-width:2px
    style E fill:#87CEEB,stroke:#333,stroke-width:2px
```

---

## Build Process Dependencies

Required steps before running MkDocs build.

```mermaid
flowchart LR
    A[1. lang.yml exists] --> B[2. manage_i18n.py<br/>syncs to mkdocs.yml]
    B --> C[3. generate_static_pages.py<br/>creates HTML files]
    C --> D[4. hreflang.html generated]
    D --> E[MkDocs Build]
    
    style A fill:#ffd700,stroke:#333,stroke-width:3px
    style E fill:#87CEEB,stroke:#333,stroke-width:3px
```

---

For detailed information about each component and workflow, see [I18N_WORKFLOW_AND_HIERARCHY.md](./I18N_WORKFLOW_AND_HIERARCHY.md).

