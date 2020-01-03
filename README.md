# Blister

create env: python3.6 -m venv Blister && cd Blister

activate environment: source env/bin/activate

install packages: pip install -r requirements.txt

install mrcnn: cd Mask_RCNN && python setup.py install && cd ../

run python: python app.py

push model ".h5" in folder Mask_RCNN
