import requests
from bs4 import BeautifulSoup
from main import get_llm_response  # Réutilisation du connecteur Ollama

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    """
    Une classe utilitaire pour représenter une page web avec titre, texte et liens.
    """

    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"

        # Nettoyage du contenu texte
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""

        # Extraction des liens
        raw_links = [link.get('href') for link in soup.find_all('a')]
        self.links = [link for link in raw_links if link and link.startswith("http")]

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\n\nWebpage Contents:\n{self.text}\n\n"

if __name__ == "__main__":
    url = "https://edwarddonner.com"
    ed = Website(url)

    print("✅ Titre de la page :", ed.title)
    print(f"🔗 Nombre de liens extraits : {len(ed.links)}")
    print(f"🧠 Envoi à Ollama pour résumé...")

    prompt = f"Voici le contenu d'une page web :\n{ed.text[:3000]}\n\nPeux-tu en faire un résumé ?"
    response = get_llm_response(prompt)

    print("\n📄 Résumé du contenu :\n", response)
    print("\n🔗 Liens trouvés sur la page :")
    for link in ed.links[:10]:  # Affiche les 10 premiers liens
        print("-", link)
