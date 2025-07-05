#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from company_picker.crew import CompanyPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """ Main function """
    inputs = {
        'sector': 'fashion'
    }
    result = CompanyPicker().crew().kickoff(inputs=inputs)
    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)

if __name__ == "__main__":
    run()