
import google.generativeai as genai
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'




GOOGLE_API_KEY=""
genai.configure(api_key=GOOGLE_API_KEY)



model2 = genai.GenerativeModel('gemini-1.0-pro')


def gemini_pro_test(prompt):
    try:
        # print("Gemini_pro..... Ask the question.....")
        query =prompt
        # print("Generating content... Please wait.")
        response = model2.generate_content(query)
        return response.text
    except :
        return []
      

