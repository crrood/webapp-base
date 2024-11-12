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
if [ ! -f "webapp-client/shared/.env" ]; then
    cp webapp-client/shared/.env.example webapp-client/shared/.env
fi