import sys
try:
    import django_mongodb_engine
    print("django_mongodb_engine imported successfully")
except ImportError as e:
    print(f"ImportError: {e}")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
