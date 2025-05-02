#!/bin/bash

echo "🚀 Removing old broken environment (if exists)..."
conda deactivate
conda remove --name urdu_tts_env --all -y

echo "✅ Creating new clean environment..."
conda create --name urdu_tts_env python=3.10 -y
conda activate urdu_tts_env

echo "📦 Installing stable scientific libraries with conda..."
conda install numpy scipy scikit-learn -y

echo "📦 Installing stable PyTorch (CPU-only) with pip..."
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cpu

echo "📦 Installing Transformers, TTS, Pydub, and Sentencepiece with pip..."
pip install transformers TTS pydub sentencepiece

echo "🎉 Environment setup complete!"
echo "👉 Now activate it with: conda activate urdu_tts_env"
echo "👉 Then run your script: python test_translation_tts.py"
