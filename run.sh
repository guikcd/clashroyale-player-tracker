docker build -t player:0.1 .
bash ./tests.sh
docker stop player-gui && docker rm -f player-gui
docker run --restart always --env CR_API_TOKEN=$(cat token) --env INFLUXDB_HOST=influxdb -e INFLUXDB_PORT=8086 -e INFLUXDB_LOGIN=root -e INFLUXDB_PASSWORD=root -e INFLUXDB_DATABASE=clashroyale_stats -e PLAYER_TAG=2G00222J --link influxdb --name player-gui --detach player:0.1
docker logs player-gui
