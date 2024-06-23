#🐍 Day 29: Python’s Utility Belt: Must-Know Modules 🐍
import requests
response = requests.get('https://api.github.com/events')
print(response.status_code)
