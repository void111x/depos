"""Execute every question using its built-in sample inputs."""
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
records = json.loads((root / 'manifest.json').read_text())
failures = []
for record in records:
    print('\n===', record['path'], record['title'], '===', flush=True)
    result = subprocess.run([sys.executable, str(root / record['path']), '--demo'])
    if result.returncode:
        failures.append(record['path'])
print(f'\n{len(records) - len(failures)}/{len(records)} scripts succeeded.')
if failures:
    print('Failures:', failures)
    sys.exit(1)
