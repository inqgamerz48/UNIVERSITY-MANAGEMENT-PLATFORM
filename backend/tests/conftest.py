import sys
import os
import pytest
from pathlib import Path

# Add the 'apps/api' root directory to sys.path
api_root = str(Path(__file__).parent.parent)
sys.path.insert(0, api_root)

# Fixtures will go here (e.g. async db session)
