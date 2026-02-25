import sys
import traceback

print("Python version:", sys.version)
print("Starting import diagnostic...")

try:
    import django_mongodb_engine.base
    print("SUCCESS: django_mongodb_engine.base imported")
except ImportError as e:
    print("ImportError:", e)
    traceback.print_exc()
except Exception as e:
    print("Unexpected Error:", type(e).__name__, "-", e)
    traceback.print_exc()

print("Diagnostic finished.")
