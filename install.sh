cd webapp-client
npm install
cd ../webapp-server
pip3 install -r requirements.txt
cd ..
if [ -f ".env" ]; then
    cp .env.example .env
fi