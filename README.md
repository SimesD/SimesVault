# 🦞 SimesVault: The Bridge to SimesClaw

Welcome to your "Command Center." This vault is a shared workspace between you (the human) and SimesClaw (the AI). It acts as both a personal knowledge base and a live configuration interface for your assistant.

## 🚀 Getting Started

1. **Clone & Open:** Clone this repo to your desktop and open it as a vault in Obsidian.
2. **Install Obsidian Git:** This is the easiest way to keep your notes synced. Set it to auto-commit/push every 5-10 minutes.
3. **Core Links:** The files in the root (like `SOUL.md`, `USER.md`, `MEMORY.md`) are live-linked to SimesClaw's internal configuration. Editing them here changes how SimesClaw behaves on the VM.

## 📁 Vault Structure

- **`Inbox/`**: Drop new notes, clippings, or draft ideas here for SimesClaw to process.
- **`memory/`**: Contains daily logs and session contexts. SimesClaw updates these automatically.
- **`System/`**: (Recommended) Create a folder for templates, logs, or vault metadata.

## 💡 Pro-Tips for Simon

- **Direct Commands**: You can leave a note in the `Inbox/` titled `Task: [Something]` and ask SimesClaw (via chat) to process it.
- **Memory Maintenance**: If you learn something new or change a preference, update `MEMORY.md`. SimesClaw reads this file at the start of every session to maintain continuity.
- **Personality Shifts**: Want SimesClaw to be more formal or more witty? Edit `SOUL.md` and push the changes.
- **Symbolic Links**: Note that on the VM, the root `.md` files are symlinks. If you replace them with regular files on your desktop and push, the link might break. Try to **edit** the content rather than deleting and re-creating the files.

## 🛠 Troubleshooting

- **Sync Issues**: If SimesClaw isn't picking up your changes, ensure you've pushed them to GitHub. You can always ask SimesClaw to "pull the latest vault changes."
- **Broken Links**: If the core config files stop updating, ask SimesClaw to "repair the symlinks in the vault."

---
*Created by SimesClaw 🦞 — Feb 23, 2026*
