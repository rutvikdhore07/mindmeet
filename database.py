### database.py:

```python
import sqlite3

# Create the database and table
def create_db():
    conn = sqlite3.connect('mindmeet.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transcripts (
                        id INTEGER PRIMARY KEY,
                        meeting_id TEXT,
                        content TEXT
                    )''')
    conn.commit()
    conn.close()

create_db()

# Save a transcript
def save_transcript(meeting_id, content):
    conn = sqlite3.connect('mindmeet.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transcripts (meeting_id, content) VALUES (?, ?)", (meeting_id, content))
    conn.commit()
    conn.close()

# Retrieve a transcript
def get_transcript(meeting_id):
    conn = sqlite3.connect('mindmeet.db')
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM transcripts WHERE meeting_id = ?", (meeting_id,))
    data = cursor.fetchone()
    conn.close()
    return data[0] if data else None
```
