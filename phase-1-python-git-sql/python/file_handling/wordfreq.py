try:
    with open("sample.txt","r") as f:
        content = f.read()
        content = content.lower()
        cleaned = ("")
        
        for char in content:
            if char.isalpha() or char.isdigit() or char.isspace():
                cleaned+= char

        words = cleaned.split()
        word_count = {}

    for word in words:
          if word in word_count:
             word_count[word]+=1
          else:
           word_count[word]=1


    print (word_count)

    with open("output.txt", "w") as out:
     for word, count in word_count.items():
        out.write(f"{word}: {count}\n")
        
except FileNotFoundError:
    print("File not found")

