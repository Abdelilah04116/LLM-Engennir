# Parcours d'Ingénierie LLM : Maîtrise de l'IA, des Grands Modèles de Langage et des Agents

![Banner LLM Engineering](https://via.placeholder.com/800x200?text=LLM+Engineering+Journey)

## 📋 Vue d'ensemble

Ce dépôt contient tous mes projets réalisés dans le cadre du cours Udemy "[LLM Engineering: Master AI, Large Language Models & Agents](https://www.udemy.com/course/llm-engineering)". À travers ce parcours de 8 semaines, je développe progressivement des compétences avancées en ingénierie des grands modèles de langage (LLM), en construisant des applications concrètes et en explorant différentes techniques d'optimisation.

## 🧠 Carte Mentale du Parcours

```
                           +----------------------------+
                           |                            |
                           |   PARCOURS LLM ENGINEERING |
                           |                            |
                           +-------------+--------------+
                                         |
               +------------------------+------------------------+
               |                        |                        |
    +----------v----------+  +---------v----------+  +----------v----------+
    |                     |  |                    |  |                     |
    |  FONDATIONS (1-3)   |  |  AVANCÉ (4-5)     |  |  CAPSTONE (6-8)     |
    |                     |  |                    |  |                     |
    +----------+----------+  +---------+----------+  +----------+----------+
               |                       |                        |
     +---------+---------+   +---------+---------+    +---------+---------+
     |         |         |   |         |         |    |         |         |
+----v---+ +---v----+ +--v---+ +-------v+ +-----v-+ +-v------+ +v------+ +v-------+
|        | |        | |      | |        | |       | |        | |       | |        |
|Projet 1| |Projet 2| |Proj 3| |Projet 4| |Proj 5 | |Projet 6| |Proj 7 | |Projet 8|
|        | |        | |      | |        | |       | |        | |       | |        |
+----+---+ +---+----+ +--+---+ +---+----+ +---+---+ +---+----+ +---+---+ +---+----+
     |         |         |        |          |         |          |         |
     v         v         v        v          v         v          v         v
 Générateur  Support   Minutes  Python     RAG     Prédiction  Fine-    Système
 Brochures   Client    Réunion  vers C++          de Prix    tuning     Multi-
                                                                       Agents
```

## 🎯 Objectifs d'Apprentissage

Durant ce parcours, je vais:

- Maîtriser l'utilisation des modèles LLM de pointe (frontière) et open-source
- Développer des applications IA pratiques avec des cas d'usage concrets
- Implémenter des techniques avancées: RAG, fine-tuning, et workflows agentiques
- Construire des systèmes multimodaux intégrant texte, audio et interfaces utilisateur
- Comparer et évaluer les performances de différentes approches LLM

## 📚 Structure du Cours (8 Semaines)

### 🚀 Phase 1: Fondations LLM (Semaines 1-3)

#### Semaine 1: Générateur Intelligent de Brochures
**Projet 1:** Développement d'un générateur de brochures alimenté par IA qui explore et analyse intelligemment les sites web d'entreprises.

```
+---------------------+     +--------------------+     +----------------------+
|                     |     |                    |     |                      |
| Exploration Web     | --> | Analyse de Contenu | --> | Génération Brochure  |
| (Web Scraping)      |     | (LLM Processing)   |     | (Document Creation)  |
|                     |     |                    |     |                      |
+---------------------+     +--------------------+     +----------------------+
```

**Compétences développées:**
- Web scraping intelligent
- Extraction et structuration de contenu
- Génération de texte persuasif
- Intégration d'API LLM

#### Semaine 2: Agent de Support Client Multimodal
**Projet 2:** Construction d'un agent de support client multimodal pour une compagnie aérienne avec interface utilisateur et appels de fonctions.

```
                    +-------------------------+
                    |                         |
                    |  Interface Utilisateur  |
                    |                         |
                    +------------+------------+
                                 |
                    +------------v------------+
                    |                         |
                    |    Agent Multimodal     |
                    |                         |
                    +------------+------------+
                                 |
        +---------------------+  |  +----------------------+
        |                     |  |  |                      |
        | Traitement Requête  <--+-->  Appels de Fonctions |
        | (Texte/Image/Audio) |     |  (APIs Externes)     |
        +---------------------+     +----------------------+
```

**Compétences développées:**
- Conception d'interfaces conversationnelles
- Intégration multimodale (texte, image)
- Function calling avec LLMs
- Gestion de contexte conversationnel

#### Semaine 3: Outil de Procès-verbaux de Réunions
**Projet 3:** Développement d'un outil qui crée des procès-verbaux et éléments d'action à partir d'audio, utilisant des modèles open et closed-source.

```
+---------------+     +----------------+     +---------------+     +---------------+
|               |     |                |     |               |     |               |
| Entrée Audio  | --> | Transcription  | --> | Extraction    | --> | Génération    |
|               |     | (Speech-to-Text)|     | Points Clés   |     | Procès-verbal |
|               |     |                |     |               |     |               |
+---------------+     +----------------+     +---------------+     +---------------+
```

**Compétences développées:**
- Traitement audio et transcription
- Extraction d'informations pertinentes
- Résumé automatique
- Comparaison modèles propriétaires vs open-source

### 🔍 Phase 2: Techniques Avancées (Semaines 4-5)

#### Semaine 4: Optimisation Python vers C++
**Projet 4:** Développement d'un outil IA qui convertit le code Python en C++ optimisé, améliorant les performances jusqu'à 60 000 fois!

```
+---------------+     +------------------+     +----------------+     +---------------+
|               |     |                  |     |                |     |               |
| Code Python   | --> | Analyse          | --> | Conversion     | --> | Code C++      |
| Source        |     | Sémantique       |     | Optimisée      |     | Optimisé      |
|               |     |                  |     |                |     |               |
+---------------+     +------------------+     +----------------+     +---------------+
                                                      |
                                                      v
                                              +----------------+
                                              |                |
                                              | Validation &   |
                                              | Benchmarking   |
                                              |                |
                                              +----------------+
```

**Compétences développées:**
- Analyse de code source
- Transformation de langages programmation
- Optimisation algorithmique
- Techniques de prompting avancées

#### Semaine 5: Assistant IA avec RAG
**Projet 5:** Construction d'un travailleur IA utilisant RAG (Retrieval-Augmented Generation) pour devenir expert sur toutes les questions relatives à l'entreprise.

```
                    +---------------------+
                    |                     |
                    | Base de Connaissances|
                    | Entreprise          |
                    |                     |
                    +----------+----------+
                                |
            +-----------------+ | +------------------+
            |                 | | |                  |
            | Indexation      | | | Embedding        |
            | Vectorielle     | | | Sémantique       |
            |                 | | |                  |
            +--------+--------+ | +--------+---------+
                     |          |          |
                     |   +------v-------+  |
                     |   |              |  |
                     +-->| Système RAG  |<-+
                         |              |
                         +------+-------+
                                |
                         +------v-------+
                         |              |
                         | Assistant IA |
                         |              |
                         +--------------+
```

**Compétences développées:**
- Construction de base de connaissances
- Implémentation de RAG (Retrieval-Augmented Generation)
- Embeddings sémantiques
- Gestion de contexte et mémoire

### 🏆 Phase 3: Projet Capstone (Semaines 6-8)

#### Semaine 6: Prédiction de Prix avec Modèles Frontier
**Projet 6:** Développement d'un système IA prédisant les prix de produits à partir de courtes descriptions en utilisant des modèles de pointe.

```
+------------------+     +-------------------+     +----------------+
|                  |     |                   |     |                |
| Descriptions     | --> | Extraction        | --> | Prédiction     |
| Produits         |     | Caractéristiques  |     | Prix           |
|                  |     |                   |     |                |
+------------------+     +-------------------+     +----------------+
```

**Compétences développées:**
- Extraction de caractéristiques textuelles
- Modélisation prédictive
- Intégration de modèles frontier

#### Semaine 7: Fine-tuning pour la Prédiction de Prix
**Projet 7:** Exécution d'un modèle open-source fine-tuné pour concurrencer les modèles frontier dans la prédiction de prix.

```
+------------------+     +-------------------+     +----------------+     +-----------------+
|                  |     |                   |     |                |     |                 |
| Dataset          | --> | Préparation       | --> | Fine-tuning    | --> | Évaluation &    |
| Produits/Prix    |     | Données           |     | Modèle         |     | Comparaison     |
|                  |     |                   |     |                |     |                 |
+------------------+     +-------------------+     +----------------+     +-----------------+
```

**Compétences développées:**
- Préparation de données pour fine-tuning
- Techniques de fine-tuning LLM
- Évaluation comparative de modèles
- Optimisation coût/performance

#### Semaine 8: Système Multi-agents Autonome
**Projet 8:** Construction d'un système autonome multi-agents collaborant avec des modèles pour repérer des offres et vous notifier des bonnes affaires.

```
                    +--------------------+
                    |                    |
                    | Orchestrateur      |
                    | Multi-agents       |
                    |                    |
                    +--------+-----------+
                             |
              +--------------|-------------+
              |              |             |
     +--------v----+  +------v------+  +---v----------+
     |             |  |             |  |              |
     | Agent       |  | Agent       |  | Agent        |
     | Recherche   |  | Analyse     |  | Notification |
     |             |  |             |  |              |
     +-------------+  +-------------+  +--------------+
```

**Compétences développées:**
- Architecture multi-agents
- Communication inter-agents
- Prise de décision autonome
- Intégration de systèmes de notification

## 💡 Techniques & Méthodologies

Tout au long du parcours, j'explore ces techniques essentielles:

```
+----------------------+     +----------------------+     +----------------------+
|                      |     |                      |     |                      |
| RAG                  |     | Fine-tuning          |     | Systèmes Agentiques  |
| (Retrieval-Augmented |     | (Adaptation de       |     | (Architecture        |
| Generation)          |     | modèles pré-entraînés)|    | multi-agents)        |
|                      |     |                      |     |                      |
+----------------------+     +----------------------+     +----------------------+
```

### Comparaison des Approches LLM

| Technique | Avantages | Limitations | Cas d'usage |
|-----------|-----------|-------------|-------------|
| **RAG** | - Pas besoin d'entraînement<br>- Informations toujours à jour<br>- Contrôle des sources | - Dépendance à la qualité des documents<br>- Complexité d'implémentation<br>- Latence potentielle | Chatbots documentaires, assistants de recherche |
| **Fine-tuning** | - Performances spécialisées<br>- Réponses plus cohérentes<br>- Réduction de tokens | - Coût d'entraînement<br>- Risque d'oubli<br>- Données d'entraînement nécessaires | Classification spécialisée, génération stylisée |
| **Agents** | - Résolution problèmes complexes<br>- Autonomie<br>- Extensibilité | - Complexité<br>- Difficulté de débogage<br>- Besoin d'orchestration | Automatisation workflow, systèmes décisionnels |

### Comparaison Modèles Frontier vs Open-Source

| Catégorie | Modèles Frontier | Modèles Open-Source |
|-----------|------------------|---------------------|
| **Performance** | Généralement supérieure | En progression rapide |
| **Coût** | Plus élevé (API) | Coûts d'infrastructure |
| **Personnalisation** | Limitée | Très flexible |
| **Latence** | Dépend de l'API | Contrôlable |
| **Sécurité des données** | Politique du fournisseur | Contrôle total |

## 🛠️ Technologies Utilisées

- **Frameworks LLM:** LangChain, LlamaIndex, Transformers
- **Modèles Frontier:** GPT-4, Claude, PaLM
- **Modèles Open-Source:** Llama 3, Mistral, Falcon
- **Langages:** Python, JavaScript, C++
- **Bases de données vectorielles:** Pinecone, Weaviate, Chroma
- **Outils de développement:** Visual Studio Code, Jupyter, Docker

## 📈 Progression du Parcours

| Semaine | Projet | Status | Compétences Acquises |
|---------|--------|--------|----------------------|
| 1 | Générateur de Brochures | 🔄 En cours | Web scraping, Génération de contenu |
| 2 | Agent Support Client | 📅 À venir | Multimodalité, UI, Function calling |
| 3 | Minutes de Réunion | 📅 À venir | Traitement audio, Résumé automatique |
| 4 | Python vers C++ | 📅 À venir | Transformation de code, Optimisation |
| 5 | Assistant RAG | 📅 À venir | RAG, Embeddings, Base de connaissances |
| 6 | Prédiction Prix (Frontier) | 📅 À venir | Extraction de caractéristiques, Prédiction |
| 7 | Prédiction Prix (Fine-tuning) | 📅 À venir | Fine-tuning, Évaluation comparative |
| 8 | Système Multi-agents | 📅 À venir | Architecture multi-agents, Autonomie |

## 📂 Structure du Dépôt

```
llm-engineering-course/
├── week1-brochure-generator/
│   ├── README.md
│   ├── src/
│   ├── data/
│   └── notebooks/
├── week2-customer-support/
│   ├── README.md
│   ├── src/
│   ├── ui/
│   └── api/
├── week3-meeting-minutes/
│   ├── README.md
│   ├── src/
│   ├── models/
│   └── examples/
├── week4-python-to-cpp/
│   ├── README.md
│   ├── src/
│   ├── examples/
│   └── benchmarks/
├── week5-rag-assistant/
│   ├── README.md
│   ├── src/
│   ├── knowledge_base/
│   └── evaluation/
├── week6-price-prediction-frontier/
│   ├── README.md
│   ├── src/
│   ├── data/
│   └── models/
├── week7-price-prediction-finetuned/
│   ├── README.md
│   ├── src/
│   ├── training/
│   └── evaluation/
├── week8-multi-agent-system/
│   ├── README.md
│   ├── src/
│   ├── agents/
│   └── orchestration/
└── README.md (ce fichier)
```

## 🚀 Installation et Configuration

Pour exécuter ces projets localement:

```bash
# Cloner le dépôt
git clone https://github.com/votre-username/llm-engineering-course.git
cd llm-engineering-course

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances communes
pip install -r requirements.txt

# Pour exécuter un projet spécifique
cd week1-brochure-generator
pip install -r requirements.txt
python src/main.py
```

## 📚 Ressources

- [Documentation du cours Udemy](https://www.udemy.com/course/llm-engineering)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)

## 📝 Journal de Progression

### Semaine 1
- Exploration des concepts fondamentaux LLM
- Mise en place de l'environnement de développement
- Implémentation du web scraper intelligent
- Début du développement du générateur de brochures

### À venir...

## 📞 Contact

N'hésitez pas à me contacter pour échanger sur l'ingénierie LLM ou discuter de ces projets!

- GitHub: [votre-username](https://github.com/votre-username)
- LinkedIn: [votre-profil](https://linkedin.com/in/votre-profil)
- Email: votre-email@example.com

---

⭐ Si vous trouvez ce dépôt utile, n'hésitez pas à lui donner une étoile!

*Dernière mise à jour: 4 mai 2025*