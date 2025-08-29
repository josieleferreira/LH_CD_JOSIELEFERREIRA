


import os
import joblib
from typing import Dict, List

def load_models(names: List[str], indir: str = "modelos_pkl") -> Dict[str, object]:
    """
    Carrega todos os modelos cujo nome esteja em `names` a partir do diretório `indir`.

    Retorna um dicionário {nome: objeto}.
    """
    models = {}
    for name in names:
        path = os.path.join(indir, f"{name}.pkl")
        if not os.path.exists(path):
            print(f"[AVISO] Arquivo não encontrado: {path}")
            continue
        try:
            models[name] = joblib.load(path)
            print(f"[OK] carregado: {path}")
        except Exception as e:
            print(f"[ERRO] {name} -> {e}")
    return models
