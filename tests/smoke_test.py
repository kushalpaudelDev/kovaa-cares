import urllib.request
import urllib.error
import sys

BASE_URL = 'http://127.0.0.1:8000'
PATHS = [
    '/', '/admin/', '/accounts/login/', '/pets/', 
    '/appointments/', '/payments/', '/reviews/'
]

results = []

for path in PATHS:
    try:
        with urllib.request.urlopen(BASE_URL + path, timeout=10) as response:
            code = response.getcode()
            body = response.read(2048).decode('utf-8', errors='ignore')
            status = 'OK' if code == 200 else 'FAIL'
            results.append((path, code, status, body[:200].strip()))
    except urllib.error.HTTPError as e:
        results.append((path, e.code, 'HTTPError', str(e)))
    except Exception as e:
        results.append((path, None, 'Error', str(e)))

print('\nSmoke test results:')
for path, code, status, snippet in results:
    print(f"{path:20} {status:10} code={code} snippet={snippet!r}")

has_failures = any(
    status not in ('OK', 'HTTPError') or (status == 'OK' and code != 200)
    for _, code, status, _ in results
)
sys.exit(1 if has_failures else 0)
