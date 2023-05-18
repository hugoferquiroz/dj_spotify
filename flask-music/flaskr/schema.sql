DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks (
  id TEXT NOT NULL,
  acousticness REAL NOT NULL,
  danceability REAL NOT NULL,
  duration_ms INT NOT NULL,
  energy REAL NOT NULL,
  instrumentalness REAL NOT NULL,
  key INT NOT NULL,
  liveness REAL NOT NULL,
  loudness REAL NOT NULL,
  mode INT NOT NULL,
  speechiness REAL NOT NULL,
  tempo REAL NOT NULL,
  valence REAL NOT NULL
)