[![docker stars](https://img.shields.io/docker/stars/guidelacour/clashroyale-player-tracker.svg)](https://hub.docker.com/r/guidelacour/clashroyale-player-tracker/) [![docker pulls](https://img.shields.io/docker/pulls/guidelacour/clashroyale-player-tracker.svg)](https://hub.docker.com/r/guidelacour/clashroyale-player-tracker/) [![docker automated build](https://img.shields.io/docker/automated/guidelacour/clashroyale-player-tracker.svg)](https://hub.docker.com/r/guidelacour/clashroyale-player-tracker/) [![docker build status](https://img.shields.io/docker/build/guidelacour/clashroyale-player-tracker.svg)](https://hub.docker.com/r/guidelacour/clashroyale-player-tracker/)
[![layers](https://images.microbadger.com/badges/image/guidelacour/clashroyale-player-tracker.svg)](https://microbadger.com/images/guidelacour/clashroyale-player-tracker "Get your own image badge on microbadger.com") [![version](https://images.microbadger.com/badges/version/guidelacour/clashroyale-player-tracker.svg)](https://microbadger.com/images/guidelacour/clashroyale-player-tracker "Get your own version badge on microbadger.com")
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This simple script collect player metrics from Clash Royale and insert them 
in InfluxDB.

# How to use

```
docker run --env CR_API_TOKEN=$(cat token) --env INFLUXDB_HOST=influxdb --env INFLUXDB_PORT=8086 --env INFLUXDB_LOGIN=root --env INFLUXDB_PASSWORD=root --env INFLUXDB_DATABASE=clashroyale_stats --env PLAYER_TAG=XXXX --link influxdb --name player guidelacour/clashroyale-player-tracker
```
