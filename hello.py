stages = ["environment", "git_setup", "first_script"]

for idx, stage  in enumerate (stages, start=1):
    print(f"[{idx}/{len(stages)}] Ready: {stage}")