from app.summarizer import generate_summary

if __name__ == "__main__":
    print("Paste or type in your text below (then press Enter twice):")
    user_input = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        user_input += line + " "

    summary = generate_summary(user_input)
    print("\nSummary:\n", summary)
