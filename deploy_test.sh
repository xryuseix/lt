python make_slides_json.py
if [ -d dist ]; then
    rm -rf dist/*
else
    mkdir dist
fi
yarn run build
python build.py