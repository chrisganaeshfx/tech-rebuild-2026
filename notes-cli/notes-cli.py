import sys
import subprocess

# The AppleScript command written as a Python string
def get_apple_note_content(note_title):
    applescript = f'''
    tell application "Notes"
        if exists note "{note_title}" then
            return plaintext of note "{note_title}"
        else
            return "NOT_FOUND"
        end if
    end tell
    '''
    result = subprocess.run(["osascript", "-e", applescript], capture_output=True, text=True)
    return result.stdout.strip()

def analyze_text(text, note_title):
    # Handle "NOT_FOUND" case
    # Handle note empty case
    if text == "NOT_FOUND":
        print(f"Note titled '{note_title}' not found.")
        return
    if not text:
        print(f"Note titled '{note_title}' is empty.")
        return
    # Slicing text into lines and words
    lines = text.splitlines()
    words = text.split()
    # Print analysis results
    print(f"--- Note Statistics for '{note_title}' ---")
    print(f"Total lines: {len(lines)}")
    print(f"Total words: {len(words)}")
    print(f"First 100 characters: {text[:100].strip()}...")
    print(f"------------ End of Analysis ------------")

def main():
    # If only entered 'python notes-cli-slow.py', len(sys.argv) = 1
    if len(sys.argv) < 2:
        print ("Expected format: python notes_cli.py \"Note Title\"")
        sys.exit(1)

    note_title = " ".join(sys.argv[1:])
    
    print("Connecting to Apple Notes...")
    note_content = get_apple_note_content(note_title)
    analyze_text(note_content, note_title)
    
if __name__ == "__main__":
    main()