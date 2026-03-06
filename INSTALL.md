
# Install as a package (editable mode, so changes take effect immediately)
cd ~/ai/doc-parser
pip install -e . --break-system-packages

# Set up config
cp oracle_rag.conf.example ~/.oracle_rag.conf
# edit ~/.oracle_rag.conf with your actual paths

# Run tests
python test_retriever.py

# Try it out
oracle-rag stats
oracle-rag search "session wait events"
oracle-rag lookup DBA_SEGMENTS
oracle-rag lookup DBMS_STATS.GATHER_TABLE_STATS
oracle-rag package DBMS_STATS --compact
oracle-rag related DBA_SEGMENTS

# Pipe to Ollama
oracle-rag search "how to gather table statistics" | ollama run llama3

# Pipe to Gemini CLI
oracle-rag search "redo log archiving" --format markdown | gemini


