# 🐍 Day 16: What’s in the File? Reading Data! 🐍
# # 🚨 Don't change the code below 👇
#reding a file
with open("diary.txt", "r") as file:
   # print(file.read())
    content = (file.read())
    print(content)
#Line-by-Line Reading
with open("diary.txt", "r") as file:
    for a in file:
        print(a)

'''
Homework: Play Detective
Message Decoder: Write a program to read a file and look for specific keywords or patterns. Maybe it's a secret message!'''
with open("diary.txt", "r") as file:
    for a in file:
      if "classified" in a:
        print(a)

   #Word Counter: Read a text file and count how many times each word appears

def word_count(filename):
  """
  This function counts the frequency of each word in a text file.

  Args:
      filename: The path to the text file.

  Returns:
      A dictionary where keys are words and values are their frequencies.
  """
  # Initialize an empty dictionary to store word counts
  word_counts = {}

  # Read the text file line by line
  with open(filename, 'r') as file:
    for line in file:
      # Convert the line to lowercase and split it into words
     # words = line.lower().split()
       words = line.split()

      # Remove punctuation from each word
    words = [word.strip(".,?!:;-'") for word in words]

      # Count the occurrences of each word
    for word in words:
        if word:  # Check if the word is not empty after removing punctuation
          if word in word_counts:
            word_counts[word] += 1
          else:
            word_counts[word] = 1

  return word_counts

# Example usage
filename = "diary.txt"  # Replace with the actual filename
word_counts = word_count(filename)

# Print the word frequencies
for word, count in word_counts.items():
  print(f"{word}: {count}")
