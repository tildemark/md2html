import os
import git
import markdown

# Configuration
REPO_URL = 'https://gitea.avegabros.net/AVega-IT/Systems-Design-Documentations.git'
REPO_LOCAL_PATH = '/app/manuals'
MARKDOWN_DIR = os.path.join(REPO_LOCAL_PATH, 'ABAS v3')  # Updated path to Markdown files
OUTPUT_DIR = '/app/html'  # Output directory inside the container

def update_repo():
    """Clones or pulls the latest changes from the Gitea repository."""
    if not os.path.exists(REPO_LOCAL_PATH):
        print(f"Cloning repository from {REPO_URL} to {REPO_LOCAL_PATH}")
        git.Repo.clone_from(REPO_URL, REPO_LOCAL_PATH)
    else:
        print(f"Pulling latest changes in {REPO_LOCAL_PATH}")
        repo = git.Repo(REPO_LOCAL_PATH)
        origin = repo.remotes.origin
        origin.pull()

def convert_markdown(md_filepath, html_filepath):
    """Converts a single Markdown file to HTML."""
    try:
        with open(md_filepath, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()
        html = markdown.markdown(markdown_text, extensions=['fenced_code', 'tables'])
        with open(html_filepath, 'w', encoding='utf-8') as html_file:
            html_file.write(html)
        print(f"Converted: {md_filepath} -> {html_filepath}")
    except Exception as e:
        print(f"Error converting {md_filepath}: {e}")

def process_markdown_files():
    """Processes all Markdown files in the specified directory."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if os.path.exists(MARKDOWN_DIR):
        for filename in os.listdir(MARKDOWN_DIR):
            if filename.endswith('.md'):
                md_filepath = os.path.join(MARKDOWN_DIR, filename)
                html_filename = filename[:-3] + '.html'
                html_filepath = os.path.join(OUTPUT_DIR, html_filename)
                convert_markdown(md_filepath, html_filepath)
    else:
        print(f"Warning: Markdown directory not found: {MARKDOWN_DIR}")

if __name__ == "__main__":
    update_repo()
    process_markdown_files()
    print("Markdown to HTML conversion complete within Docker.")