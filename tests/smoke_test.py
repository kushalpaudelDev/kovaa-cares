import urllib.request
import urllib.error

BASE = 'http://127.0.0.1:8000'

paths = [
    '/',
    '/admin/',
    '/accounts/login/',
    '/pets/',
    '/appointments/',
    '/payments/',
    '/reviews/',
]

results = []

for p in paths:
    url = BASE + p
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            code = r.getcode()
            body = r.read(2048).decode('utf-8', errors='ignore')
            ok = code == 200
            results.append((p, code, 'OK' if ok else 'FAIL', body[:200].strip()))
    except urllib.error.HTTPError as e:
        results.append((p, e.code, 'HTTPError', str(e)))
    except Exception as e:
        results.append((p, None, 'Error', str(e)))

print('\nSmoke test results:')
for p, code, status, snippet in results:
    print(f"{p:20} {status:10} code={code} snippet={snippet!r}")

# Exit non-zero if any important page failed
failed = any(status not in ('OK','HTTPError') or (status=='OK' and code!=200) for (_,code,status,_) in results)
exit(1 if failed else 0)
