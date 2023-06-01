# Flask + Vite + KnockoutJS

This was a test app to build a flask + vite + knockout app.

## usage

Ensure the frontend bundles, watches
```
cd statics
npm i
npm run autobuild // this will auto bundle if the code changes
```

Then run the backend
```
cd ..
python3 -m venv venv
source venv/bin/activate
pip install flask
python main.py
```