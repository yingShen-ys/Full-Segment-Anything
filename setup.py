from setuptools import find_packages, setup

setup(
    name="full_segment_anything",
    version="1.0",
    install_requires=[],
    packages=find_packages(),
    extras_require={
        "all": ["matplotlib", "pycocotools", "opencv-python", "onnx", "onnxruntime"],
        "dev": ["flake8", "isort", "black", "mypy"],
    },
)
