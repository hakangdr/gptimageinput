import base64
import requests
import os
import time



folder_path = 'folder/path'
prompt = "prompt"

folder_list = []
for img in os.listdir(folder_path):
    if img.endswith(".jpg"):
        add_to_list = folder_path + img
        folder_list.append(add_to_list)
        
        
# OpenAI API Key
api_key = 'api-key'


for i in folder_list:
  image_path = i
  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
  
  
  image_name = image_path[image_path.rfind("/")+1:]
  
  base64_image = encode_image(image_path)

  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
  }

  payload = {
      "model": "gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  
  output = response.json()['choices'][0]['message']['content']
  print(image_name+"&&"+output)
  
  time.sleep(3)
  
  
