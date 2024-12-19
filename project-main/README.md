[![Open In Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1r4IRL0UA7JEoZ0ZK8PKfMyTIBHKpyhcw)

# Local Installation
If you already have RVC installed, then just download GUI.py and drop it in the root folder!
If you need to install RVC, I recommend you check the [original repo](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
Or read this at least.

I recommend you use a virtual environment

```bash
python -m venv RVC
cd RVC
git clone https://github.com/777gt/-EVC-
Scripts/activate.bat
pip install torch torchvision torchaudio
pip install -r "-EVC-/requirements.txt"
```
If you're on Windows, like me, and don't have an NVIDA graphics card, install the requirements from a different .txt:
```bash
pip install -r "-EVC-/requirements-dml.txt"
```
Also, do not forget to download the necessary models. EasyGUI uses RVC 2 40k models.

```bash
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt -O ./assets/rmvpe/rmvpe.pt
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.onnx -O ./assets/rmvpe/rmvpe.onnx
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt -O ./assets/hubert/hubert_base.pt
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D40k.pth -O ./assets/pretrained_v2/D40k.pth
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G40k.pth -O ./assets/pretrained_v2/G40k.pth
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D40k.pth -O ./assets/pretrained_v2/f0D40k.pth
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G40k.pth -O ./assets/pretrained_v2/f0G40k.pth
```
