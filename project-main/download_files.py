import subprocess, os
assets_folder = "./assets/"
if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)
files = {
    "rmvpe/rmvpe.pt":"https://huggingface.co/dipankerz/rvc_0.0.0/resolve/main/rmvpe.pt",
    "hubert/hubert_base.pt":"https://huggingface.co/dipankerz/rvc_0.0.0/resolve/main/hubert_base.pt",
    "pretrained_v2/D48k.pth":"https://huggingface.co/dipankerz/rvc_0.0.0/resolve/main/D48k.pth",
    "pretrained_v2/G48k.pth":"https://huggingface.co/dipankerz/rvc_0.0.0/resolve/main/G48k.pth",
    "pretrained_v2/f0D48k.pth":"https://huggingface.co/dipankerz/rvc_0.0.0/resolve/main/f0D48k.pth",
    "pretrained_v2/f0G48k.pth":"https://huggingface.co/dipankerz/rvc_0.0.0/resolve/main/f0G48k.pth"
}
for file, link in files.items():
    file_path = os.path.join(assets_folder, file)
    if not os.path.exists(file_path):
        try:
            subprocess.run(['wget', link, '-O', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {file}: {e}")


