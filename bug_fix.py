def bug_fix(error):
    raise_error(error)
    return "Bug is fixed"

def raise_error(error):
    print(f"Error Occured: {error}")

if __name__ == "__main__":
    bug_fix("Issue is NameError")