#!/usr/bin/env python3
import os
import sys

def analyze_vault(vault_path):
    print(f"Analyzing vault at: {vault_path}")
    total_size = 0
    file_counts = {"md": 0, "images": 0, "pdfs": 0, "other": 0}
    large_files = []

    for root, dirs, files in os.walk(vault_path):
        if ".git" in dirs:
            dirs.remove(".git")
        
        for file in files:
            path = os.path.join(root, file)
            try:
                size = os.path.getsize(path)
                total_size += size
                ext = file.split('.')[-1].lower() if '.' in file else ''
                
                if ext == 'md':
                    file_counts["md"] += 1
                elif ext in ['jpg', 'jpeg', 'png', 'gif', 'svg']:
                    file_counts["images"] += 1
                elif ext == 'pdf':
                    file_counts["pdfs"] += 1
                else:
                    file_counts["other"] += 1
                
                if size > 5 * 1024 * 1024: # > 5MB
                    large_files.append((path, size))
            except Exception as e:
                pass

    print(f"\nSummary:")
    print(f"Total Vault Size: {total_size / (1024*1024):.2f} MB")
    print(f"Notes (.md): {file_counts['md']}")
    print(f"Images: {file_counts['images']}")
    print(f"PDFs: {file_counts['pdfs']}")
    print(f"Other: {file_counts['other']}")
    
    if large_files:
        print("\nLarge Files (>5MB):")
        for path, size in sorted(large_files, key=lambda x: x[1], reverse=True)[:10]:
            print(f"- {path} ({size / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyzer.py <vault_path>")
    else:
        analyze_vault(sys.argv[1])
