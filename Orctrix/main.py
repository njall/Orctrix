"""
Main function
"""
import sys

import orcid

def main():
    if len(sys.argv) > 1:
        orcid_json = orcid.get_json(sys.argv[1])
        print(orcid_json)
    else:
        print("Please supply a ORCID ID.")

# TODO Replace this with properly package
if __name__ == "__main__":
    main()
