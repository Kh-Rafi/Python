from collections import Counter

if __name__== '__main__':
    s=input().strip()
    
    char_counts= Counter(s)
    shorted_chars = sorted(char_counts.items(), key=lambda x:(-x[1],x[0]))
    
    for char, count in shorted_chars[:3]:
        print(f"{char} {count}")
