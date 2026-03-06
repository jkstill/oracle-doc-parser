from setuptools import setup, find_packages

setup(
    name="oracle-rag",
    version="0.1.0",
    description="Oracle documentation RAG retrieval library and CLI",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[],   # only stdlib (sqlite3, json, re, pathlib, configparser)
    entry_points={
        "console_scripts": [
            "oracle-rag=oracle_rag.cli:main",
        ],
    },
)
