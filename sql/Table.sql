CREATE TABLE `gcp-weather-data-engineering.weather.weather_history` (
  city STRING,
  country STRING,
  temperature FLOAT64,
  feels_like FLOAT64,
  temp_min FLOAT64,
  temp_max FLOAT64,
  humidity INT64,
  pressure INT64,
  wind_speed FLOAT64,
  weather_main STRING,
  weather_description STRING,
  latitude FLOAT64,
  longitude FLOAT64,
  collected_at TIMESTAMP
)
PARTITION BY DATE(collected_at);