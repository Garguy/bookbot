with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
def count_words(book_text):
    words = book_text.split()
    return len(words)

word_count = count_words(file_contents)

def count_chars(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def create_report(text):
    word_count = count_words(text)
    char_counts = count_chars(text)
    
    sorted_chars = sorted(
        [(char, count) for char, count in char_counts.items() if char.isalpha()],
        key=lambda x: x[1],
        reverse=True
    )
    
    report = f"""=== Book Report === Total Word Count: {word_count} 
    Character Frequencies (top 10 letters):"""
    
    for char, count in sorted_chars[:10]:
        percentage = (count / sum(char_counts[c] for c in char_counts if c.isalpha())) * 100
        report += f"\n'{char}': {count} times ({percentage:.1f}%)"
    
    return report
    
def main():
    print(create_report(file_contents))
    #char_count = count_chars(file_contents)
    #print(char_count)

if __name__ == "__main__":
    main()
