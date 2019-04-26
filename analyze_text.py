# Remember to reach out for help after your own due diligence

def analyze_text(text):
  letter_count = 0
  for char in text:
      if char.isalpha() == True:
          letter_count += 1  
  num_e = text.count("e") + text.count("E")
  percent_e = ((num_e) / (letter_count))
  return "The text contains " + str(letter_count) + " alphabetic characters, of which " + str(num_e) + " (" + str((format(percent_e, '.2%'))) + ") are 'e'."

    # Your code here
