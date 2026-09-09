# How to use this repo
## Using requirements.txt
If you are using requirements.txt, just run `pip install --no-deps -r requirements.txt` (in your virtual environment / Anconda). *However*, this doesn't seem to always install the exact packages that were frozen. If this doesn't work, you might want to try running the script.
## Using requirements-script.py
If you are using this script, just run the python file. It runs `pip install --no-deps <package>` for every single package (except the ones frozen in the script itself), so it should enforce the versions better.
## Using conda_environment_coqui-tts.yml
If you are using conda, you can run `conda env create -f conda_environment_coqui-tts.yml` to attempt to recreate my conda environment.

Note: This environment was working for an Intel CPU with no discrete GPU, so this may not work for a discrete GPU if you only simply change the index URL in requirements-script.py.
Finally, always remember that if this doesn't immediately work, you can always modify the script, the requirements.txt file, or just randomly try different installation orders or versions without the script! Manual dependency resolving is sometimes unavoidable, unfortunately.
