# <img src="https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg" width="35px" alt="Gemini Icon" /> GeminiKit

**GeminiKit** is an unofficial Python wrapper developed through reverse-engineering. This tool utilizes cookie values to interact with Google Gemini for testing purposes.

<br>

## Installation

To install GeminiKit, you can use pip:

```bash
pip install -U geminikit
```
or

```bash
pip install git+https://github.com/rekcah-pavi/geminikit
```

***
 ## Get Cookie File
<details>
 

For a detailed video guide, [click here](https://youtu.be/IUCJg2KWcJs).

### 1. Close All Tabs

Ensure all tabs are closed in Google Chrome.

### 2. Access Network Export

- Open a new tab and navigate to `chrome://net-export/`.

### 3. Configure Logging Settings

- Check the box labeled `Include cookies and credentials`.
- Set the `Maximum log size` to `1 MB`.
- Click the `Start logging` button.

### 4. Perform Actions

- Open a new tab and go to [gemini.google.com](https://gemini.google.com).
- Log in to your Gemini account.
- Send a sample message and wait for Gemini's response.

### 5. Stop Logging

- Return to the logging tab and click the `Stop logging` button.

### 6. Retrieve Cookies

- The cookies will be saved in a JSON file.

### 7. Extract Cookies from File

```python
from geminikit import get_cookies_from_file

with open("chrome-net-export-log.json", 'r') as f:
    cookies = get_cookies_from_file(f.read())

print(cookies)
```

</details>

***

## Usage

### Setup Gemini

```python
from geminikit import get_cookies_from_file
from geminikit import Gemini

with open("chrome-net-export-log.json", 'r') as f:
    cookies = get_cookies_from_file(f.read())

gemini = Gemini(cookies)
```

### Ask a Message

```python
res = gemini.ask("hello")
print(res['text'])
```

### Ask continuous message
```python
user = None
while True:
 text = input("Ask: ")
 res = gemini.ask(text,user=user)
 user = res
 print(res['text'])
```

### Text to Voice

```python
res = gemini.speech("hello")
with open("a.wav", "wb") as f:
    f.write(res)
```

### Ask with Photo

```python
with open("cat.jpg", "rb") as f:
    img_link = gemini.upload_image(f.read())

photo = ['cat.jpg', img_link]  # photo name (if not available, use 'none.jpg'), link

res = gemini.ask("What is in this photo?", photo=photo)
print(res['text'])
```

### Save Response Images

```python
res = gemini.ask("send me some wallpapers")

print(res['text'])

#Or You can access URLs directly
for url in res['image_urls']:
    img_name  = url.split("/")[-1]
    img_bytes = gemini.get_img_bytes(url)
    with open(img_name, 'wb') as f:
        f.write(img_bytes)
```

### Save Generated Images

```python
res = gemini.ask("Generate an image of a cat holding a rose.")

print(res['text'])

for url in res['generated_image_urls']:
    img_name  = url.split("/")[-1][:10] + ".png"
    img_bytes = gemini.get_img_bytes(url)
    with open(img_name, 'wb') as f:
        f.write(img_bytes)
```

### Get Sharable URL

```python
res = gemini.ask("Hi")
url = gemini.share(res['conversation_id'], res['response_id'], res['choice_id'], res['req_id'], res['fsid'], title="test by me")
print(url)
```
