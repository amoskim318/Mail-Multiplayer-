# Developed by Amos Kim and Top Boy

import re
import random
import os

# Colors
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
WHITE = "\033[1;97m"
CYAN = "\033[0;96m"
RESET = "\033[0m"


def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""{RED} __  __       _ _   __  __       _ _   _       _       
|  \/  |     (_) | |  \/  |     | | | (_)     | |      
| \  / | __ _ _| | | \  / |_   _| | |_ _ _ __ | |_   _ 
| |\/| |/ _` | | | | |\/| | | | | | __| | '_ \| | | | |
| |  | | (_| | | | | |  | | |_| | | |_| | |_) | | |_| |
|_|  |_|\__,_|_|_| |_|  |_|\__,_|_|\__|_| .__/|_|\__, |
                                         | |       __/ |
     Hola! Create Unlimited Gmails        |_|      |___/
        {CYAN}Developed by: {RED}Amos Kim & Top Boy{RESET}
    """)

    print(f"{GREEN}[Facebook]{RESET}: MIK TC")
    print(f"{GREEN}[Instagram]{RESET}: miktcamoskim")
    print(f"{YELLOW}[TOOL CREATED BY]{RESET}: BlacTech (Amos Kim - The MIK TC Top Boy)")
    print(f"{CYAN}TOP BOY WEB DEVELOPER{RESET}: Amos Kim - Cybersecurity")
    print(f"\n{WHITE}TOOL VERSION 1.0.12{RESET}\n")


def validate_email(email: str) -> bool:
    """Validate email using regex."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$"
    return re.match(pattern, email) is not None


def generate_aliases(name: str) -> list[str]:
    """Generate Gmail alias variations with dots in different positions."""
    results = set()

    def helper(prefix, rest):
        if rest:
            for i in range(1, len(rest) + 1):
                candidate = prefix + "." + rest[:i] + rest[i:]
                results.add(candidate)
                helper(prefix + "." + rest[:i], rest[i:])

    results.add(name)
    helper("", name)
    return list(results)


def email_tool():
    email = input(f"{WHITE}[{GREEN}*{WHITE}]{GREEN} Enter email address : {WHITE}")
    if not validate_email(email):
        print(f"{WHITE}[{RED}!{WHITE}]{RED} Invalid email address{RESET}")
        return email_tool()

    number = int(input(f"{WHITE}[{GREEN}*{WHITE}]{GREEN} Number of mails to generate : {WHITE}"))

    name, domain = email.split("@")
    print(f"{WHITE}[{RED}!{WHITE}]{RED} Generating...{WHITE}\n")

    aliases = generate_aliases(name)

    if number > len(aliases):
        number = len(aliases)

    selected = random.sample(aliases, number)

    # Add "+" alias trick
    alias_number = number // 2 if number // 2 < len(aliases) else number - len(aliases)
    plus_aliases = [f"{name}+{random.randint(1000,9999)}@{domain}" for _ in range(alias_number)]

    final_list = [f"{alias}@{domain}" for alias in selected] + plus_aliases
    random.shuffle(final_list)

    for addr in final_list:
        print(f"{WHITE}{addr}{RESET}")

    save_output = input(f"\n{WHITE}[{GREEN}*{WHITE}]{GREEN} Do you want to save the output (y/n) : {WHITE}")
    if save_output.lower() == "y":
        if not os.path.exists("output"):
            os.makedirs("output")
        filename = f"output/{name}.lst"
        with open(filename, "w") as f:
            f.write("\n".join(final_list))
        print(f"{WHITE}[{YELLOW}*{WHITE}]{YELLOW} Output saved at : {WHITE}{filename}{RESET}")
        print(f"{WHITE}[{RED}!{WHITE}]{RED} Exiting...\n{RESET}")
    else:
        print(f"{WHITE}[{RED}!{WHITE}]{RED} Exiting...\n{RESET}")


if __name__ == "__main__":
    banner()
    email_tool()