instalar con: pip install .
(creo que se puede llegar y ejecutar en la carpeta sin necesidad del pip)

python -m garak --help: ayuda
python -m garak --list_probes: muestra los plugins disponibles


comando de ejemplo, gpt2 lo instala automaticamente --probes <plugins a ejecutar>:
python -m garak --model_type huggingface --model_name gpt2 --probes 3_discursoNoDeseado.Deadnaming

comando con un respuestas en blanco
python -m garak --model_type test --probes 3_discursoNoDeseado.Deadnaming



En relacion al codigo, lo importante esta en la carpeta de probes, que son los plugins. Los detectores tambien