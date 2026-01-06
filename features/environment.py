"""Behave environment configuration"""
import sys
from pathlib import Path

# 將 src 目錄加入 Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

