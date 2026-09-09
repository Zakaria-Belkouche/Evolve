# Commit Message Standards

- Use the format: `type: short description`
- Use a lowercase type: `feature`, `fix`, `docs`, `refactor`, `test`, or `maintenance`.
- Keep the description clear and short.
- In the short description, write in the imperative mood: "add", "fix", "update", or "debug".
- Describe one focused change per commit.

- For commits related to an issue, always include the issue number: `fix: resolve login timeout (#123)`.
- Omit the issue number only for unrelated maintenance commits.
- To close an issue, include `Closes #123` in the commit message.

## Examples

```bash
git commit -m "feature: add user authentication" -m "(#27)"
```

```bash
git commit -m "fix: login timeout" -m "(#123)"
```

```bash
git commit -m "docs: update README" -m "(#45)"
```

```bash
git commit -m "fix: resolve login timeout" -m "Closes #123"
```