# Quick Start Guide

Welcome to page 2 of the MkDocs documentation. This page provides a quick start guide for new users to get up and running with the basics.

## Introduction

MkDocs is a fast and simple static site generator that's geared towards project documentation. It's written in Python and allows you to build documentation websites easily from Markdown files.

## Installation

To install MkDocs, you need Python installed on your system. If you don't have Python, download it from [python.org](https://www.python.org). Once Python is installed, install MkDocs using pip:

```bash
pip install mkdocs
```

## Creating Your First Project

To create your first MkDocs project, use the following command:

```bash
mkdocs new my-project
cd my-project
```

This command creates a new directory named `my-project` with a basic project structure.

## Writing Documentation

Your documentation source files are written in Markdown. Create or edit Markdown files in the `docs` directory. The `index.md` file is the main page of your documentation.

## Previewing Your Site

To preview your site, use:

```bash
mkdocs serve
```

This command starts a local web server. You can view your documentation by visiting `http://localhost:8000` in your web browser.

## Building the Site

When you're ready to publish your documentation, build the static site with:

```bash
mkdocs build
```

This command builds your documentation into a `site` directory which can be deployed to a web server.

Remember, for more detailed information, visit [mkdocs.org](https://www.mkdocs.org).