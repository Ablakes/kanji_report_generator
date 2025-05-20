import subprocess

def request_kanji_report(email):
    try:
        result = subprocess.run(
            ["python3", "generate_report.py"],
            input=email + "\n",  
            capture_output=True,
            text=True
        )
        print("Microservice output:")
        print(result.stdout)

        if result.stderr:
            print("Microservice error output:")
            print(result.stderr)

    except Exception as e:
        print(f"Failed to run microservice: {e}")

if __name__ == "__main__":
    request_kanji_report("test2@gmail.com")
