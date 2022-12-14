import os
import subprocess

here = os.getcwd()
[[subprocess.run(["python3","solve.py"]) for ii in sorted(os.listdir(f"{here}/{i}")) if  print(f"----------\nAnswer for {i.replace('d','Day ')}\n{ii.replace('p','Part ')} ") or os.chdir(f"{here}/{i}/{ii}")==None] for i in sorted(os.listdir(here)) if i.startswith("d")]
