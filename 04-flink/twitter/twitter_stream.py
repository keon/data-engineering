import tweepy
import json 
from kafka import KafkaProducer


consumer_key="rZvW1pZNuV5I1TpOsou9rB01Z"
consumer_secret="Wb5refprqlksjMWuO7H7IofgDU2k1Q2Aa2MdFiByHLfDMTZKKB"
access_token="1471981519124443137-ZdDegGWOIUn2Zr1OLSWw2HgLlfaMmi"
access_token_secret="48fCS7cGCwYX3l3K5bXWXD6jU86d2mFCWjrV3AiYwyZs5"


producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

class ProcessStream(tweepy.Stream):
  def on_data(self, raw_data):
    data = json.loads(raw_data)
    if "lang" in data and data["lang"] == "ko":
      korean_tweet = {
        "text": data["text"],
        "timestamp_ms": data["timestamp_ms"]
      }
      producer.send("korean-tweets", json.dumps(korean_tweet).encode("utf-8"))

twitter_stream = ProcessStream(
  consumer_key,
  consumer_secret,
  access_token,
  access_token_secret
)

twitter_stream.filter(track=["Twitter"])