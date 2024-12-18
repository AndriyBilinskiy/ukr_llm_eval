def generate_modus_ponens(grouped_causes, consequences, names, pronoun):
    questions = []
    for group, group_causes in grouped_causes.items():
        for cause in group_causes:
            for consequence in consequences[group]:
                for name in names:
                    question = {
                        'context': f"Якщо хтось {cause}, тоді {pronoun} {consequence}.",
                        'qa_pairs': [
                            {"question": f"Якщо {name} {cause}, це означає, що {pronoun} {consequence}?",
                             "answer": "так"},
                            {"question": f"Якщо {name} {cause}, це означає, що {pronoun} не {consequence}?",
                             "answer": "ні"},
                            {"question": f"Якщо {name} не {cause}, це означає, що {pronoun} {consequence}?",
                             "answer": "ні"},
                            {"question": f"Якщо {name} не {cause}, це означає, що {pronoun} не {consequence}?",
                             "answer": "ні"}
                        ]
                    }
                    questions.append(question)
    return questions
