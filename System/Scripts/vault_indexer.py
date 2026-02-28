import os
import json
import sys

def index_vault(vault_path):
    index = []
    for root, dirs, files in os.walk(vault_path):
        if ".git" in dirs:
            dirs.remove(".git")
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, vault_path)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    # Basic metadata extraction
                    index.append({
                        "path": rel_path,
                        "size": len(content),
                        "preview": content[:200].replace("\n", " ")
                    })
    
    report_path = os.path.join(vault_path, "Inbox/Index-Report.md")
    with open(report_path, "w") as f:
        f.write("# 📂 Vault Index Report\n\n")
        f.write(f"Total Markdown Files: {len(index)}\n\n")
        f.write("| File Path | Size (chars) | Preview |\n")
        f.write("| --- | --- | --- |\n")
        for item in index[:20]: # Show first 20 for the test
            f.write(f"| {item['path']} | {item['size']} | {item['preview']}... |\n")
    
    print(f"Index complete. Report written to {report_path}")

if __name__ == "__main__":
    index_vault(sys.argv[1])
