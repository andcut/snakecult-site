# Coding Agent Guidelines

This file provides instructions for automated coding agents working on this repository.

## Commit Messages
- Use short, imperative sentences ("Add feature" not "Added feature").
- Explain the reason for the change when it is not obvious.
- Reference issues or documentation when relevant.

## Required Checks
Before creating a pull request:
1. Run `npm test` and ensure it exits successfully.
2. Attempt to build the site locally via `hugo --minify`. Only proceed if the build succeeds. Capture any build output or errors for the PR notes.

## Project Charter
See `docs/project-charter.md` for the high level goals and workflow of this project. All contributions should align with this charter.

The project aims to create a lightning-fast, static research site focused on the Eve Theory of Consciousness. Key technical requirements include maximizing crawlability through plaintext Markdown and JSON-LD, maintaining zero-latency UX with minimal assets, and ensuring automated publishing through Hugo and Netlify. All code changes should prioritize performance, accessibility, and SEO best practices.
