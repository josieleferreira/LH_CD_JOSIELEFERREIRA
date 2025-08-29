import os
import joblib
from typing import Iterable, Mapping, Tuple, List

def save_models(ns: Mapping[str, object], names: Iterable[str], outdir: str = "modelos_pkl") -> Tuple[List[str], List[str], List[Tuple[str, str]]]:
    """
    Salva objetos presentes em `ns` (ex.: globals()) cujos nomes estão em `names`.

    Retorna (saved_paths, skipped_names, errors_list).
    """
    os.makedirs(outdir, exist_ok=True)
    saved, skipped, errors = [], [], []
    for name in names:
        obj = ns.get(name)
        if obj is None:
            skipped.append(name)
            continue
        try:
            path = os.path.join(outdir, f"{name}.pkl")
            joblib.dump(obj, path)
            saved.append(path)
        except Exception as e:
            errors.append((name, str(e)))
    return saved, skipped, errors

def quick_report(saved, skipped, errors):
    print("[Resumo do salvamento]")
    print("Salvos:", saved)
    print("Ignorados (não definidos):", skipped)
    print("Erros:", errors)
