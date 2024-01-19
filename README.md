
## Step 1: Create Virtual Environment

```bash
# Create a virtual environment named 'venv'
python -m venv venv
```
## Step 2: Activate the virtual environment
```bash
venv\Scripts\activate
```

## Step 3: Install required packages
```bash
pip install -r requirements.txt
```

## Step 4A: Run on images
```
python image.py --image-path <full-image-path>
```

## Step 4B: Run on videos
```
python video.py
```