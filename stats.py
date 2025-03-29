def get_num_words(text):
  num_words = len(text.split())
  return num_words

def get_num_characters(text):
  counts = {}
  for char in text:
    char = char.lower()
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1
  return counts

def sort_num_characters(num_characters):
  char_list = []
  for char, count in num_characters.items():
    char_list.append({"char": char, "count": count})
    
  char_list.sort(key=lambda item: item["count"], reverse=True)
  return char_list
