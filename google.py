from google import genai

client = genai.Client(api_key="AIzaSyAFY3Wk0235Web7JAsboU4XnJp21Rjxtik")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)