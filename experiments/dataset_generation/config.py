LOGIC_RULE_TEMPLATES = {
    'modus_ponens': {
        'context': "Якщо хтось {cause_male}, тоді він {consequence_male}.",
        'qa_pairs': [
            {"question": "Якщо {name} {cause}, це означає, що {pronoun} {consequence}?", "answer": "так"},
            {"question": "Якщо {name} {cause}, це означає, що {pronoun} не {consequence}?", "answer": "ні"},
            {"question": "Якщо {name} не {cause}, це означає, що {pronoun} {consequence}?", "answer": "ні"},
            {"question": "Якщо {name} не {cause}, це означає, що {pronoun} не {consequence}?", "answer": "ні"}
        ]
    },
    'modus_tollens': {
        'context': "Якщо хтось {cause_male}, тоді він {consequence_male}.",
        'qa_pairs': [
            {"question": "Якщо {name} не {consequence}, це означає, що {pronoun} не {cause}?", "answer": "так"},
            {"question": "Якщо {name} не {consequence}, це означає, що {pronoun} {cause}?", "answer": "ні"},
            {"question": "Якщо {name} {consequence}, це означає, що {pronoun} {cause}?", "answer": "ні"},
            {"question": "Якщо {name} {consequence}, це означає, що {pronoun} не {cause}?", "answer": "ні"}
        ]
    },
    'material_implication': {
        'context': "Якщо хтось {cause_male}, тоді він {consequence_male}.",
        'qa_pairs': [
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} не {cause}, 2. {pronoun} {consequence}?", "answer": "так"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} не {cause}, 2. {pronoun} не {consequence}?", "answer": "так"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} {cause}, 2. {pronoun} {consequence}?", "answer": "ні"},
            {"question": "Враховуючи контекст, чи можна зробити висновок, що хоча б одне з наступних тверджень завжди є правдивим? 1. {name} {cause}, 2. {pronoun} не {consequence}?", "answer": "так"}
        ]
    }
}