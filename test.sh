cd webapp-client
if [ "$(npm list | grep vite)" ]; then
    npx vite build
else
    echo "false"
fi
cd ..