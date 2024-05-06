
import sys
import os
sys.path.append('../')
os.environ['PISA_PATH'] = '/root/Portal-to-ISAbelle/src/main/python'
from dsp_utils import Checker, LMFunction

class MathTheoremProvingService:
    def __init__(self, isa_path, theory_file, port=9000):
        self.isa_path = isa_path
        self.theory_file = theory_file
        self.port = port
        self.checker = Checker(
            working_dir=os.path.dirname(theory_file),
            isa_path=isa_path,
            theory_file=theory_file,
            port=port
        )
        print(self.checker.get_status())

    def prove_theorem(self, informal_statement, formal_statement):
        # Step 1: Generate a draft (informal proof)
        p_draft = LMFunction('gpt-4')
        draft = p_draft.f("Draft an informal solution similar to below.", informal_statement)

        # Step 2: Generate a formal sketch based on the draft
        p_sketch = LMFunction('gpt-4')
        sketch_prompt = "Translate the informal solution into a sketch of the formal Isabelle proof."
        for example in examples:
            sketch_prompt += (example['prompt'] + "\n\n")
        sketch_prompt += "Informal:\n(*### Problem\n\n"
        sketch_prompt += draft + "\n\n"
        sketch_prompt += formal_statement + "\n*)"
        zf = p_sketch.f(sketch_prompt)

        # Step 3: Use Sledgehammer to prove the remaining conjectures in the sketch
        result = self.checker.check(zf)

        # Return the result
        return result

# Example usage:
if __name__ == "__main__":
    # Set up the paths and port for the Isabelle proof assistant
    isa_path = '/workspace/huangyongfeng/ananke/example/pipeline/math_experiment/LEGO-Prover/Isabelle2022'
    theory_file = '/workspace/huangyongfeng/ananke/example/pipeline/math_experiment/LEGO-Prover/Isabelle2022/src/HOL/Examples/Interactive.thy'
    port = 9000

    # Initialize the service
    service = MathTheoremProvingService(isa_path, theory_file, port)

    # Example LaTeX input
    # latex_statement = r"""theorem
    # fixes x :: int
    # assumes h0: "even x"
    # shows "odd (x+5)"
    # """
    
    # # Call the service to prove the theorem
    # result = service.prove_theorem("Show that if x is even, then x+5 is odd", latex_statement)

    # # Output the result
    # if result['success']:
    #     print("Proof successful:")
    #     print(result['theorem_and_proof'])
    # else:
    #     print("Proof failed.")