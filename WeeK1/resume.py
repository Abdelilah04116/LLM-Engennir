import requests
from bs4 import BeautifulSoup
from initialisation import get_llm_response  # 🔁 Import depuis main.py

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

if __name__ == "__main__":
    url = "https://cnn.com"
    site = Website(url)

    print(f"✅ Titre : {site.title}\n")

    prompt = f"Voici le contenu d'une page web :\n{site.text[:3000]}\n\nPeux-tu résumer ce contenu en quelques lignes ?"
    print("⏳ Envoi au modèle LLaMA3 via Ollama...")
    response = get_llm_response(prompt)

    print("\n📄 Résumé du contenu :\n", response)
