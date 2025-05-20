import subprocess

def request_kanji_report(email):
    try:
        # Call your microservice file as a standalone script
        result = subprocess.run(
            ["python3", "generate_report.py"],
            input=email + "\n",   # simulate typing the email into input()
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

# Example usage
if __name__ == "__main__":
    request_kanji_report("test@gmail.com")
