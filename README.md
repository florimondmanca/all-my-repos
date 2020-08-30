# all-my-repos

Configuration and autofixers for applying changes across all my repos using [asottile/all-repos](https://github.com/asottile/all-repos).

## Install

* Get yourself a GitHub API key with the appropriate scope, and put it in a `.env` file (git-ignored):

```bash
# .env
GITHUB_API_KEY="..."
```

* Run:

```bash
scripts/install
```

This will generate a git-ignored `all-repos.json` file, then clone repos listed in `repos.json`.

## Usage

```bash
scripts/apply [AUTOFIXER]
```

Example:

```bash
scripts/apply black20
```

## License

MIT
