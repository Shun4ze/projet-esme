from kafka import KafkaProducer
import requests
import json
import time

# ---------------------------------------------------------------------------
# Étape 1 : Configuration
# ---------------------------------------------------------------------------
# Remplacez par votre clé personnelle d'API OpenWeather
API_KEY = '6365575828f48fe0263c2d56aa2e323c'

# Villes à surveiller
CITIES = ["Paris", "London", "Tokyo", "New York", "Port Louis"]

# Nom du topic Kafka utilisé dans votre projet
KAFKA_TOPIC = 'topic-weather'

# Adresse du serveur Kafka
KAFKA_SERVER = 'localhost:9092'

# ---------------------------------------------------------------------------
# Étape 2 : Initialisation du producteur Kafka
# ---------------------------------------------------------------------------
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_SERVER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Sérialisation en JSON
)

# ---------------------------------------------------------------------------
# Étape 3 : Fonction pour récupérer les données météo
# ---------------------------------------------------------------------------
def get_weather_data(city):
    """
    Fonction qui récupère les données météo d'une ville depuis l'API OpenWeather.
    :param city: Nom de la ville
    :return: Données JSON de la météo ou None si une erreur survient
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        return response.json()  # Renvoie les données JSON si la requête réussit
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données météo pour {city}: {e}")
        return None  # Retourne None en cas d'erreur

# ---------------------------------------------------------------------------
# Étape 4 : Envoi des données en continu vers Kafka
# ---------------------------------------------------------------------------
while True:
    for city in CITIES:
        data = get_weather_data(city)  # Récupération des données météo
        if data:
            # Envoi au topic Kafka
            producer.send(KAFKA_TOPIC, key=city.encode('utf-8'), value=data)
            print(f"Données envoyées pour {city}: {data}")
        else:
            print(f"Aucune donnée envoyée pour {city} en raison d'une erreur.")
    time.sleep(60)  # Pause d'une minute entre chaque envoi
