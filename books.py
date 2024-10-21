import pandas as pd

def create_books_excel(hebrew_text, filename="books_list.xlsx"):
    # Split the input text by new lines
    lines = hebrew_text.split('\n')
    
    # Prepare lists to store the data
    books = []
    authors = []
    availability = []
    
    # Iterate through each line
    for line in lines:
        if line.startswith("עברית") or line.startswith("לא עברית") or line.startswith("בקינדל") or line.startswith("רוסית") or line.startswith("בקשיח"):
            # Skip headers
            continue
        
        # Check for specific availability indicators
        if "יש למטה" in line:
            available = "Available below"
            line = line.replace(" - יש למטה", "")
        elif "✅" in line:
            available = "Read"
            line = line.replace(" ✅", "")
        else:
            available = "Not available"

        # Split the line into book title and author
        if " - " in line:
            book, author = line.split(" - ", 1)
        else:
            book, author = line, ""
        
        # Append the data to lists
        books.append(book.strip())
        authors.append(author.strip())
        availability.append(available)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Book': books,
        'Author': authors,
        'Availability': availability
    })
    
    # Save to Excel
    df.to_excel(filename, index=False)
    return df

# Example input (the text from the user)
hebrew_text = """
לא עברית
אנה קרנינה - לב טולסטוי ✅
העולם של אתמול - סטפן צוויג ✅
האמן ומרגריטה - מיכאל בולגקוב
אל תיגע בזמיר - נל הרפר לי - יש למטה
היום שאיננו כלה - צ'ינגיז אייטמטוב
גר בארץ נוכריה - רוברט היינליין
זאב הערבה - הרמן הסה
100 שנים של בדידות - גבריאל גארסיה מארקס
גטסבי הגדול - פרנסיס סקוט פיצג'רלד
רודף העפיפונים - ח'אלד חוסייני
דפוק וזרוק בפריז ולונדון - ג'ורג' אורוול
שובו של בן המקום - תומס הארדי
הטירה - קפקא
לוליטה - ולדימיר נבוקוב
על העיוורון - ז'וזה סאראמאגו
יוליסס - ג'יימס ג'ויס
חולית - פרנק הרברט
ארץ פלאות קשוחה וסוף העולם - הרוקי מורקמי
1984 - ג'ורג' אורוול
אנקת גבהים - אמילי ברונטה
הוביט - טולקין - יש למטה
מלכוד 22 - גוזף הלר - יש למטה
התפסן בשדה השיפון
יער נורווגי - הרוקי מורקמי

עברית
קופסא שחורה עמוס עוז - יש למטה
מאיר שלו - יש למטה 
אשכול נבו
נויפלד
המקווה האחרון בסיביר 
להעיר אריות - איילת גונדר גושן

בקינדל
Art of hearing heartbeats - jan philipp sendler
The bridges of madison county
The color of our sky
רוסית
Harry Potter
The choice Nicholas sparks
זבל
Every summer after that

בקשיח
חיים קטנים
"""

# Call the function and generate the Excel
df = create_books_excel(hebrew_text)
