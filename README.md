Real-Time Data Streaming avec Kafka et Spark

Contexte

Notre entreprise a récemment lancé une application de monitoring météo en temps réel permettant aux utilisateurs de suivre l'évolution de la météo à travers différentes régions et villes. Ce projet utilise Apache Kafka pour collecter les données et Apache Spark Streaming pour leur traitement.

Objectifs

Collecte des données : Récupérer les données météorologiques en temps réel depuis l'API OpenWeatherMap et les publier dans un topic Kafka nommé topic-weather.

Traitement des données : Utiliser Spark Streaming pour transformer ces données et produire de nouvelles variables, puis envoyer les résultats dans un second topic Kafka nommé topic-weather-final.

Déploiement d'un pipeline fonctionnel et documenté.
