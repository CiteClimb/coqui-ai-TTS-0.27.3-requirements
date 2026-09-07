import os

def pip_install(r): # Run pip install with --no-deps flag
    os.system(f'pip install --no-deps {r}')

os.system('pip install packaging==26.0') # Install package installation related packages first
os.system('pip install setuptools==80.9.0')
os.system('pip install wheel==0.46.3')

with open('requirements-for-script.txt', 'r') as f:
    for i, line in enumerate(f):
        if i == 24: # The 24th line in requirements-for-script.txt (Jinja2) is the last PyTorch dependency in the file
            os.system('pip install torch==2.3.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu') # Install PyTorch via their own wheel index
        pip_install(line.rstrip())
        
pip_install('coqui-tts-trainer==0.3.2')
pip_install('coqui-tts==0.27.3') # Install coqui-tts last
