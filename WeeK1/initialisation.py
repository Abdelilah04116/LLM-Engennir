"""
Dans ce script, nous allons apprendre à initialiser et à nous connecter à Ollama,
notre LLM local (comme LLaMA 2 ou LLaMA 3). Nous découvrirons également les types de prompts
que l’on peut utiliser pour interagir efficacement avec le modèle.
Ce script servira de base pour expérimenter des requêtes simples et avancées avec un LLM local.
"""

# === Configuration ===
OPENAI_API_KEY = "your-openai-api-key"  # Remplace par ta clé OpenAI si besoin
USE_OLLAMA = True                       # Met à False pour utiliser OpenAI
OLLAMA_MODEL = "llama3"                 # Nom du modèle Ollama

# === Fonction pour interroger le LLM ===
def get_llm_response(prompt: str) -> str:
    if USE_OLLAMA:
        import requests
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
            )
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            return f"Erreur lors de la requête Ollama : {e}"
    else:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=OPENAI_API_KEY)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Erreur lors de la requête OpenAI : {e}"

# === Exemple d'utilisation ici on a fait un appele a notre llm  ===
if __name__ == "__main__":
    prompt = "Explique-moi le fonctionnement des réseaux de neurones"
    response = get_llm_response(prompt)
    print("Réponse du LLM :\n", response)
