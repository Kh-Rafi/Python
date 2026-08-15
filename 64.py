def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string),k):
        sub_string = string[i:i+k]
        unique_chars=[]
        for char in sub_string:
            if char not in unique_chars:
                
                unique_chars.append(char)
        print("".join(unique_chars))
                

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)