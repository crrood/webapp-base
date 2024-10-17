docker volume create mongodb
docker volume create caddy
cd client
npm install
cd ../server
pip3 install -r requirements.txt
cd ..
docker compose build