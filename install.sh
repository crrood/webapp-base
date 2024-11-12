if command -v npm 2>&1 >/dev/null; then
  cd webapp-client
  npm install
  cd ..    
fi
if command -v pip3 2>&1 >/dev/null; then
  cd webapp-server
  pip3 install -r requirements.txt
  cd ..
fi
if [ -f ".env" ]; then
    cp .env.example .env
fi